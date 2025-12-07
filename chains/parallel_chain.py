from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)

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


# response = fact_chain.invoke({'stream': 'geography', 'name': 'Laura', 'points': 2})
# print(response)


 # poem chain

question = HumanMessagePromptTemplate.from_template('Write poem on {topic} in {points} points')

messages = [system, question]

templates = ChatPromptTemplate(messages)


poem_chain = templates | llm | StrOutputParser()

#
# response = poem_chain.invoke({'stream': 'geography', 'name': 'Laura','topic':'sky', 'points': 5})
# print(response)

final_chain = RunnableParallel(fact = fact_chain, poem = poem_chain)

output= final_chain.invoke({'stream': 'geography', 'name': 'Laura','topic':'sky', 'points': 5})

print(output)


