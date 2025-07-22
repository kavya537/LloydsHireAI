import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(candidate_email, candidate_name, job_title):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = candidate_email
    msg['Subject'] = f"Job Application Update for {job_title}"

    body = f"Dear {candidate_name},\n\nThank you for applying for the position of {job_title}. We appreciate your interest in joining our team.\n\nBest regards,\nHR Team"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent to {candidate_name} at {candidate_email}")
    except Exception as e:
        print(f"Failed to send email to {candidate_name}: {e}")