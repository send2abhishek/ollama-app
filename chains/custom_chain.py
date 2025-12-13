from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)
from langchain_core.runnables import chain

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)

system = SystemMessagePromptTemplate.from_template('You are helpful {stream} assistant! Your name is {name}. ')
question = HumanMessagePromptTemplate.from_template('Why sky is cloudy? what did it denotes? explain in {points} points')

messages = [system, question]

templates = ChatPromptTemplate(messages)

fact_chain = templates | llm | StrOutputParser()


question = HumanMessagePromptTemplate.from_template('Write poem on {topic} in {points} points')

messages = [system, question]

templates = ChatPromptTemplate(messages)


poem_chain = templates | llm | StrOutputParser()

@chain
def custom_chain(params):
    return {
        'fact': fact_chain.invoke(params),
        'poem': poem_chain.invoke(params),
    }


params = {'stream': 'geography', 'name': 'Laura','topic':'sky', 'points': 5}
output  = custom_chain.invoke(params)
print(output['fact'])
print("poem output is below")
print(output['poem'])


