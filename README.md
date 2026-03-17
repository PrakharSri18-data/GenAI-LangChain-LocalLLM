# 🧠 Retrieval-Augmented Generation (RAG) QA System
A lightweight Generative AI Question-Answering system built using LangChain, FAISS, HuggingFace embeddings, and a local LLM (Ollama - Phi3). This project demonstrates how to build a Retrieval-Augmented Generation (RAG) pipeline that answers questions based on custom documents.

---

## 🚀 Project Overview
- This project implements a RAG pipeline that:
     - Loads custom text data
     - Converts it into vector embeddings
     - Stores them using FAISS
     - Retrieves relevant context for a query
     - Uses an LLM to generate accurate answers
     - It combines information retrieval + generative AI, making responses more factual and context-aware.

---

## 📂 Project Structure
- data
     - document.txt
- src
     - llm_model.py
     - rag_pipeline.py
     - vector_store.py
- gitignore
- LICENSE
- README.md
- app.py
- requirements.txt

---

## ⚙️ How It Works

### 1. Document Processing
- Loads text from documents.txt
- Splits into smaller chunks for better retrieval
- 📄 See implementation:

### 2. Embeddings & Vector Store
- Uses HuggingFace embeddings (all-MiniLM-L6-v2)
- Stores vectors using FAISS

### 3. LLM Integration
- Uses Ollama with phi3:mini model
- 📄 LLM loader:

### 4. Retrieval-Augmented QA
- Retrieves relevant chunks
- Passes them to LLM with a custom prompt
- Generates contextual answers
- 📄 QA pipeline:

---

🧩 Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Ollama (Phi3 Mini)
- Streamlit / CLI (via app.py)

---

## 🛠️ Installation

### 1. Clone the Repository
- git clone https://github.com/your-username/rag-genai-project.git
- cd rag-genai-project

### 2. Create Virtual Environment
- python -m venv venv
- source venv/bin/activate   # Mac/Linux
- venv\Scripts\activate      # Windows

### 3. Install Dependencies
- pip install -r requirements.txt

### 4. Install & Run Ollama
- Download Ollama from: https://ollama.com
- Run the model:
     - ollama run phi3:mini
 
---

## ▶️ Usage
- Run the application:
     - python app.py
- Then:
     - Enter your query
     - The system retrieves relevant context
     - LLM generates an answer

---

## 🔥 Features
- ✅ Local LLM (no API cost)
- ✅ Fast vector search using FAISS
- ✅ Custom knowledge base support
- ✅ Modular and scalable design
- ✅ Clean LangChain integration

---

## 👤 Author
- Prakhar Srivastava
- Aspiring Data Scientist & Business Analyst | Machine Learning, Deep Learning & Generative AI Enthusiast
