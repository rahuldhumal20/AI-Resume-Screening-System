from langchain_core.output_parsers import StrOutputParser
from prompts.scoring_prompt import scoring_prompt

def get_scoring_chain(llm):
    return scoring_prompt | llm | StrOutputParser()