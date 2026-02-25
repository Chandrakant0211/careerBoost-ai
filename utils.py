# utils.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process
from db import ROLE_SKILLS, ALL_SKILLS


# -----------------------------
# 1️⃣ Role Detection
# -----------------------------
def detect_role(jd_text):
    roles = ROLE_SKILLS.keys()
    match, score, _ = process.extractOne(jd_text.lower(), roles)
    if score > 60:
        return match
    return None


# -----------------------------
# 2️⃣ Skill Extraction
# -----------------------------
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in ALL_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# -----------------------------
# 3️⃣ Auto Required Skills
# -----------------------------
def get_required_skills(job_description):
    role = detect_role(job_description)

    if role:
        return ROLE_SKILLS[role], role
    else:
        return extract_skills(job_description), None


# -----------------------------
# 4️⃣ Match Score (ML Based)
# -----------------------------
def calculate_match_score(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(similarity * 100, 2)


# -----------------------------
# 5️⃣ ATS Score Logic
# -----------------------------
def calculate_ats_score(resume_skills, required_skills):
    if not required_skills:
        return 50

    match_count = len(set(resume_skills) & set(required_skills))
    ats_score = (match_count / len(required_skills)) * 100
    return round(ats_score, 2)


# -----------------------------
# 6️⃣ Skill Gap Analysis
# -----------------------------
def get_skill_gap(resume_skills, required_skills):
    return list(set(required_skills) - set(resume_skills))