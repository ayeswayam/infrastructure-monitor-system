import os
import requests
def send_slack(message, webhook_url=None):
    webhook = webhook_url or os.getenv('SLACK_WEBHOOK')
    if not webhook:
        return False
    payload = {'text': message}
    requests.post(webhook, json=payload)
    return True
def send_email(subject, body, to_email):
    import smtplib, os
    from email.message import EmailMessage
    smtp = os.getenv('SMTP_HOST')
    user = os.getenv('SMTP_USER')
    pwd = os.getenv('SMTP_PASS')
    if not smtp:
        return False
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to_email
    msg.set_content(body)
    with smtplib.SMTP(smtp, 587) as s:
        s.starttls()
        s.login(user, pwd)
        s.send_message(msg)
    return True
