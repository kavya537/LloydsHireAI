import re
from PyPDF2 import PdfReader, errors
import os

def extract_text_from_pdf(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return ""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except errors.PdfReadError as e:
        print(f"❌ PDF read error for {file_path}: {e}")
        return ""

def extract_info(text):
    email = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    name = re.findall(r'Name[:\- ]+([A-Za-z ]+)', text)
    skills = re.findall(r'Skills[:\- ]+([A-Za-z, ]+)', text)
    experience = re.findall(r'(\d+)\s+years', text)
    return {
        "name": name[0].strip() if name else "Unknown",
        "email": email[0] if email else "Unknown",
        "skills": skills[0].strip() if skills else "Unknown",
        "experience": experience[0] if experience else "Unknown",
        "text": text
    }