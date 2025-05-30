import streamlit as st
from resume_parser import extract_text_from_pdf
from job_matcher import compute_similarity, extract_keywords

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0f172a;
        font-family: 'Segoe UI', sans-serif;
        color: #e2e8f0;
    }
    .main-title {
        font-size: 42px;
        color: #38bdf8;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 8px #000;
    }
    .section-title {
        font-size: 24px;
        margin-top: 20px;
        color: #e2e8f0;
        font-weight: 600;
    }
    .highlight-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        min-height: 60px;
        color: #f8fafc;
    }
    .footer-text {
        text-align: center;
        font-weight: bold;
        margin-top: 40px;
        font-size: 18px;
        color: #60a5fa;
        text-shadow: 1px 1px 4px #000;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>AI Resume Analyzer and Job Matcher</div>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Upload and Input")
    uploaded_resume = st.file_uploader("Upload Your PDF Resume", type=["pdf"])
    job_description = st.text_area("Paste the Job Description")

if uploaded_resume and job_description:
    with st.spinner("Analyzing resume and job description..."):
        resume_text = extract_text_from_pdf(uploaded_resume)
        score = compute_similarity(resume_text, job_description)

        resume_keywords = extract_keywords(resume_text, 10)
        job_keywords = extract_keywords(job_description, 10)

        resume_keywords_display = ", ".join(resume_keywords) if resume_keywords else "No keywords extracted"
        job_keywords_display = ", ".join(job_keywords) if job_keywords else "No keywords extracted"

        missing_keywords = [word for word in job_keywords if word not in resume_keywords] if resume_keywords and job_keywords else []

    st.markdown("<div class='section-title'>Match Score</div>", unsafe_allow_html=True)
    st.metric(label="Resume Match Score", value=f"{score}%")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='section-title'>Resume Keywords</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='highlight-box'>{resume_keywords_display}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='section-title'>Job Description Keywords</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='highlight-box'>{job_keywords_display}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Missing Keywords</div>", unsafe_allow_html=True)
    if missing_keywords:
        st.markdown("<div class='highlight-box' style='color: #f87171;'>" + ", ".join(missing_keywords) + "</div>", unsafe_allow_html=True)
    else:
        st.success("Your resume includes all key terms from the job description.")

    st.markdown("<div class='footer-text'>Crafted with ❤️ by <span style='text-shadow:2px 2px 6px #000; font-size:22px;'>Anurag Singh</span></div>", unsafe_allow_html=True)

else:
    st.info("Please upload your resume and paste a job description to begin analysis.")
