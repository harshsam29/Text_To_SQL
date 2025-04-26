# 🧠 Natural Language to SQL (Text + Voice + Fuzzy Matching)

Turn your CSV data into instant insights!  
Ask questions in **natural language** (text or voice), and get **SQLite queries** generated, corrected, and executed — fully inside **Streamlit**.

---

## 🚀 Features

- 📤 Upload any CSV file
- 📝 Type or 🎙️ Speak your question
- 🤖 LLM-powered SQL generation (local **Mistral** model via **Ollama**)
- 🛠️ Fuzzy matching to auto-correct column names
- 🔍 Instant SQL execution
- 📊 Automatic chart generation (bar charts)
- 📁 Download query results as CSV
- 🧠 Query history (Chat memory)

---

## 🛠️ Tech Stack

- Python
- Streamlit (Web UI)
- Pandas (Data handling)
- SQLite (In-memory database)
- Ollama (Local LLM model - Mistral)
- FuzzyWuzzy (Fuzzy string matching)
- SpeechRecognition (Voice input)

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
