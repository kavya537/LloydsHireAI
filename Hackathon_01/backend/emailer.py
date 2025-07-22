import smtplib
from email.message import EmailMessage

# CONFIGURATION — replace with your values
SENDER_EMAIL = 'kavyadodla08@gmail.com'         # <-- Replace this
APP_PASSWORD = 'qtvh rklg ksfo xvxz'       # <-- Replace with App Password

def send_email_to_list(recipients):
    subject = "Resume Shortlisted - Next Steps"
    body = """
Dear Candidate,

Congratulations! Your resume has been shortlisted for the next round.
We will reach out to you with further details.

Best regards,  
HR Team
    """

    success = []
    failed = []

    for recipient in recipients:
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient
            msg.set_content(body)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)

            print(f"✅ Email sent to: {recipient}")
            success.append(recipient)

        except Exception as e:
            print(f"❌ Failed to send to {recipient}: {str(e)}")
            failed.append((recipient, str(e)))

    return success, failed
