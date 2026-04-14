from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama3-70b-8192",  # best model on Groq
    temperature=0
)

response = llm.invoke("Explain AI in one line")
print(response.content)