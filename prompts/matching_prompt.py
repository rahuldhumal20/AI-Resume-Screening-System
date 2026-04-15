from langchain_core.prompts import PromptTemplate

matching_prompt = PromptTemplate.from_template("""
You are an AI recruiter.

Compare candidate with job description.

Return ONLY valid JSON.
Do NOT add explanation.
Do NOT use markdown.

Format:
{{
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"]
}}

Candidate:
{candidate}

Job Description:
{job_description}
""")