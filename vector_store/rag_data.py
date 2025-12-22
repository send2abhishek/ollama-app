import warnings
import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore


embeddings = OllamaEmbeddings(model='nomic-embed-text')

db_name = "vajra"
vector_store = FAISS.load_local(db_name,embeddings=embeddings,allow_dangerous_deserialization=True)

question = "what is vajra akeyless ?"
docs = vector_store.search(query=question,k=1,search_type="similarity")
print(docs)