# AI Resume Screening System

## Project Overview

The AI Resume Screening System is a web application developed using Python and Streamlit. It compares a candidate's resume with a job description using Natural Language Processing (NLP) techniques and provides a recommendation based on skill matching and similarity score.

---

## Features

- Upload Resume (PDF)
- Upload Job Description (TXT)
- Automatic Candidate Name Extraction
- Extract Matched Skills
- Identify Missing Skills
- Calculate AI Similarity Score
- Display Skill Match Percentage
- Generate Candidate Recommendation
- User-Friendly Web Interface

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- PyMuPDF
- TF-IDF Vectorizer
- Cosine Similarity
- Pandas
- Sentence Transformers (Library Installed)

---

## Project Structure

```
Resume_AI_Web_App/
│
├── app.py
├── requirements.txt
├── README.md
├── job_description.txt
└── sample_resume.pdf
```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Input

### Resume

- PDF File

### Job Description

- TXT File

---

## Output

The application displays:

- Candidate Name
- Matched Skills
- Missing Skills
- AI Similarity Score
- Skill Match Percentage
- Recommendation

---

## Recommendation Criteria

- Skill Match ≥ 80% → Suitable Candidate
- Skill Match ≥ 50% → Moderately Suitable
- Skill Match < 50% → Not Suitable

---

## Future Enhancements

- Multiple Resume Screening
- Automatic Email Extraction
- Automatic Phone Number Extraction
- Resume Ranking
- Database Integration
- Login and Registration
- ATS Score Improvement

---

## Author

**Kavibala I**