from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

def create_vector_store():

    with open("data/documents.txt") as f:
        text = f.read()

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(docs, embeddings)

    return vectorstore