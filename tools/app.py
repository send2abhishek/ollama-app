from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_core.messages import HumanMessage


load_dotenv()

llm = ChatOllama(
    model="llama3.1:latest"
)

@tool
def add(a,b):
    """
    Add two integer numbers together

    Args:
    a: First integer
    b: Second integer
    """
    return a + b

@tool
def multiply(a,b):
    """
    multiply two integer numbers together

    Args:
    a: First integer
    b: Second integer
    """
    return a * b



# print(add.invoke({'a':1,'b':2}))

# tools = [add, multiply]
#
# llm_with_tools = llm.bind_tools(tools)

#
# search = DuckDuckGoSearchRun()
#
# result = search.invoke("Obama's first name?")
# print(result)


# search = TavilySearchResults(
#     max_results=5,
#     search_depth="advanced",
#     include_answer=True,
#     include_raw_content=True,
# )

# question = "what is today's stock market news?"
# print(search.invoke(question))


# @tool
# def duckduckgo_search(query):
#     """
#     Search DuckDuckGo for news articles or general query
#
#     Args:
#     query: search query
#     :return:
#     """
#
#     return search.invoke(query)

# print(llm_with_tools)

# print(llm_with_tools.invoke("find 1 plus 2"))


@tool
def wikipedia_search(query):
    """
    Search wikipedia for general information.

    Args:
    query: The search query
    """

    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    response = wikipedia.invoke(query)
    return response


@tool
def pubmed_search(query):
    """
    Search pubmed for medical and life sciences queries.

    Args:
    query: The search query
    """

    search = PubmedQueryRun()
    response = search.invoke(query)
    return response


@tool
def tavily_search(query):
    """
    Search the web for realtime and latest information.
    for examples, news, stock market, weather updates etc.

    Args:
    query: The search query
    """

    search = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
    )
    response = search.invoke(query)
    return response

tools = [wikipedia_search, pubmed_search, tavily_search, multiply]

list_of_tools = { tool.name: tool for tool in tools }
# print(list_of_tools)

llm_with_tools = llm.bind_tools(tools)

# print(llm_with_tools.invoke("how to treat lung cancer").tool_calls)
query = "provide stock market news"

messages = [HumanMessage(query)]

ai_msg = llm_with_tools.invoke(messages)

messages.append(ai_msg)
# print(msg)


for tool_call in ai_msg.tool_calls:
    print(tool_call)

    name = tool_call['name'].lower()
    selected_tool= list_of_tools[name]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)


response = llm_with_tools.invoke(messages)

print(response.content)