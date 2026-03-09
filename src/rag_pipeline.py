from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from src.vector_store import create_vector_store
from src.llm_model import load_llm


def build_qa_chain():

    # create vector DB
    vectorstore = create_vector_store()

    retriever = vectorstore.as_retriever()

    # load LLM
    llm = load_llm()

    template = """
    Use the following context if it is relevant to the question.

    If the context does not contain the answer, answer using your general knowledge.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain