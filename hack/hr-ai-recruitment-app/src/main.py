import os
from flask import Flask, request, jsonify
from utils.file_upload import upload_file
from agent.ai_agent import AIAgent
from database.models import Candidate, JobDescription

app = Flask(__name__)
ai_agent = AIAgent()

@app.route('/upload_job_description', methods=['POST'])
def upload_job_description():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    job_desc_path = upload_file(file, 'job_descriptions')
    if job_desc_path:
        job_description = JobDescription(path=job_desc_path)
        ai_agent.process_job_description(job_description)
        return jsonify({"message": "Job description uploaded successfully"}), 200
    return jsonify({"error": "Failed to upload job description"}), 500

@app.route('/apply', methods=['POST'])
def apply():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file part"}), 400
    resume_file = request.files['resume']
    if resume_file.filename == '':
        return jsonify({"error": "No selected resume file"}), 400
    candidate_info = upload_file(resume_file, 'resumes')
    if candidate_info:
        candidate = Candidate(info=candidate_info)
        ai_agent.add_candidate(candidate)
        return jsonify({"message": "Resume submitted successfully"}), 200
    return jsonify({"error": "Failed to submit resume"}), 500

@app.route('/match_candidates', methods=['GET'])
def match_candidates():
    matched_candidates = ai_agent.match_candidates()
    return jsonify(matched_candidates), 200

if __name__ == "__main__":
    app.run(debug=True)