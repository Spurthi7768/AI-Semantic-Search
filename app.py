import streamlit as st
import openai
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
st.title("📄 AI Semantic Search 💻")

if 'secret' not in st.session_state:
    st.session_state.secret=st.secrets['apikey']

user_secret=st.text_input(label=":black[OpenAI API Key]",placeholder="Paste your OpenAI API Key" ,type='password')

if user_secret:
    openai.api_key=user_secret
    st.session_state.secret=user_secret

@st.cache_data
def load_data():
    reader = PdfReader('data/living planet report.pdf')
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text
    text_splitter = CharacterTextSplitter(        
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)
    return texts

data=load_data()


def search_article(data,search_term):
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(data, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = docsearch.similarity_search(search_term)
    ans=chain.run(input_documents=docs, question=search_term)
    return ans




search_term=st.text_input(label=":blue[Search your Query]",placeholder="Please, search the article with...")

search_button=st.button(label="Run",type="primary")

if search_term:
    if search_button:
        answer=search_article(data,search_term)

        st.write(answer)