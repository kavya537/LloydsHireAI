from flask import Flask, render_template
from database.models import Candidate, JobDescription
from ml.matcher import match_candidates

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    job_descriptions = JobDescription.query.all()
    candidates = Candidate.query.all()
    
    match_results = []
    for job in job_descriptions:
        matched_candidates = match_candidates(job.description, candidates)
        match_results.append({
            'job_title': job.title,
            'matched_candidates': matched_candidates
        })

    return render_template('dashboard.html', match_results=match_results)

if __name__ == '__main__':
    app.run(debug=True)