# 📊 InsightRAG: Business Document + CSV Q&A Assistant

**InsightRAG** is a Retrieval-Augmented Generation (RAG) application that lets you ask natural language questions over business documents like PDFs and structured CSV reports — with contextual, source-cited answers.

### ✅ Features
- 🔍 Ingest and combine **unstructured (PDF)** and **structured (CSV)** data
- 🤖 Powered by **Ollama + LangChain** (uses `llama3` + `nomic-embed-text`)
- 💬 Ask natural questions like "Why did Q4 revenue drop?"
- 📎 Returns relevant answers from both data types with citations
- 🖥️ Optional Streamlit UI for interactive querying

---

### 🛠️ Tech Stack

- Python 3.10+
- LangChain
- Ollama (`llama3` + `nomic-embed-text`)
- FAISS (local vector store)
- PyMuPDF (for PDF parsing)
- Pandas (for CSV parsing)
- Streamlit (optional web UI)

---

### 🚀 Getting Started

#### 1. Install Requirements

```bash
pip install -r requirements.txt
```

#### 2. Install and Run Ollama

```bash
# Install Ollama: https://ollama.com
ollama pull llama3
ollama pull nomic-embed-text
```

#### 3. Run the CLI Tool

```bash
python main.py
```

#### 4. Use Streamlit UI (optional)

```bash
streamlit run streamlit_app.py
```

---

### 📁 Project Structure

```
insightrag/
├── ingest/            # Loaders for PDFs and CSVs
│   ├── pdf_loader.py
│   └── csv_loader.py
├── rag/               # Vector store and RAG chain logic
│   ├── vectorstore.py
│   └── qa_chain.py
├── data/              # Upload your sample files here
├── main.py            # Core app logic
├── streamlit_app.py   # Optional web interface
├── requirements.txt
└── README.md
```

---

### 🧪 Sample Queries
- "Summarize key points from the policy document."
- "What were the most expensive departments last month?"
- "Why did revenue decrease in Q3?"

---

### 📌 Notes
- Ollama must be running locally before you launch the app.
- You can switch to other LLMs or embedding models by modifying `qa_chain.py` and `vectorstore.py`.

---
