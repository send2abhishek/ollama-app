from langchain_ollama import ChatOllama
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)



system = SystemMessagePromptTemplate.from_template('You are helpful {stream} assistant! Your name is {name}. ')
question = HumanMessagePromptTemplate.from_template('Why sky is cloudy? what did it denotes in {points} points')

messages = [system, question]

templates = ChatPromptTemplate(messages)

chain = templates | llm

res = chain.invoke({'stream': 'geography', 'name': 'Laura', 'points': 5})

print(res.content)

