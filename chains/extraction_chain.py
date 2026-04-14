from langchain_core.output_parsers import StrOutputParser
from prompts.extraction_prompt import extraction_prompt

def get_extraction_chain(llm):
    return extraction_prompt | llm | StrOutputParser()