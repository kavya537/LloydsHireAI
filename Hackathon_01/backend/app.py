from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from emailer import send_email_to_list
from werkzeug.utils import secure_filename
from pymongo import MongoClient
import os
import webbrowser
import threading

# Import local helper modules
from resume_matcher_db import match_resumes, extract_resume_data
from utils import extract_text_from_pdf

# Setup
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['resume_db']
resumes_collection = db['resumes']


# ======================
# Home Page
# ======================
@app.route('/')
def home():
    return render_template('index.html', title="Lloyd's HIRE AI")


# ======================
# Matching Resumes
# ======================
@app.route('/result', methods=['POST'])
def result():
    requirement_text = request.form['requirement']
    db_choice = request.form['db_choice']

    resumes = []

    try:
        if db_choice == 'upload':
            uploaded_files = request.files.getlist("resumes")
            for file in uploaded_files:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                text = extract_text_from_pdf(filepath)
                data = extract_resume_data(text)
                data['resume_link'] = url_for('uploaded_file', filename=filename)
                resumes.append(data)

        elif db_choice == 'database':
            for r in resumes_collection.find():
                text = r.get('text', '')
                data = extract_resume_data(text)
                # Link fallback
                filename = os.path.basename(r.get('resume_link', ''))
                data['resume_link'] = url_for('uploaded_file', filename=filename)
                resumes.append(data)

        results = match_resumes(requirement_text, resumes)
        return render_template("result.html", results=results, title="Lloyd's HIRE AI")

    except Exception as e:
        print("Error:", str(e))
        return render_template("result.html", results=[], error="An error occurred. Please try again.", title="Lloyd's HIRE AI")

# ======================
# send emails
# ======================

@app.route('/send-emails', methods=['POST'])
def send_emails_route():
    selected_emails = request.form.getlist('selected_emails')

    if not selected_emails:
        return render_template("result.html", results=[], error="❌ No candidates selected.", title="Lloyd's HIRE AI")

    # ✅ Send real emails
    success, failed = send_email_to_list(selected_emails)

    message = ""
    if success:
        message += f"✅ Emails sent to: {', '.join(success)}<br>"
    if failed:
        message += f"❌ Failed to send to: {', '.join([f[0] for f in failed])}"

    return render_template("result.html", results=[], error=message, title="Lloyd's HIRE AI")

# ======================
# Serve Resume Files
# ======================
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# ======================
# Auto-launch browser
# ======================
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


# ======================
# Main App Runner
# ======================
if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)
