AI-Powered Resume Screening System

An AI-based Resume Screening Web Application developed using Python, Streamlit, and Natural Language Processing (NLP). The application compares a candidate's resume with a job description, identifies matching and missing skills, calculates similarity scores, and provides a hiring recommendation.

Project Overview

This project automates the initial resume screening process by analyzing a candidate's resume against a given job description.

It uses:
- TF-IDF Vectorizer
- Cosine Similarity
- Skill Matching
- Candidate Name Extraction

 Features

 Upload Resume (PDF)
- Upload Job Description (TXT)
- Paste Job Description
- Automatic Candidate Name Extraction
- Matched Skills Detection
- Missing Skills Detection
- AI Similarity Score
- Skill Match Percentage
- Recommendation Generation
- Final Result Summary

 Technologies Used

- Python
- Streamlit
- PyMuPDF
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Regular Expressions (re)

Project Structure

Resume_AI_Web_App/
│
├── app.py
├── requirements.txt
├── README.md
├── job_description.txt

Installation

Clone the repository
bash
git clone https://github.com/kavibala29/AI-Resume-Screening-System.git

Go to the project folder
bash
cd AI-Resume-Screening-System

Install dependencies
bash
pip install -r requirements.txt

Run the application
bash
streamlit run app.py

Application Workflow

1. Upload Resume (PDF)
2. Upload or Paste Job Description
3. Extract Resume Text
4. Extract Required Skills
5. Calculate AI Similarity Score
6. Identify Matched & Missing Skills
7. Generate Recommendation
8. Display Final Result

Output

The application displays:

- Candidate Name
- Matched Skills
- Missing Skills
- AI Similarity Score
- Skill Match Percentage
- Recommendation
- Final Result

 Future Enhancements

- Support DOCX Resume
- Bulk Resume Screening
- Export Results to Excel/PDF
- Semantic Matching using Sentence Transformers
- ATS Score Prediction

 Developed By

 Kavibala I

