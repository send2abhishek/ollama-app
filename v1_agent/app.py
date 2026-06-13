from langchain_ollama import ChatOllama
from langchain.agents import create_agent
import tools



system_prompt = """You are a helpful AI assistant. 
Use the available tools when needed to answer questions accurately.
If you need to search for information, use the web_search tool.
Always provide clear and concise answers.
"""


# result = tools.web_search.invoke({"query": "python programming","num_results": 1})
# print(result)


model = ChatOllama(
    model="llama3.1:latest"
)

agent = create_agent(model=model,tools=[tools.web_search],system_prompt=system_prompt)

result = agent.invoke({"messages": "what is the top global news right now ? "})



print(result['messages'][-1].content)

