import os
import re
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader

# 📥 Load PDF Text
def extract_text_from_pdf(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return ""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# 🧠 Extract Candidate Info
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

# 🔍 Match Resumes to Job Description
def match_resumes(job_desc, resume_texts):
    corpus = [job_desc] + [r['text'] for r in resume_texts]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    for i, score in enumerate(scores):
        resume_texts[i]['match'] = round(score * 100, 2)
    return sorted(resume_texts, key=lambda x: x['match'], reverse=True)

# 📧 Send Email (Optional)
def send_email(to_email, candidate_name):
    msg = MIMEText(f"Dear {candidate_name},\n\nYou are shortlisted for an interview. Please confirm your availability.\n\nRegards,\nHR Team")
    msg['Subject'] = "Interview Invitation"
    msg['From'] = "hr@example.com"
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login("hr@example.com", "your_password")
            server.send_message(msg)
        print(f"✅ Email sent to {candidate_name} ({to_email})")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

# 🚀 Main Workflow
def process_resumes(job_desc_path, resume_folder):
    print("📄 Loading job description...")
    job_desc = extract_text_from_pdf(job_desc_path)

    print("📁 Scanning resumes...")
    resume_files = [os.path.join(resume_folder, f) for f in os.listdir(resume_folder) if f.endswith('.pdf')]
    print(f"🔍 Found {len(resume_files)} resumes.")

    resume_data = []
    for f in resume_files:
        text = extract_text_from_pdf(f)
        if not text:
            print(f"⚠️ No text found in {f}")
            continue
        info = extract_info(text)
        resume_data.append(info)

    print("🧠 Matching resumes to job description...")
    matched = match_resumes(job_desc, resume_data)

    df = pd.DataFrame(matched)[['name', 'email', 'skills', 'experience', 'match']]
    print("\n📊 Matched Candidates:")
    print(df.to_string(index=False))

    # 💌 Optional: Send emails to top 5 matches
    for candidate in matched[:5]:
        if candidate['email'] != "Unknown":
            print(f"📨 Would send email to: {candidate['name']} ({candidate['email']})")
            # Uncomment below to actually send emails
            # send_email(candidate['email'], candidate['name'])

# 🧪 Run the script
if __name__ == "__main__":
    process_resumes("job_description/job_description.pdf", "C:/Users/kavya/Documents/HR_Recruitment/resumes")
