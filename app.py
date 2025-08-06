import streamlit as st
from rag import awake_rag
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(page_title="Disaster Management RAG", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        background: linear-gradient(to right, #ff5e62, #ff9966);
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 25px;
        font-size: 28px;
        font-weight: bold;
    }
    .answer-box {
        border: 2px solid #00aaff;
        padding: 20px;
        border-radius: 12px;
        background-color: #f0faff;
        margin-top: 20px;
        font-size: 17px;
        color: #1f1f1f;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    .info-section {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #dcdcdc;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin-top: 20px;
        line-height: 1.7;
    }
    .query-card {
        background-color: #fdfdfd;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-top: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Know About Disaster Management:<br>RAG Model</div>', unsafe_allow_html=True)

# Navigation menu
page_select = option_menu(
    None,
    ['Home', 'Info'],
    icons=['house', 'info-circle'],
    menu_icon='cast',
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {
            "background-color": "#ff5e62",
            "color": "white",
            "font-weight": "bold",
        }
    }
)

# Home Page: Query
if page_select == "Home":
    st.markdown("""
    ## 📘 Disaster Management Information System

    Welcome to the **RAG-powered Q&A system**.  
    Upload a document and ask any question related to **Disaster Risk Management (DRM)** —  
    powered by **LangChain**, **Gemini**, and **Chroma Vector Store**.

    ---
    """)

    query = st.text_input("💬 What is your query?")
    st.markdown('</div>', unsafe_allow_html=True)

    if query:
        with st.spinner("🤔 Thinking..."):
            result = awake_rag(query)
        st.markdown(f"""
        <div class="answer-box">
            <b>📘 Answer:</b><br>{result}
        </div>
        """, unsafe_allow_html=True)

# Info Page
elif page_select == "Info":
    st.markdown('<div class="info-section">', unsafe_allow_html=True)
    st.markdown("""
    ## 🛰️ Project Title:
    ### **Disaster Management Information System using RAG (Retrieval-Augmented Generation)**

    ---

    ### 📌 Objective:
    Build an interactive system that retrieves accurate, context-aware information related to **Disaster Risk Management (DRM)** using a smart **RAG model**.

    ---

    ### 🧠 Key Features:
    - 📄 Load & analyze disaster-related documents
    - 🔗 Integration with **LangChain** and **Gemini LLM**
    - 📦 Store embeddings in **Chroma Vector Store**
    - 🔍 Intelligent semantic search
    - 💬 Natural language interface with **Streamlit**
    - ⚙️ Automatic context-based answer generation

    ---

    ### 🛠️ Tech Stack:
    - **Python**
    - **Streamlit**
    - **LangChain**
    - **Gemini LLM** (Google GenAI)
    - **Chroma Vector DB**
    - **dotenv** for secure key management

    ---

    ### ⚙️ How It Works:
    1. Load disaster-related PDFs
    2. Split and embed text with Gemini
    3. Store in Chroma Vector Store
    4. Retrieve relevant chunks on query
    5. Generate answer with Gemini LLM

    ---

    ### 🎯 Use Case:
    Help **students**, **researchers**, and **disaster response teams** instantly find relevant content from large DRM documents — without manually searching.

    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
