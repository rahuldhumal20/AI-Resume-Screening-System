# 🚀 AI Resume Screening System (GenAI + LangChain)

## 📌 Overview
This project is an **AI-powered Resume Screening System** that evaluates candidates based on a given job description.

It simulates a **real-world recruiter pipeline** by:
- Extracting skills and experience from resumes (PDF)
- Matching candidate profiles with job requirements
- Assigning a **score (0–100)**
- Providing **explainable hiring decisions**

---

## 🎯 Key Objectives
- Build a complete **LLM-powered evaluation pipeline**
- Implement **skill extraction + matching + scoring**
- Ensure **explainability in AI decisions**
- Enable **LangSmith tracing for debugging**

---

## ⚙️ Tech Stack
- **Python**
- **LangChain (LCEL)**
- **Groq API (LLaMA 3.3)**
- **LangSmith (Tracing & Monitoring)**
- **PyPDF (PDF Processing)**

---

## 🔄 Pipeline Architecture

PDF Resume → Text Extraction → Skill Extraction → Matching → Scoring → Explanation


---

## 🧠 Features

### ✅ Resume Processing
- Reads resumes directly from **PDF files**
- Supports multiple candidates dynamically

### ✅ Skill Extraction
- Extracts:
  - Skills
  - Tools
  - Experience

### ✅ Intelligent Matching
- Compares resume with job description
- Identifies:
  - Matched skills
  - Missing skills

### ✅ Hybrid Scoring System
- Combines:
  - AI-based understanding
  - Rule-based scoring logic
- Factors:
  - Skill match ratio
  - Experience level
- Produces **realistic scores (0–100)**

### ✅ Explainable AI
- Provides:
  - Strengths
  - Weaknesses
  - Final Recommendation (Hire / Consider / Reject)

### ✅ Automatic Classification
- Strong → Score ≥ 80  
- Average → Score 50–79  
- Weak → Score < 50  

### ✅ LangSmith Tracing (Mandatory)
- Tracks full pipeline:
  - Extraction
  - Matching
  - Scoring
  - Explanation

---

## 📊 Sample Output

============================
Resume: Rahul Resume.pdf
Score: 88
Category: STRONG

--- Explanation ---

Strengths:

Strong MERN stack skills
Good API development experience

Weaknesses:

Slightly lower experience (1–2 years)

Recommendation:
Hire


---

## 🚀 How to Run

### 1️⃣ Clone Repository

git clone <your-repo-link>
cd resume-screening-ai

### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Setup Environment Variables

Create .env file:

GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=resume-screening

### 5️⃣ Add Resumes

Place PDF files inside:

resumes/

### 6️⃣ Run Project
python main.py

---

📈 Evaluation Logic
Factor	    | Weight
Skill Match	|60%
Experience	|30%
Penalties	|Applied for gaps

---

### 💡 Key Highlights
No hardcoded outputs ❌
Fully dynamic evaluation ✅
Real-world recruiter simulation ✅
Structured and modular design ✅

---


### 🔍 LangSmith Tracing
Enables debugging of each pipeline step
Shows:
Input → Output flow
Model behavior
Error tracking

---

### 🚀 Future Improvements
Streamlit UI (Resume upload)
Candidate ranking system
JSON structured outputs
Multi-job comparison
ATS-style scoring system

---


### 👨‍💻 Author

Rahul Dhumal

---