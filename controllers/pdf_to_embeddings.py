from fastapi import FastAPI, UploadFile, File
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

import os
import shutil
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")



def pdf_to_Embedded(file):
    temp_path = f"temp_{file.filename}"
        
    # Save the uploaded PDF
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load and split the document
    loader = PyPDFLoader(temp_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)
    embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)
    persist_dir = "my_vector_db"

    # Create or update vector store
    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=embedding_model,
        persist_directory=persist_dir
    )
    vectorstore.persist()

    # Clean up temp file
    os.remove(temp_path)

    return {"status": "success", "message": f"{file.filename} has been processed and stored in vector DB."}