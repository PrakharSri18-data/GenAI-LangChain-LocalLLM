from langchain_community.llms import Ollama

def load_llm():

    llm = Ollama(
        model="phi3:mini"
    )

    return llm