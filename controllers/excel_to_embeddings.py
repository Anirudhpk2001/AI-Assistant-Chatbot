import pandas as pd
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import shutil
import os

from dotenv import load_dotenv
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")


def excel_to_embeddings(file, persist_dir="my_vector_db", collection_name="my_collection"):
    temp_path = f"temp_{file.filename}"

 
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

  
    df = pd.read_excel(temp_path)

   
    docs = []
    for index, row in df.iterrows():
        row_text = " ".join([str(cell) for cell in row if pd.notnull(cell)])
        docs.append(Document(page_content=row_text))

    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = text_splitter.split_documents(docs)

    
    embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)

    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=persist_dir,
        embedding_function=embedding_model
    )

    vectorstore.add_documents(split_docs)
    vectorstore.persist()

    os.remove(temp_path)

    return {"status": "success", "message": f"{file.filename} processed and added to the vector store."}
