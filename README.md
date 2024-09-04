# Chat with the Document (RAG): Attention is All You Need, Transformer
This project provides an interactive interface to chat with documents using a Retrieval-Augmented Generation (RAG) approach. It uses the "Attention is All You Need" Transformer paper as a primary document, Chroma for vector storage, and OpenAI's language model for chat responses. The application is built using Streamlit to provide an easy-to-use chat interface.

# Project Structure

- augment_generation_chat.py: The main application file that sets up the Streamlit interface and handles the chat logic.
- retrieval_process_document.ipynb: A Jupyter Notebook responsible for loading, splitting, and creating embeddings from the document.
- Transformer.pdf: The primary document used for the chat context.
- chromadb: Directory where the Chroma vector store persists the document embeddings.

# Requirements

- Python 3.8 or higher
- Streamlit
- LangChain
- OpenAI's API key
- Chroma
- PyPDFLoader

# Installation

- Clone the repository:
```bash
git clone https://github.com/your-repository/project.git

cd project
```
- Install the required dependencies:
```bash
pip install streamlit langchain chromadb PyPDFLoader openai
```
- Set up your OpenAI API key: Export your API key to the environment variable:
```bash
export OPENAI_API_KEY='your_openai_api_key'
```
![Chat Interface Output](/chat_interface.png)

# Features
- Document Interaction: Chat with the content of the Transformer paper using a retrieval-augmented generation approach.
- Contextual Responses: The model generates responses based on specific document sections, ensuring answers are relevant.
- Streamlit Interface: Basic interface to type queries and see responses.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
