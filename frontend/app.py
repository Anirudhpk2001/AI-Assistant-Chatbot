import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.title("📚 AI Assistant (Frontend)")


uploaded_file = st.file_uploader("Upload PDF/Excel", type=["pdf", "xlsx"])

if st.button("Upload File"):
    if uploaded_file:
        files = {'file': uploaded_file.getvalue()}
        endpoint = "/api/upload_pdf" if uploaded_file.name.endswith(".pdf") else "/api/upload_excel"
        response = requests.post(BACKEND_URL + endpoint, files={'file': (uploaded_file.name, uploaded_file.getvalue())})
        st.success(response.json()["message"])


url = st.text_input("Feed Website URL")
if st.button("Feed URL"):
    res = requests.post(BACKEND_URL + "/api/url_embeddings", json={"url": url})
    st.success(res.json()["message"])


user_input = st.text_input("Ask a question")
if st.button("Ask"):
    res = requests.get(BACKEND_URL + "/api/chat", json={"prompt": user_input})
    st.text_area("AI Response", res.json()["answer"])
