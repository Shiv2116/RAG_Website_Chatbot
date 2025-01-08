import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_response(user_query):
    return "I'm sorry, I don't understand. Can you rephrase that?"

def get_vectorstore_from_url(url):
    ##Load the documents
    loader = WebBaseLoader(url)
    documents = loader.load()

    ##Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    documents_chunk = text_splitter.split_documents(documents)

    ##Vectorize the documents
    vector_store = Chroma.from_documents(documents_chunk,OpenAIEmbeddings())

    return vector_store

st.set_page_config(page_title="Chat with Website", page_icon="🧁")
st.title("Chat with Website")

if "chat_history" not in st.session_state: ## Initialize chat history- session state helps to persist data between reruns , so that we can keep track of the chat history
    st.session_state.chat_history = [
    AIMessage(content="Hello! How can I help you today?"),  
]

##Side-bar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:  
    documents = get_vectorstore_from_url(website_url)
    with st.sidebar:
        st.write(documents)

    user_query = st.chat_input("Type a message...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
        
    ##Conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)


