# filepath: src/ui_app.py
import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Base, Candidate, JobDescription
from src.database.models import Base, Candidate, JobDescription

# Database setup
engine = create_engine('sqlite:///hr_ai.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

st.title("HR AI Recruitment Dashboard")

# HR uploads job description
st.header("Upload Job Description")
jd_title = st.text_input("Job Title")
jd_file = st.file_uploader("Upload Job Description PDF", type=["pdf"])
if st.button("Save Job Description") and jd_file and jd_title:
    jd_text = jd_file.read().decode(errors="ignore")
    jd = JobDescription(title=jd_title, description_text=jd_text)
    session.add(jd)
    session.commit()
    st.success("Job Description Saved!")

# Candidate uploads resume
st.header("Candidate Application")
name = st.text_input("Name")
email = st.text_input("Email")
resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
if st.button("Apply") and resume_file and name and email:
    resume_text = resume_file.read().decode(errors="ignore")
    candidate = Candidate(name=name, email=email, resume_text=resume_text)
    session.add(candidate)
    session.commit()
    st.success("Application Submitted!")

# Dashboard: List candidates and job descriptions
st.header("Dashboard")
candidates = session.query(Candidate).all()
job_descriptions = session.query(JobDescription).all()
st.write("Candidates:", candidates)
st.write("Job Descriptions:", job_descriptions)