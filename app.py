from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
    # other params ...
)

print(llm.invoke("What is machine learning").content)