import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Loop through all the pdfs, loop through all the pages, extract the text and return it as a string
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs: 
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", # split by new line
        chunk_size=1000, # split into chunks of 1000 characters
        chunk_overlap=200, # overlap chunks by 200 characters
        length_function=len 
    )
    chunks = text_splitter.split_text(text) # split the text into chunks
    return chunks

def get_vectorstore(text_chunks, openai_api_key):
    embeddings = OpenAIEmbeddings(api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    return vectorstore


def main():
    st.set_page_config(page_title='Go chat with pdfs', page_icon=':shark:')
    
    st.header("Chat with pdfs :shark:")
    question = st.text_input("Ask any question about your documents")
    
    with st.sidebar:
        OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        if not OPENAI_API_KEY:
            st.warning("Please add your OpenAI API key to continue.")
        
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing your documents"): 
                # get the text from the pdfs
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text) # run this to test if the text is being extracted correctly
                
                # get the text chunks from the pdfs
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)
                
                # create vector store
                vectorstore = get_vectorstore(text_chunks, OPENAI_API_KEY)
        
        
            
        
    

# to test app.py 
if __name__ == '__main__':
    main()