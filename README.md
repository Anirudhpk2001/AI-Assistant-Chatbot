# AI-Assistant-Chatbot

This AI Assistant runs on a Retrieval-Augmented Generation (RAG) pipeline that can process multiple input formats, including PDFs, Excel files, and websites.

You can interact with the system by asking any question related to the content of the provided sources, and it will generate accurate, context-aware answers by searching through the relevant documents.

### Educational Use Case:
This tool is especially valuable in teaching environments, where educators can limit the assistant's knowledge base to specific chapters or topics. For example, students can interact with the chatbot to learn concepts related to a specific lesson, without being distracted by unrelated information from the broader internet.

### How It Works:
The project uses LangChain to orchestrate a pipeline of tasks, such as document loading, text splitting, embedding generation, and retrieval.
* All document embeddings are stored in ChromaDB, a lightweight and efficient vector database.
* When a user sends a prompt from the frontend, the backend:
* Converts the query into embeddings.
* Searches the ChromaDB for the most relevant document chunks.
* Combines the results with the original prompt.
* Sends the combined context to an LLM (like OpenAI GPT or similar) to generate an answer.

### Key Features:
Multi-modal Input Support: PDF, Excel, Websites

**Custom Knowledge Limitation**: Control the chatbot’s knowledge to focus on specific chapters or topics

**Context-Aware Q&A**: Retrieves document-specific answers using embeddings

**Efficient Storage & Retrieval**: Powered by ChromaDB and LangChain


To run this project please follow the following steps 

## Step 1 :
Create a virtual environment using the following code :

`python -m venv .venv`

`.venv/Scripts/activate`

## Step 2 :
Install all the requirements 

`pip install -r requirements.txt`

## Step 3:
Create .env file with Open_ai api as shown in .env.example file

## Step 4:
run the backend 

`fastapi dev main.py`

## Step 5:
In another terminal 

`cd frontend`
`streamlit run app.py`

