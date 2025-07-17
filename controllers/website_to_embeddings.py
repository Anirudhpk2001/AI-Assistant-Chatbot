
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings  
from langchain_community.vectorstores import Chroma
import json

load_dotenv()
user_agent = os.getenv("USER_AGENT")
openai_key = os.getenv("OPENAI_API_KEY")  



def website_to_vector(url):
    url_str = str(url) 

    loader = WebBaseLoader(
        web_paths=[url_str],
        header_template={"User-Agent": user_agent}
    )

    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)
    embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)
    persist_dir = "my_vector_db"

    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=embedding_model,
        persist_directory=persist_dir
    )

    vectorstore.persist()

    result = {"status": "successfully added to the vector store"}
    return json.dumps(result, indent=3)


