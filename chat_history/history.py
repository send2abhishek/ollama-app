from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate,MessagesPlaceholder)
from langchain_core.messages import  HumanMessage,SystemMessage
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

#
#
# template = ChatPromptTemplate.from_template("{prompt}")
#
# chain = template | llm | StrOutputParser()
# runnable_with_history = RunnableWithMessageHistory(chain,get_session_history)
about = "Hi, I am Abhishek Kumar a software Engineer works in walmart."
# output = runnable_with_history.invoke([HumanMessage(content=about)],config={'configurable':{'session_id':user_id}})
#
# print(output)
#
# output_new = runnable_with_history.invoke([HumanMessage(content="whats my profession")],config={'configurable':{'session_id':user_id}})
#
# print("new output below")
# print(output_new)

system = SystemMessagePromptTemplate.from_template("You are helpful assistance.")
human = HumanMessagePromptTemplate.from_template("{input}")
message = [system,MessagesPlaceholder(variable_name='history'), human]

prompt = ChatPromptTemplate(messages=message)
chain = prompt | llm | StrOutputParser()
runnable_with_history = RunnableWithMessageHistory(chain,get_session_history,
                                                   input_messages_key='input',
                                                   history_messages_key='history')


def cha_with_llm(session_id,input):
    return runnable_with_history.invoke({'input': input},config={'configurable':{'session_id':session_id}})


output = cha_with_llm(user_id,about)
print(output)

output = cha_with_llm(user_id,"whats my name ?")
print(output)

