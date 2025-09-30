import streamlit as st
import flow_chatbot
import rag_app

st.set_page_config(page_title="Q&A Chatbot", layout="centered")
st.title("Flow Mode & RAG Mode Q&A")

# Sidebar mode switch
mode = st.sidebar.radio("Choose Mode:", ["Flow Mode", "RAG Mode"])

if mode == "Flow Mode":
    flow_chatbot.flow_ui()
else:
    rag_app.rag_ui()