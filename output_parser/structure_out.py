from langchain_ollama import ChatOllama
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import (SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate,
                                    PromptTemplate)

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
    rating: str = Field(description="The rating of the joke is from 1 to 10")
    temperature: float = Field(description="The temperature of the joke")



structured_llm = llm.with_structured_output(Joke)

output = structured_llm.invoke('Tell me a joke about the cat')
print(output)