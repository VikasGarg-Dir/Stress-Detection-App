import streamlit as st
import os
from pathlib import Path

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Define the template for the chatbot responses
template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

# Fix the path - use proper path handling
pdfs_directory = Path("Tabs/pdfs")
# Create directory if it doesn't exist
pdfs_directory.mkdir(parents=True, exist_ok=True)

# Initialize embeddings and vector store
embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")
vector_store = InMemoryVectorStore(embeddings)

# Initialize LLM
model = OllamaLLM(model="deepseek-r1:1.5b")

def upload_pdf(file):
    """Save uploaded file to the pdfs directory"""
    file_path = pdfs_directory / file.name
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

def load_pdf(file_path):
    """Load PDF file and extract documents"""
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

def split_text(documents):
    """Split documents into smaller chunks for processing"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)

def index_docs(documents):
    """Add documents to the vector store"""
    vector_store.add_documents(documents)

def retrieve_docs(query):
    """Retrieve relevant documents based on query"""
    return vector_store.similarity_search(query)

def answer_question(question, documents):
    """Generate answer based on question and retrieved documents"""
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return chain.invoke({"question": question, "context": context})

def main():
    st.title("PDF Question Answering Bot")
    st.write("Upload a PDF and ask questions about its content.")
    
    # Session state to track if a file has been processed
    if 'file_processed' not in st.session_state:
        st.session_state.file_processed = False
    
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type="pdf",
        accept_multiple_files=False
    )

    if uploaded_file and not st.session_state.file_processed:
        with st.spinner("Processing PDF..."):
            file_path = upload_pdf(uploaded_file)
            documents = load_pdf(file_path)
            chunked_documents = split_text(documents)
            index_docs(chunked_documents)
            st.session_state.file_processed = True
            st.success(f"Processed {uploaded_file.name} successfully!")

    # Display chat interface only after processing a file
    if st.session_state.file_processed:
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Get user question
        question = st.chat_input("Ask a question about the PDF...")

        if question:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": question})
            
            # Display user message
            with st.chat_message("user"):
                st.write(question)
            
            # Generate and display assistant response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    related_documents = retrieve_docs(question)
                    answer = answer_question(question, related_documents)
                    st.write(answer)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})

# if __name__ == "__main__":
#     main()