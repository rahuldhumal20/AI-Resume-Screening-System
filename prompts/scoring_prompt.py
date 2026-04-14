from langchain_core.prompts import PromptTemplate

scoring_prompt = PromptTemplate.from_template("""
You are an AI recruiter scoring candidates.

Evaluate the candidate based on:
- Matched skills
- Missing skills
- Experience

Rules:
- Score must be between 0 to 100
- Be realistic and strict
- More missing skills → lower score
- More experience → higher score

Candidate Profile:
{candidate}

Matching Result:
{matching}

Output format:
Score: 
Reason:
""")