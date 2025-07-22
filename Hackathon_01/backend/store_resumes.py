from pymongo import MongoClient
import fitz
import os
from matcher import extract_skills

client = MongoClient("mongodb://localhost:27017")
db = client["resumedb"]
collection = db["resumes"]

resume_dir = "./resumes"

for filename in os.listdir(resume_dir):
    if filename.endswith(".pdf"):
        path = os.path.join(resume_dir, filename)
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        skills = extract_skills(text)

        collection.insert_one({
            "name": filename,
            "text": text,
            "skills": skills,
            "email": "test@example.com",
            "phone": "1234567890",
            "resume_link": None
        })
        print(f"Inserted {filename} into database.")
