from langchain_groq import ChatGroq
from dotenv import load_dotenv
from chains.extraction_chain import get_extraction_chain

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

chain = get_extraction_chain(llm)

resume = """
John Doe
Skills: Python, Machine Learning, SQL
Worked 3 years as Data Analyst
Used tools: Pandas, NumPy
"""

result = chain.invoke({"resume": resume})

print(result)