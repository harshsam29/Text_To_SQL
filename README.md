# 🚀 Natural Language to SQL Query Generator with LLMs

This project allows users to upload a CSV or Excel file and query the data using natural language. The system uses a Large Language Model (via Groq API) to translate the query into SQL and fetch results from an SQLite database — all in a simple and interactive Streamlit app.

---

## 🔍 Features

- 🧠 **LLM-powered** Natural Language to SQL translation
- 📂 Upload any CSV or XLSX file
- 🔄 Dynamic table creation and query execution with SQLite
- ✅ Query results and AI-generated SQL displayed in real time
- 🌐 Streamlit-based interactive web interface
- 🔐 Secure API key management using `secrets.toml`

---

## 📊 Sample Use Cases

- **"Show the top 5 most expensive cars."**
- **"List all diesel cars manufactured after 2018."**
- **"Count how many cars are available for each fuel type."**

---

## 🛠 Tech Stack

- Python 3.8+
- Streamlit
- SQLite
- Groq API (LLaMA3 model)
- Pandas
- SQLAlchemy

---

## 📁 Project Structure

