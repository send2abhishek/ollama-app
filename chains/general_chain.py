from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import (SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate)

llm = ChatOllama(
    model="llama3.1:latest",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)

prompt = ''' Given the user review below, classify it as either being about `Positive` or `Negative`.
Do not respond with more than one word.

Review: {review}
Classification: '''

template = ChatPromptTemplate.from_template(prompt)
chain = template | llm | StrOutputParser()

# review = "Thank you so much for providing such a great plateform for learning. I am really happy with the service. "
review = "I am not happy with you! "

output = chain.invoke({'review': review})
print(output)

positive_prompt = """
                You are expert in writing reply for positive reviews.
                You need to encourage the user to share their experience on social media.
                Review: {review}
                Answer:"""

positive_template = ChatPromptTemplate.from_template(positive_prompt)
positive_chain = positive_template | llm | StrOutputParser()

negative_prompt = """
                You are expert in writing reply for negative reviews.
                You need first to apologize for the inconvenience caused to the user.
                You need to encourage the user to share their concern on following Email:'send2abhishek@live.com'.
                Review: {review}
                Answer:"""


negative_template = ChatPromptTemplate.from_template(negative_prompt)
negative_chain = negative_template | llm | StrOutputParser()




def rout(info):
    if 'positive' in info['sentiment'].lower():
        return positive_chain
    else:
        return negative_chain


full_chain = {"sentiment": chain, 'review': lambda x: x['review']} | RunnableLambda(rout)

output = full_chain.invoke({'review': review})

print(output)


