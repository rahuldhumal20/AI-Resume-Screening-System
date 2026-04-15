from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate.from_template("""
Extract:

1. Skills
2. Tools
3. Experience (in years)

IMPORTANT:
- Internship counts as experience
- Projects count as partial experience
- If not clearly mentioned, estimate reasonably

Resume:
{resume}

Return format:
Skills: []
Tools: []
Experience: X years
""")