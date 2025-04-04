import streamlit as st
import pandas as pd
import sqlite3
import os
from groq import Groq
from sqlalchemy import create_engine, text

# App Title
st.set_page_config(page_title="Natural Language to SQL with Groq", layout="wide")
st.title("🧠💬 Natural Language to SQL with Groq API")

# Load Groq API key from .streamlit/secrets.toml
groq_api_key = st.secrets["groq_api_key"]

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# File uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")
        st.write("📊 Preview of Uploaded Data:")
        st.dataframe(df.head())

        # Normalize column names (remove spaces and make lowercase)
        df.columns = [col.strip().replace(" ", "_").replace("-", "_") for col in df.columns]

        # Save to SQLite
        conn = sqlite3.connect("uploaded_data.db")
        df.to_sql("uploaded_table", conn, if_exists="replace", index=False)

        user_input = st.text_input("Ask your question in natural language")

        if user_input:
            with st.spinner("Generating SQL Query using Groq..."):
                prompt = f"""
                You are an expert data analyst.
                Translate the following natural language question into an executable SQLite SQL query.
                Use only the following table: 'uploaded_table'
                Available columns: {list(df.columns)}
                Only return the SQL query without any explanation, markdown formatting, or comments.
                Question: {user_input}
                SQL Query:
                """
                
                try:
                    response = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    sql_code = response.choices[0].message.content.strip()

                    # Clean and enforce correct table name and column format
                    sql_code = sql_code.replace("table_name", "uploaded_table")

                    # Replace column names with corrected ones if needed
                    for col in df.columns:
                        sql_code = sql_code.replace(col.replace("_", " "), col)

                    st.code(sql_code, language='sql')

                    # Execute the SQL query
                    try:
                        engine = create_engine("sqlite:///uploaded_data.db")
                        with engine.connect() as connection:
                            result = connection.execute(text(sql_code))
                            result_df = pd.DataFrame(result.fetchall(), columns=result.keys())

                            st.success("✅ Query Executed Successfully!")
                            st.dataframe(result_df)

                    except Exception as sql_error:
                        st.error(f"\n\n❌ SQL Execution Error:\n\n{sql_error}")

                except Exception as api_error:
                    st.error(f"\n\n❌ Groq API Error:\n\n{api_error}")

    except Exception as file_error:
        st.error(f"\n\n❌ File Processing Error:\n\n{file_error}")
