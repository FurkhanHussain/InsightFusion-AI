# 🤖 InsightFusion AI: GenAI-Powered Business Document Assistant

**InsightFusion AI** is a GenAI-powered Retrieval-Augmented Generation (RAG) system that enables users to ask natural language questions across combined structured (CSV) and unstructured (PDF) business documents — returning accurate, citation-backed answers using local LLMs and embeddings.

---

### ✅ Features
- 🔍 Combine **PDF reports** and **CSV data** for unified Q&A
- 🤖 Powered by **LangChain + Ollama (LLaMA3 + embeddings)**
- 💬 Ask natural questions like "Why did Q4 revenue drop?"
- 📎 Context-aware answers with traceable source references
- 🖥️ Optional **Streamlit UI** for interactive exploration

---

### 🛠️ Tech Stack

- Python 3.10+
- LangChain, FAISS
- Ollama (with `llama3` + `nomic-embed-text`)
- PyMuPDF, Pandas
- Streamlit (for web UI)

---

### 💼 Real-World Use Cases

- Analyze financial reports to explain performance changes
- Summarize legal or policy documents for quick review
- Extract key trends from monthly departmental CSVs
- Enable customer service agents to query internal PDFs + reports

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
