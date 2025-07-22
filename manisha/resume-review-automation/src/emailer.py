import smtplib
from email.mime.text import MIMEText

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