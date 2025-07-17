from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Specify the same persist directory
persist_dir = "my_vector_db"

# Load the persisted vectorstore
embedding_model = OpenAIEmbeddings(openai_api_key=openai_key)

vectorstore = Chroma(
    persist_directory=persist_dir,
    embedding_function=embedding_model
)

# Inspect what's stored (e.g., list documents or perform a search)
print("Number of items in vectorstore:", vectorstore._collection.count())

# Example: perform a similarity search
query = "what is physics"
results = vectorstore.similarity_search(query, k=5)

for i, doc in enumerate(results):
    print(f"Result {i+1}: {doc.page_content}")
