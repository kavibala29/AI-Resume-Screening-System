# AI-Powered Resume Screening System

## Project Overview

The AI-Powered Resume Screening System is a web-based application developed using Python and Streamlit. It automates the resume screening process by comparing a candidate's resume with a Job Description using Natural Language Processing (NLP) techniques.

The application extracts text from PDF resumes, identifies matching and missing skills, calculates an AI Similarity Score using TF-IDF Vectorizer and Cosine Similarity, and generates a recommendation based on the candidate's skill match.

Additionally, the system automatically extracts the candidate's name from the uploaded resume, generates a structured screening report using Pandas, and allows users to download the report as a CSV file.

## Features

 Upload Resume (PDF)
 Upload Job Description (TXT)
 Paste Job Description directly
 Automatic Candidate Name Extraction
 Skill Matching
 Missing Skill Detection
 AI Similarity Score Calculation
 Candidate Recommendation
 Screening Report using Pandas
 Download Screening Report (CSV)

## Technologies Used
 python
 Streamlit
 PyMuPDF
 Pandas
 Scikit-learn
 TF-IDF Vectorizer
 Cosine Similarity
 Regular Expressions (Regex)

## Project Structure

Resume_AI_Web_App/
│
├── app.py
├── requirements.txt
├── README.md
├── job_description.txt

## Installation

Install the required libraries:

bash
pip install -r requirements.txt

## Run the Application

bash
py -m streamlit run app.py

or

bash
streamlit run app.py

## Working Process

1. Upload Resume (PDF)
2. Upload or Paste Job Description
3. Extract Resume Text using PyMuPDF
4. Extract Candidate Name
5. Compare Resume and Job Description
6. Calculate AI Similarity Score using TF-IDF and Cosine Similarity
7. Identify Matched Skills and Missing Skills
8. Generate Recommendation
9. Create Screening Report using Pandas
10. Download Screening Report as CSV

## Output

The application displays:

- Candidate Name
- Matched Skills
- Missing Skills
- AI Similarity Score
- Skill Match Percentage
- Recommendation
- Screening Report (Table)
- CSV Download Option

---

## Future Enhancements

- Support DOCX Resume
- Automatic Skill Extraction using NLP
- Multiple Resume Screening
- Resume Ranking
- Recruiter Login System
- Database Integration

## Developed By

**Kavibala**

