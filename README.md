# GenAI-LangChain-LocalLLM

> 🧠 A robust, local Large Language Model (LLM) chatbot built using LangChain, Streamlit, and the Phi-3 model.

This project enables users to interact with a lightweight generative AI model directly on their local machine, ensuring fast inference, complete data privacy, and zero reliance on external API keys or internet connectivity for query processing.

---

## ✨ Features

- **100% Local Execution** — Run generative AI entirely on your hardware. Keep your conversational data private and secure.
- **Phi-3 Integration** — Leverages the highly efficient and capable Phi-3 model via Ollama, optimized for local environments without sacrificing conversational quality.
- **LangChain Orchestration** — Utilizes the LangChain framework to manage prompts, handle conversational memory, and structure the RAG (Retrieval-Augmented Generation) pipeline efficiently.
- **Interactive UI** — Features a clean, responsive chatbot interface built with Streamlit, making it easy to interact with the model right out of the box.

---

## 📂 Repository Structure

```
GenAI-LangChain-LocalLLM/
├── Outputs/                 # Directory containing visual proof of model outputs and citations
│   ├── Output 1/
│   │   ├── Citation 1.png
│   │   ├── Citation 2.png
│   │   ├── LLM Generated Answer.png
│   │   └── Streamlit Home Page & Question.png
│   └── Output 2/
│       ├── Citation 1.png
│       ├── Citation 2.png
│       ├── LLM Generated Answer.png
│       └── Streamlit Home Page & Question.png
├── Test Datasets/           # Sample datasets for evaluating and testing model accuracy
│   └── Data Analytics using SQL.pdf
├── src/                     # Core modules, LangChain utilities, and backend logic
│   ├── llm_model.py         # Handles the initialization and configuration of the local LLM
│   ├── rag_pipeline.py      # Orchestrates the prompt management and generation pipeline
│   └── vector_store.py      # Manages document embeddings and vector database operations
├── .gitignore               # Ignored files and directories
├── LICENSE                  # MIT License
├── app.py                   # Main Streamlit application entry point
└── requirements.txt         # List of all Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ installed on your machine.
- A machine capable of running local LLMs (sufficient RAM/VRAM depending on the quantization of the Phi-3 model used).

### Installation

**1. Clone the repository:**

```bash
git clone https://github.com/PrakharSri18-data/GenAI-LangChain-LocalLLM.git
cd GenAI-LangChain-LocalLLM
```

**2. Create a virtual environment (Recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install the dependencies:**

```bash
pip install -r requirements.txt
```

**4. Model Setup:**

Ensure you have the local Phi-3 model initialized (e.g., via Ollama) and available to the scripts in the `src/` directory.

### Running the Application

Launch the Streamlit interface by running the following command in your terminal:

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to start chatting with your local AI!

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| LLM Framework | LangChain |
| Generative Model | Phi-3 |
| Vector Database | FAISS (handled in `vector_store.py`) |
| Frontend / UI | Streamlit |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) © 2026 Prakhar Srivastava.

---

## 🙋 Author

**Prakhar Srivastava**

Data Analyst & AI Engineer | Machine Learning, Deep Learning, Generative AI, Prompt Engineering & Agentic AI
