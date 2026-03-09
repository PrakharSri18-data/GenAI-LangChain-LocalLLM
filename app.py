import streamlit as st
from src.rag_pipeline import build_qa_chain

st.title("LocalGPT LangChain Chatbot")

qa_chain = build_qa_chain()

user_question = st.text_input("Ask a question")

if user_question:

    response = qa_chain.run(user_question)

    st.write(response)