# AI-Assistant-Chatbot

This Ai Assistant thats run on a RAG pipeline that takes any form of input be it pdf , excel or and websites
you can ask system with any question regarding the content of those particular files , This can be very helpful for teaching kids where you can limit the chatbot to certain knowledge help them learn 
concepts particularly related to that chapter

This project makes use of Langchain to create a pipline of tasks , and also make use of chromaDB to store all the vector embeddings , then from theses embeddings the prompt that is sent from the frontend to the backend using 


To run this project please follow the following steps 

## Step 1 :
Create a virtual environment using the following code :

`python -m venv .venv`

`.venv/Scripts/activate`

## Step 2 :
Install all the requirements 

`pip install -r requirements.txt`

## Step 3:
Create .env file with Open_ai api

## Step 4:
run the backend 

`fastapi dev main.py`

## Step 5:
In another terminal 

`cd frontend`
`streamlit run app.py`

