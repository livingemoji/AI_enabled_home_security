import smtplib
import requests
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from config import (
    SMTP_SERVER,
    SMTP_PORT,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    RECEIVER_EMAIL,
    PUSH_URL
)

def send_email_notification(subject, body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(attachment_path)}"
                )
                msg.attach(part)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        if attachment_path and os.path.exists(attachment_path):
            os.remove(attachment_path)

        print("[EMAIL] Sent")

    except Exception as e:
        print("[EMAIL ERROR]", e)

def send_push_notification(message):
    try:
        requests.post(PUSH_URL, data=message.encode("utf-8"))
        print("[PUSH] Sent")
    except Exception as e:
        print("[PUSH ERROR]", e)
