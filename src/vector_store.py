# vector_store.py
# ----------------------------------------------
# THis module is responsible for turning rae documents into searchable math.
# Loads a PDF document using LangChain's PyPDFLoader. 
# Then applies advanced semantic chunking to maintain contextual integrity.
# Converts those text chunks into numerical vectors using HuggingFace's sentence-transformers model.
# Then creates a FAISS vector store for efficient retrieval.
# ----------------------------------------------


# =========================================
# Libraries
# ------------------------------------
# PyPDFLoader : For loading PDF documents.
# HuggingFaceEMbeddings : For generating embeddingd using HuggingFace models.
# SemanticChunker : For advanced text splitting based on semantic similarity.
# FAISS : For creating a vector store for efficient similarity search.
# ========================================
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker


# =========================================
# create_vector_store Function
# ------------------------------------
# This function takes a file path to a PDF, loads the document, applies semantic chunking to maintain contextual integrity. 
# Then creates a FAISS vector store for efficent retrieval.
# =========================================
def create_vector_store(file_path):
    """Loads a PDF, applies semantic chunking, and returns a FAISS vector store."""
    
    # Load the dynamic PDF file from the provided path
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Initialize Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Apply Advanced Semantic Chunking
    text_splitter = SemanticChunker(
        embeddings, 
        breakpoint_threshold_type="percentile"
    )
    
    # Split the loaded documents into chunks
    chunks = text_splitter.split_documents(documents)

    # Create and return the FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore