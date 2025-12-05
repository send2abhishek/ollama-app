from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
    # other params ...
)

messages = [
            SystemMessage(content="You are a helpful geography assistant! Your name is Lina."),
            HumanMessage(content="Why sky is cloudy? what did it denotes? "),
        ]

answer = llm.invoke(messages)

print(answer.content)
