from langchain_community.document_loaders import PyMuPDFLoader
# import tiktoken

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)



loader = PyMuPDFLoader("./doc/onbord.pdf")

doc = loader.load()
context = doc[0].page_content

# print(doc[0].page_content)

# encoding = tiktoken.encoding_for_model("gpt-4o-mini")
#
# enc = encoding.encode("congratulations")
# print(enc)



system = SystemMessagePromptTemplate.from_template("You are helpful AI assistant who answer user question based on the provided context. Do no answer in more than {words} words")
prompt = """Answer user question based on the provided context ONLY! If you do not know the answer, just say "I don't know".
            ### Context:
            {context}

            ### Question:
            {question}

            ### Answer:"""

prompt = HumanMessagePromptTemplate.from_template(prompt)

messages = [system, prompt]
template = ChatPromptTemplate(messages)



qna_chain = template | llm | StrOutputParser()

response = qna_chain.invoke({'context': context, 'question': "what is vajra ?", 'words': 50})

print(response)



