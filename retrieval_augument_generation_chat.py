# app.py
import os
import streamlit as st
from langchain.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Define the path to the vector store and API key
CHROMA_PATH = "chromadb"
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# Load the Chroma vector store with the embedding function
db_chroma = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
# Load the Chroma vector store with the embedding function

# Define the prompt template
PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}
Answer the question based on the above context: {question}.
Provide a detailed answer.
Don’t justify your answers.
Don’t give information not mentioned in the CONTEXT INFORMATION.
Do not say "according to the context" or "mentioned in the context" or similar.
"""

# Streamlit interface
st.title("Chat with the Document(RAG) : Attention is All You Need, Transformer")

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to display chat history
def display_chat():
    for message in st.session_state.messages:
        if message['is_user']:
            st.write(f"**You:** {message['text']}")
        else:
            st.write(f"**Chat Respone:** {message['text']}")

# Sidebar title
st.sidebar.title("Streamlit Chatbox")

# Display the chat history
display_chat()

# Create a form to handle user input and send button together
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="input_field")
    send_button = st.form_submit_button("Send")

# Handle form submission
if send_button and user_input:
    # Append user message to chat history
    st.session_state.messages.append({"text": user_input, "is_user": True})
    docs_chroma = db_chroma.similarity_search(user_input, k=5)
    context_text = "\n\n".join([doc.page_content for doc in docs_chroma])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=user_input)
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    response = model.invoke(prompt)

    # Simulate bot response (replace this with your chatbot logic)
    bot_response = f"The answer to query : {response.content}"

    # Append bot response to chat history
    st.session_state.messages.append({"text": bot_response, "is_user": False})
