import os
import pandas as pd
from resume_parser import extract_text_from_pdf, extract_info
from matcher import match_resumes

def process_resumes(job_desc_path, resume_folder):
    print("📄 Loading job description...")
    try:
        job_desc = extract_text_from_pdf(job_desc_path)
    except Exception as e:
        print(f"❌ PDF read error for {job_desc_path}: {e}")
        return
    print(f"Job description length: {len(job_desc)}")
    if not job_desc.strip():
        print("❌ Job description is empty. Please provide a valid PDF.")
        return

    print("📁 Scanning resumes...")
    resume_files = [os.path.join(resume_folder, f) for f in os.listdir(resume_folder) if f.endswith('.pdf')]
    print(f"Found {len(resume_files)} resume files.")
    resume_data = []
    for f in resume_files:
        try:
            text = extract_text_from_pdf(f)
        except Exception as e:
            print(f"❌ PDF read error for {f}: {e}")
            continue
        print(f"Resume {f} length: {len(text)}")
        if not text:
            continue
        info = extract_info(text)
        resume_data.append(info)

    if not resume_data:
        print("❌ No valid resumes found.")
        return

    matched = match_resumes(job_desc, resume_data)
    print(f"Matched candidates: {len(matched)}")

    df = pd.DataFrame(matched)[['name', 'email', 'skills', 'experience', 'match']]
    print("\n📊 Matched Candidates:")
    print(df.to_string(index=False))

    for candidate in matched[:5]:
        if candidate['email'] != "Unknown":
            print(f"📨 Would send email to: {candidate['name']} ({candidate['email']})")
            # Uncomment below to actually send emails
            # send_email(candidate['email'], candidate['name'])

if __name__ == "__main__":
    # Use absolute paths for clarity
    job_desc_path = r"C:\Users\kavya\Documents\manisha\resume-review-automation\job_description\job_description.pdf"
    resume_folder = r"C:\Users\kavya\Documents\manisha\resume-review-automation\resumes"
    process_resumes(job_desc_path, resume_folder)

    print("Script started")
    # ...existing code...
    print("Script finished")