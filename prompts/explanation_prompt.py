from langchain_core.prompts import PromptTemplate

explanation_prompt = PromptTemplate.from_template("""
You are an AI hiring assistant.

Explain the candidate evaluation in detail.

Include:
- Strengths
- Weaknesses
- Final Recommendation (Hire / Reject / Consider)

Rules:
- Be clear and structured
- Do NOT assume anything
- Use given data only

Candidate Profile:
{candidate}

Matching Result:
{matching}

Score:
{score}

Output format:
Strengths:
Weaknesses:
Recommendation:
""")