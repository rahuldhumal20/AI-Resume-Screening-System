from langchain_core.output_parsers import StrOutputParser
from prompts.explanation_prompt import explanation_prompt

def get_explanation_chain(llm):
    return explanation_prompt | llm | StrOutputParser()