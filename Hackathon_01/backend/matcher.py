import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def extract_skills(text):
    keywords = ["python", "java", "sql", "mongodb", "flask", "django", "aws", "azure", "git", "docker", "rest", "api"]
    return [kw for kw in keywords if re.search(rf'\b{kw}\b', text, re.IGNORECASE)]

def calculate_score(required_skills, candidate_skills):
    matched = set(required_skills) & set(candidate_skills)
    return len(matched) / len(required_skills) * 100 if required_skills else 0
