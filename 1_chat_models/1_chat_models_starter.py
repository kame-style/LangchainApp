from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# Explicitly provide the API key
llm = ChatOpenAI(model="gpt-4o")
result = llm.invoke("What is the capital of Haryana?")
print(result.content)