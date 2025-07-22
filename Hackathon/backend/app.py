from flask import Flask, render_template, request, redirect
from config import db
from matcher import match_resumes
from emailer import send_email

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dashboard():
    requirement = db['requirements'].find_one(sort=[('_id', -1)])
    resumes = list(db['resumes'].find())
    ranked = match_resumes(requirement['text'], resumes) if requirement else []
    return render_template("index.html", candidates=ranked)

@app.route('/upload', methods=['POST'])
def upload():
    req_text = request.form['requirement']
    db['requirements'].insert_one({'text': req_text})
    return redirect('/')

@app.route('/send-email', methods=['POST'])
def send_mail():
    emails = request.form.getlist('selected_emails')
    for email in emails:
        send_email(email, "Interview Update", "<p>You are shortlisted!</p>")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
