from langchain_ollama import ChatOllama
from typing import Optional
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate,PromptTemplate)

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)



class Joke(BaseModel):
    """Joke to tell user"""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
    rating: str = Field(description="The rating of the joke")


parser = PydanticOutputParser(pydantic_object=Joke)

instruction = parser.get_format_instructions()


prompt = PromptTemplate(
    template= """
    Answer the user query with a joke. Here is your formatting instruction.
    {format_instruction}
    
    Query: {query}
    Answer:""",
    input_variables=['query'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
)

chain = prompt | llm | parser

output = chain.invoke({'query': 'Tell me a joke about the dog.'})
print(output)



# system = SystemMessagePromptTemplate.from_template('You are helpful {stream} assistant! Your name is {name}. ')
# question = HumanMessagePromptTemplate.from_template('Why sky is cloudy? what did it denotes in {points} points')
#
# messages = [system, question]
#
# templates = ChatPromptTemplate(messages)
#
# analysis_prompt = ChatPromptTemplate.from_template(''' analyze the following text: {text} You need to tell me that how difficult it is to understand Answer in one sentence only ''')
#
#
#
#  # StrOutputParser will parse the output of llm into string
# chain = templates | llm | StrOutputParser()
#
# composed_chain = {"text": chain} | analysis_prompt | llm | StrOutputParser()
#
# response = composed_chain.invoke({'stream': 'geography', 'name': 'Laura', 'points': 5})
# print(response)
