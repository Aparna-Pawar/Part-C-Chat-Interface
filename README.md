Q&A chatbot with flow mode and RAG mode 
- Integrates both Flow Mode and RAG Mode into a single Streamlit app.
- Users can switch modes easily from the interface.
- Demonstrates modular chatbot design (reuse of flow and RAG code).

## Tools & Libraries You Used

- Python 3 – Core programming language.
- Streamlit – For building and deploying the interactive chatbot apps.
- LangChain – For building the RAG pipeline and handling document retrieval.
- Groq API – Used as the LLM backend (instead of OpenAI).
- dotenv – For loading API keys securely from a .env file.
- FAISS – Vector database for storing and retrieving embeddings.
- PyPDF2/PDF loader – For document loading in RAG mode.

## 📂 Folder Structure
- app.py - Main RAG pipeline code.
- requirements.txt - Python dependencies.
- .env - Stores the secret keys like GROQ_API_KEY, LANGCHAIN_API_KEY (Create your own Groq API key and Langchain API key for running app.py)

## Setup Instructions

1. Clone the repo:
bash
git clone https://github.com/Aparna-Pawar/Part-C-Chat-Interface.git
cd Part-C-Chat-Interface

2. Create and activate a virtual environment:
- python3 -m venv venv
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. If your version requires API keys for any service, create a .env file and add your own API keys:
- YOUR_API_KEY_NAME=your_api_key_here 
  (e.g. GROQ_API_KEY="your_api_key")

Run Streamlit Locally 
streamlit run app.py

⚠️ Limitationsz;
- Requires users to provide their own API keys (Groq API Key).
- Model answers depend on retrieval quality + Groq model output, so incorrect or incomplete answers are possible if documents are not well structured. So please use the documents which are provided in a repo.
- Currently supports only PDF documents

Access Online using Streamlit Cloud (You can directy access the app using the below link just by adding your own groq and langchain API keys)
https://usklkgr7pyp4zxgfju8sfp.streamlit.app/


