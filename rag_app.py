import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def create_vector_store(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=800, chunk_overlap=150)
    chunks = text_splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    return vectorstore

def create_qa_chain_with_memory(vectorstore):
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return qa_chain, memory

def rag_ui():
    st.subheader("📄 Document Q&A Chatbot (RAG)")

    uploaded_pdf = st.file_uploader("Upload your PDF", type="pdf")


    if uploaded_pdf and "qa_chain" not in st.session_state:
        with st.spinner("Processing PDF and generating knowledge base..."):
            pdf_text = extract_text_from_pdf(uploaded_pdf)
            vectorstore = create_vector_store(pdf_text)
            qa_chain, memory = create_qa_chain_with_memory(vectorstore)

            #Store in session state (cached)
            st.session_state.qa_chain = qa_chain
            st.session_state.memory = memory
            st.session_state.chat_history = []

        st.success("Document processed successfully!")

    # Only show Q&A if document is processed
    if "qa_chain" in st.session_state:
        user_question = st.text_input("Ask a question about your document:")

        if user_question:
            with st.spinner("Thinking..."):
                result = st.session_state.qa_chain.invoke({"question": user_question})
                answer = result["answer"]
                st.session_state.chat_history.append(("You", user_question))
                st.session_state.chat_history.append(("Bot", answer))
                st.write(answer)

        # Show chat history
        if st.session_state.chat_history:
            st.subheader("Chat History")
            for speaker, msg in st.session_state.chat_history:
                st.write(f"**{speaker}:** {msg}")

        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.session_state.memory.clear()
            st.success("Chat history cleared!")


    