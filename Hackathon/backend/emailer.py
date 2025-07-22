import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    sender = "you@example.com"
    password = "your-password"
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, to_email, msg.as_string())
