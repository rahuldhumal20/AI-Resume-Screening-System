from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate.from_template("""
You are an AI resume analyzer.

Extract the following from the resume:

1. Skills
2. Tools
3. Experience (in years)

Rules:
- Do NOT assume anything
- Only extract from given text

Resume:
{resume}

Output format:
Skills: []
Tools: []
Experience: 
""")