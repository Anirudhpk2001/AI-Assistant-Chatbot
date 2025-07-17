from fastapi import FastAPI,UploadFile, File
from pydantic import BaseModel, HttpUrl
from controllers.website_to_embeddings import website_to_vector
import json
from controllers.chat_openai import run_rag_query
from controllers.pdf_to_embeddings import pdf_to_Embedded
from controllers.excel_to_embeddings import excel_to_embeddings

app = FastAPI()

class URLRequest(BaseModel):
    url: HttpUrl  

class promptRequest(BaseModel):
    prompt: str

class promptResponse(BaseModel):
    prompt: str
    answer: str
    status: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    return pdf_to_Embedded(file)


@app.post("/api/upload_excel")
async def upload_excel(file: UploadFile = File(...)):
    result = excel_to_embeddings(file)
    return result


@app.post("/api/url_embeddings")
def convert_to_vector_embeddings(request : URLRequest):
    url = request.url
    return website_to_vector(url)

@app.get("/api/chat",response_model=promptResponse)
def chat(request : promptRequest):
    result = run_rag_query(request.prompt)
    return json.loads(result)


