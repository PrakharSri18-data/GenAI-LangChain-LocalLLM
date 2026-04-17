# src/llm_model.py
# ------------------------------------------------
# This module initializes the AI model used in the application.
# It defines a function to load the local Ollama model (Phi-3) using LangChain's Ollama wrapper.
# ------------------------------------------------


# =========================================
# Libraries
# ------------------------------------
# Ollama : For loading the local Ollama model.
# =========================================
from langchain_community.llms import Ollama

def load_llm():
    """Initializes and returns the local Ollama model."""
    llm = Ollama(
        model="phi3:mini"
    )

    return llm