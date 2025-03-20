from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
    
# Print to debug
print(f"API key found: {api_key[:5]}...")

# Explicitly provide the API key
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
result = llm.invoke("What is the capital of Haryana?")
print(result)