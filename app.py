import streamlit as st
from openai import OpenAI

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
                print("hello")
                
                # get the text from the pdfs
                
                # get the text chunks from the pdfs
                
                # create vector store
        
        
            
        
    

# to test app.py 
if __name__ == '__main__':
    main()