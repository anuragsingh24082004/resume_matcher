AI Resume Analyzer and Job Matcher:- 

AI Resume Analyzer and Job Matcher is a smart web application built using Streamlit that compares a candidate's resume with a job description. It extracts relevant keywords, calculates a similarity score, and identifies missing skills or terms to help improve the chances of job selection.

Features
Upload PDF resume

Paste job description text

Extract top keywords from both

Calculate and display resume match score

Identify missing keywords

Clean, modern, and responsive user interface

Tech Stack
Python

Streamlit

Scikit-learn (NLP and keyword extraction)

PyPDF2 (PDF parsing)

Cosine Similarity for score calculation

Folder Structure
Copy
Edit
project-root/
│
├── app.py
├── resume_parser.py
├── job_matcher.py
├── requirements.txt
├── README.md
How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/anuragsingh24082004/ai-resume-matcher.git
cd ai-resume-matcher
Create virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Run the app

arduino
Copy
Edit
streamlit run app.py
How It Works
Upload your resume in PDF format

Paste the job description in the input area

The app processes both inputs using NLP

It extracts keywords and computes a similarity score

It displays matched, unmatched, and missing keywords

You get real-time insights to optimize your resume

Deployment
This app can be deployed easily on platforms like:

Streamlit Cloud

Render

Hugging Face Spaces

Heroku (with slight config changes)

Author
Created by Anurag Singh
