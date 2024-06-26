import streamlit as st
from langchain_helper import get_qa_chain,create_vector_db

st.title("Edu-Query System 📚")
btn = st.button("Create Knowledge Base")
if btn:
    pass

question = st.text_input("Enter your question here:")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Response")
    st.write(response["result"])