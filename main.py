import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pypdf import PdfReader

from chains.extraction_chain import get_extraction_chain
from chains.matching_chain import get_matching_chain
from chains.scoring_chain import get_scoring_chain
from chains.explanation_chain import get_explanation_chain

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text

def calculate_score(extracted, match_result):
    import json
    import re

    try:
        cleaned = match_result.strip()

        if "```" in cleaned:
            cleaned = cleaned.split("```")[1]
            if cleaned.startswith("json"):
                cleaned = cleaned.replace("json", "").strip()

        data = json.loads(cleaned)

        matched_count = len(data.get("matched_skills", []))
        missing_count = len(data.get("missing_skills", []))

    except:
        matched_count = 0
        missing_count = 0

    # Skill score (max 60)
    if matched_count + missing_count > 0:
        skill_score = (matched_count / (matched_count + missing_count)) * 60
    else:
        skill_score = 30

    # Experience score (max 30 now instead of 40)
    exp_match = re.search(r'(\d+(\.\d+)?)\s*years', extracted.lower())
    experience = float(exp_match.group(1)) if exp_match else 1

    if experience >= 3:
        exp_score = 30
    elif experience >= 2:
        exp_score = 25
    elif experience >= 1:
        exp_score = 20
    else:
        exp_score = 15

    # 🔥 NEW: Penalty for low experience
    penalty = 0
    if experience < 2:
        penalty = 5

    total_score = int(skill_score + exp_score - penalty)

    # 🔥 Cap score (VERY IMPORTANT)
    if total_score > 95:
        total_score = 95

    return total_score

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    seed = 42
)

# Chains
extraction_chain = get_extraction_chain(llm)
matching_chain = get_matching_chain(llm)
scoring_chain = get_scoring_chain(llm)
explanation_chain = get_explanation_chain(llm)


# Job Description
job_description = """
Hiring Full Stack Developer.

Skills Required:
- JavaScript
- React.js
- Node.js, Express.js
- REST APIs
- MongoDB
- JWT Authentication

Experience:
- 1–3 years

Good to have:
- FastAPI / Python
- Deployment (Netlify, Render)
"""
folder_path = "resumes"

resume_files = [
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.endswith(".pdf")
]

results = []

for file_path in resume_files:

    # Extract file name
    file_name = os.path.basename(file_path)

    # Load PDF
    resume = load_pdf(file_path)

    extracted = extraction_chain.invoke({"resume": resume})

    match_result = matching_chain.invoke({
        "candidate": extracted,
        "job_description": job_description
    })

    score = calculate_score(extracted, match_result)

    explanation = explanation_chain.invoke({
        "candidate": extracted,
        "matching": match_result,
        "score": f"Score: {score}"
    })

    
    # Classification
    if score >= 80:
        category = "STRONG"
    elif score >= 50:
        category = "AVERAGE"
    else:
        category = "WEAK"

    results.append({
        "file_name": file_name,
        "score": score,
        "category": category,
        "explanation": explanation
    })

for res in results:
    print("\n============================")
    print(f"Resume: {res['file_name']}")
    print(f"Score: {res['score']}")
    print(f"Category: {res['category']}")

    print("\n--- Explanation ---")
    print(res['explanation'])