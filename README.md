# 🧠 Local Generative AI RAG System

A **Retrieval-Augmented Generation (RAG)** question-answering application built with **LangChain**, **FAISS**, **HuggingFace Embeddings**, and a fully **local LLM via Ollama (Phi-3 Mini)**. Upload any PDF document and get accurate, context-grounded answers — no external API keys, no data leaves your machine.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.16-green)](https://docs.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.55.0-red?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Overview

This project implements a fully **local, private, and cost-free** RAG pipeline that:

- Accepts a **PDF document** as input via a Streamlit web interface
- Splits the document into chunks and converts them into **vector embeddings** using `sentence-transformers/all-MiniLM-L6-v2`
- Stores those embeddings in a **FAISS** vector index for fast semantic search
- Retrieves the most relevant chunks for a user's query
- Passes the retrieved context to a **local Phi-3 Mini LLM** (via Ollama) to generate accurate, factual answers
- Displays the answer alongside **source citations** with page numbers, so you can verify every response

---

## 📂 Project Structure

```
GenAI-LangChain-LocalLLM/
│
├── data/
│   └── document.txt          # Sample document for testing
│
├── src/
│   ├── llm_model.py          # Loads the local Ollama (Phi-3) LLM
│   ├── rag_pipeline.py       # Builds the LangChain RetrievalQA chain
│   └── vector_store.py       # Creates FAISS vector store from PDF
│
├── app.py                    # Streamlit web application (main entry point)
├── requirements.txt          # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ How It Works

### 1. Document Ingestion
The user uploads a PDF via the Streamlit sidebar. The file is saved to a secure temporary location, processed by LangChain's `PyPDFLoader`, then deleted immediately to avoid storage bloat.

### 2. Chunking & Embedding
The document is split into smaller overlapping chunks. Each chunk is embedded using HuggingFace's `all-MiniLM-L6-v2` sentence transformer model and stored in a **FAISS** vector index.

### 3. Local LLM via Ollama
The LLM backend uses **Ollama** running `phi3:mini` entirely on your local machine — no API calls, no costs, no data exposure.

### 4. Retrieval-Augmented QA
When a question is submitted, the pipeline retrieves the top-k most semantically relevant chunks and passes them to the LLM with a custom prompt. The LLM generates a grounded answer based only on the retrieved context.

### 5. Source Citations
Every answer is accompanied by an expandable **"Show Your Work"** panel that displays the exact source passages and page numbers used to generate the response.

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `langchain` | 0.2.16 | RAG chain orchestration |
| `langchain-community` | 0.2.16 | Ollama LLM & PDF loaders |
| `langchain-huggingface` | 0.0.3 | HuggingFace embeddings integration |
| `faiss-cpu` | 1.13.2 | Vector similarity search |
| `sentence-transformers` | 5.2.3 | `all-MiniLM-L6-v2` embeddings |
| `streamlit` | 1.55.0 | Web UI |
| `torch` | 2.10.0 | ML backend for embeddings |
| `transformers` | 5.3.0 | Tokenizers & model utilities |
| `python-dotenv` | 1.2.2 | Environment variable management |

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com) installed and running

### 1. Clone the Repository

```bash
git clone https://github.com/PrakharSri18-data/GenAI-LangChain-LocalLLM.git
cd GenAI-LangChain-LocalLLM
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull and Serve the Phi-3 Model via Ollama

```bash
ollama pull phi3:mini
ollama serve
```

> Ollama must be running in the background before launching the app.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 💡 Usage

1. **Upload a PDF** using the sidebar file uploader
2. Wait for the document to be processed and the vector store to be built
3. **Type your question** in the main input field
4. View the **AI-generated answer** and expand **"📄 View Source Citations"** to see which pages the answer was drawn from
5. Click **"Reset Session / Upload New File"** to analyze a different document

---

## ✅ Key Features

- 🔒 **Fully private** — all processing happens locally, no data sent to external servers
- 💸 **Zero API cost** — runs entirely on your machine with open-source models
- 📄 **PDF support** — any PDF can be uploaded and queried
- 🔍 **Source citations** — every answer links back to the original page in the document
- 🧩 **Modular design** — vector store, LLM, and pipeline are cleanly separated in `src/`
- ♻️ **Session management** — the QA chain is cached in Streamlit session state to avoid redundant processing

---

## 📚 Resources

- [LangChain Docs](https://docs.langchain.com)
- [Ollama Model Library](https://ollama.com/library)
- [FAISS by Meta AI](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit Docs](https://docs.streamlit.io)

---

## 👤 Author

**Prakhar Srivastava**  
Aspiring Data Scientist & Business Analyst | Machine Learning, Deep Learning & Generative AI Enthusiast

- GitHub: [@PrakharSri18-data](https://github.com/PrakharSri18-data)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> ⭐ If you found this project useful, consider giving it a star!
