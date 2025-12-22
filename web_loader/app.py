from langchain_community.document_loaders import WebBaseLoader
import re

from scripts import ask_llm

urls = ['https://economictimes.indiatimes.com/markets/stocks/news',
        'https://www.livemint.com/latest-news',
        'https://www.livemint.com/latest-news/page-2'
        'https://www.livemint.com/latest-news/page-3',
        'https://www.moneycontrol.com/']

loader = WebBaseLoader(web_paths=urls)

docs = []

for doc in loader.load():
    docs.append(doc)

#
# print(docs)

def format_docs(docs):
    return "\n\n".join([x.page_content for x in docs])


context = format_docs(docs)
#
# print(context)


def text_clean(text):
    text = re.sub(r'\n\n+','\n\n',text)
    text = re.sub(r'\t','\t',text)
    text = re.sub(r'\s',' ',text)
    return text

context = text_clean(context)
# print(context)

# response = ask_llm(context[:10_000],"provide stock market news")
# print(response)


def chunk_text(text,chunk_size,overlap=100):
    chunks = []
    for i in range(1, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks

chunks2 = chunk_text(context,10_000)

question = " Extract stock market news from the given text."

chunk_summary = []
for chunk in chunks2:
    response = ask_llm(chunk,question)
    chunk_summary.append(response)


print(chunk_summary)
# print(chunks2)
#
# async def load_doc_in_asyn(loaderData):
#     docs = []
#     async for doc in loaderData.alazy_load():
#         docs.append(doc)
#     return docs
#
#
# async def get_data(loader):
#     fetched_data = await load_doc_in_asyn(loader)
#     print(fetched_data)
#
# print(get_data(loader))
