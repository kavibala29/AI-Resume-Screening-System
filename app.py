import streamlit as st
import fitz
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI-Powered Resume Screening System",
    page_icon="📄",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#1f77b4;'>
    AI-Powered Resume Screening System
    </h1>
    <h4 style='text-align:center;color:gray;'>
    AI Based Candidate Screening Application
    </h4>
    """,
    unsafe_allow_html=True
)

st.info(
    "Upload a Resume (PDF) and a Job Description (TXT), then click 'Analyze Resume' to evaluate the candidate."
)

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select",
    ["Home", "About Project", "Technologies"]
)

if menu == "About Project":
    st.header("About Project")
    st.write("""
This project compares a candidate's resume with a job description
using Natural Language Processing (TF-IDF and Cosine Similarity)
and provides a recommendation.
""")
    st.stop()

if menu == "Technologies":
    st.header("Technologies Used")
    st.write("""
- Python
- Streamlit
- PyMuPDF
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
""")
    st.stop()

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:

    st.subheader("Job Description")

    jd_option = st.radio(
        "Choose Input Method",
        ["Upload TXT File", "Paste Job Description"]
    )

    job_description = ""

    if jd_option == "Upload TXT File":

        job_file = st.file_uploader(
            "Upload Job Description",
            type=["txt"]
        )

        if job_file is not None:
            job_description = job_file.read().decode("utf-8")

    else:

        job_description = st.text_area(
            "Paste Job Description",
            height=200,
            placeholder="Paste the Job Description here..."
        )

st.markdown("")

analyze = st.button(
    "Analyze Resume",
    use_container_width=True
)

skills = [
    "Python",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Git",
    "GitHub",
    "VS Code",
    "Communication",
    "Problem Solving"
]

if analyze:

    if resume_file is None or job_description.strip() == "":
        st.error("Please upload both Resume and Job Description.")

    else:

        document = fitz.open(stream=resume_file.read(), filetype="pdf")

        resume_text = ""

        for page in document:
            resume_text += page.get_text()


        # Candidate Name Extraction

        candidate_name = "Unknown"

        lines = resume_text.split("\n")

        ignore = [
            "resume",
            "curriculum vitae",
            "cv",
            "profile",
            "summary",
            "objective",
            "email",
            "phone",
            "mobile",
            "linkedin",
            "github"
        ]

        for line in lines:

            line = line.strip()

            if len(line) < 3:
                continue

            if "@" in line:
                continue

            if re.search(r"\d", line):
                continue

            if any(word in line.lower() for word in ignore):
                continue

            if len(line.split()) <= 5:
                candidate_name = line
                break
        matched_skills = []

        for skill in skills:
            if skill.lower() in resume_text.lower() and skill.lower() in job_description.lower():
                matched_skills.append(skill)

        missing_skills = []

        for skill in skills:
            if skill.lower() not in resume_text.lower():
                missing_skills.append(skill)

        documents = [resume_text, job_description]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )

        score = similarity[0][0] * 100

        skill_match = (
            len(matched_skills) / len(skills)
        ) * 100

        st.markdown("---")

        st.subheader("Candidate Details")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Name", candidate_name)

        with col2:
            st.metric("Matched Skills", len(matched_skills))

        with col3:
            st.metric("Skill Match", f"{skill_match:.0f}%")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Matched Skills")

            for skill in matched_skills:
                st.success(skill)

        with col2:

            st.subheader("Missing Skills")

            for skill in missing_skills:
                st.error(skill)

        st.markdown("---")

        st.subheader("Similarity Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "AI Similarity Score",
                f"{score:.2f}%"
            )

        with col2:
            st.metric(
                "Skill Match",
                f"{skill_match:.2f}%"
            )

        st.progress(min(int(skill_match), 100))

        st.markdown("---")

        st.subheader("Recommendation")

        if skill_match >= 80:
            st.success("Suitable Candidate")

        elif skill_match >= 60:
            st.warning("Moderately Suitable")

        else:
            st.error("Not Suitable")
            st.markdown("---")

        st.subheader("Final Result")

        if skill_match >= 80:
            final_status = "Suitable Candidate"

        elif skill_match >= 50:
            final_status = "Moderately Suitable"

        else:
            final_status = "Not Suitable"

        st.success(f"""
        Candidate Name : {candidate_name}

        Similarity Score : {score:.2f}%

        Skill Match : {skill_match:.2f}%

        Recommendation : {final_status}
        """)
        
       
       
