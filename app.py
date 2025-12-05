from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,PromptTemplate,ChatPromptTemplate)

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
    # other params ...
)

# messages = [
#             SystemMessage(content="You are a helpful geography assistant! Your name is Lina."),
#             HumanMessage(content="Why sky is cloudy? what did it denotes? "),
#         ]


system = SystemMessagePromptTemplate.from_template('You are helpful {stream} assistant! Your name is {name}. ')
question = HumanMessagePromptTemplate.from_template('Why sky is cloudy? what did it denotes in {points} points')
#
system.format(stream='geography', name='Laura')
question.format(points=3)

template = ChatPromptTemplate([system, question])
questionAns = template.invoke({'stream': 'geography', 'name': 'Laura', 'points': 5})

print(llm.invoke(questionAns).content)