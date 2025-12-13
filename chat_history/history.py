from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (ChatPromptTemplate)

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)



template = ChatPromptTemplate.from_template("{prompt}")

chain = template | llm | StrOutputParser()

about = "Hi, I am Abhishek Kumar a software Engineer works in walmart."

output = chain.invoke({'prompt': about})
print(output)