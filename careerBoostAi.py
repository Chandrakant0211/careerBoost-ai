# careerboostai.py

import streamlit as st
from utils import (
    extract_skills,
    get_required_skills,
    calculate_match_score,
    calculate_ats_score,
    get_skill_gap
)

st.set_page_config(page_title="CareerBoost AI", layout="centered")

st.title("🚀 CareerBoost AI - Advanced Resume Analyzer")

# Text Areas
resume_text = st.text_area("📄 Paste Resume Text")
job_description = st.text_area("💼 Paste Job Description")

if st.button("Analyze Resume"):

    if resume_text and job_description:

        required_skills, detected_role = get_required_skills(job_description)

        resume_skills = extract_skills(resume_text)

        match_score = calculate_match_score(resume_text, job_description)

        ats_score = calculate_ats_score(resume_skills, required_skills)

        missing_skills = get_skill_gap(resume_skills, required_skills)

        st.subheader("📊 Analysis Results")

        if detected_role:
            st.success(f"🎯 Detected Role: {detected_role.title()}")

        st.metric("Match Score (%)", match_score)
        st.metric("ATS Score (%)", ats_score)

        st.subheader("✅ Detected Skills")
        if resume_skills:
            st.write(", ".join(resume_skills))
        else:
            st.write("No skills detected")

        st.subheader("❌ Missing Skills")
        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.write("No major skill gaps found!")

        st.subheader("💡 Improvement Suggestions")
        if missing_skills:
            st.warning("Add the following skills to improve match:")
            st.write(", ".join(missing_skills))
        else:
            st.success("Great! Resume aligns well with the job description.")

    else:
        st.error("Please paste both Resume and Job Description.")