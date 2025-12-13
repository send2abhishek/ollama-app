from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)
from langchain_core.messages import  HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)

def get_session_history(session_id):
    engine: Engine = create_engine("sqlite:///chat_history.db")
    return SQLChatMessageHistory(session_id, connection=engine)


user_id='send2abhishek'


template = ChatPromptTemplate.from_template("{prompt}")

chain = template | llm | StrOutputParser()
runnable_with_history = RunnableWithMessageHistory(chain,get_session_history)
about = "Hi, I am Abhishek Kumar a software Engineer works in walmart."
output = runnable_with_history.invoke([HumanMessage(content=about)],config={'configurable':{'session_id':user_id}})

print(output)

output_new = runnable_with_history.invoke([HumanMessage(content="whats my profession")],config={'configurable':{'session_id':user_id}})

print("new output below")
print(output_new)

# history = get_session_history(user_id)
# print(history.get_messages())
#
#
#
#
#
# output = chain.invoke({'prompt': about})
# print(output)
#
# output = chain.invoke({'prompt': "what is my name?"})
# print(output)