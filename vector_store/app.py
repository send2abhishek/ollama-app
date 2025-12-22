import warnings
import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

warnings.filterwarnings('ignore')


loader = PyMuPDFLoader("./doc/onbord.pdf")



doc = loader.load()
context = doc[0].page_content

# print(context)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=1000)
chunks = text_splitter.split_documents(doc)

# print(chunks)


# this has chunk size of 8192 which is quite large
embeddings = OllamaEmbeddings(model='nomic-embed-text')

vector = embeddings.embed_query("hello world")
# print(len(vector))

index = faiss.IndexFlatL2(len(vector))

vector_store = FAISS(embedding_function=embeddings,index=index,docstore=InMemoryDocstore(),index_to_docstore_id={})
ids = vector_store.add_documents(chunks)
#
# print(len(ids),vector_store.index.ntotal)
# print(vector_store.index.ntotal)

vector_store.save_local("vajra")


question = "what is vajra akeyless ?"
docs = vector_store.search(query=question,k=1,search_type="similarity")
print(docs)

