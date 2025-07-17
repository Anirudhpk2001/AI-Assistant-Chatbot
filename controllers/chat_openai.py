import os
import json
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain import hub
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Load vector store once (global initialization for efficiency)
persist_dir = "my_vector_db"
embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)

vectorstore = Chroma(
    persist_directory=persist_dir,
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever()

# Load RAG prompt from LangChain Hub
prompt_template = hub.pull("rlm/rag-prompt")

# Initialize LLM
llm = ChatOpenAI(openai_api_key=openai_key)

# Helper function to format docs
def format_docs(docs):
    return "\n".join(doc.page_content for doc in docs)

format_docs_runnable = RunnableLambda(format_docs)

# Create the RAG chain once
rag_chain = (
    {"context": retriever | format_docs_runnable, "question": RunnablePassthrough()}
    | prompt_template
    | llm
    | StrOutputParser()
)


def run_rag_query(user_query: str) -> str:
    try:
        answer = rag_chain.invoke(user_query)
        response = {
            "prompt": user_query,
            "answer": answer,
            "status": "success"
        }
    except Exception as e:
        response = {
            "prompt": user_query,
            "error": str(e),
            "status": "error"
        }

    return json.dumps(response, indent=3)


