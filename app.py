import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import get_missing_skills
from utils.suggestions import resume_suggestions
from utils.charts import skills_chart


# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-based analysis.")

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📂 Upload Resume (PDF)",
    type=["pdf"]
)

# ---------------- MAIN APP ---------------- #

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully!")

    # Extract Resume Text
    text = extract_text_from_pdf(uploaded_file)

    # Extract Skills
    skills = extract_skills(text)

    # ATS Score
    ats_score = calculate_ats_score(skills)

    # Job Selection
    st.subheader("💼 Select Your Target Job")

    job_role = st.selectbox(
        "Choose Target Job",
        (
            "Data Scientist",
            "AI Engineer",
            "Data Analyst"
        )
    )

    # Missing Skills
    missing_skills = get_missing_skills(job_role, skills)

    # Suggestions
    suggestions = resume_suggestions(ats_score)

    # ---------------- SHOW RESUME ---------------- #

    st.subheader("📄 Resume Content")

    st.text_area(
        "Extracted Text",
        text,
        height=300
    )

    # ---------------- SHOW SKILLS ---------------- #

    st.subheader("🎯 Skills Found")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.error("No skills found.")

    # ---------------- ATS SCORE ---------------- #

    st.subheader("📊 ATS Resume Score")

    st.progress(ats_score / 100)

    st.metric(
        label="ATS Score",
        value=f"{ats_score}/100"
    )

    if ats_score >= 80:
        st.success("🌟 Excellent Resume")

    elif ats_score >= 60:
        st.warning("👍 Good Resume")

    else:
        st.error("⚠ Resume Needs Improvement")

    # ---------------- MISSING SKILLS ---------------- #

    st.subheader("❌ Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.warning(skill)
    else:
        st.success("🎉 No Missing Skills")

    st.subheader("📈 Skills Dashboard")

    fig = skills_chart(skills, missing_skills)

    st.plotly_chart(fig) 
    # ---------------- SUGGESTIONS ---------------- #

    st.subheader("💡 Resume Suggestions")

    if suggestions:
        for tip in suggestions:
            st.info(tip)
    else:
        st.success("Excellent! No Suggestions Required.")