import os
import asyncio

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv


# setting loop
def awake_rag(query):
    try:
        asyncio.get_running_loop()
    except:
        asyncio.set_event_loop(asyncio.new_event_loop())
    load_dotenv()
    os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

    loader = PyPDFLoader(r"data\UNIT I DRMM.docx.pdf")
    document = loader.load()

    # splitting as character
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text = text_splitter.split_documents(document)

    # Embedding
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # store in vectordb
    vectorstore = Chroma.from_documents(text, embeddings)

    ## creaing a model 

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=vectorstore.as_retriever())

    # requesting model to output
    result = qa.invoke(query)

    return result['result']
