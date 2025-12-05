import smtplib
import ssl
from email.message import EmailMessage
import yaml

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def send_email(attachment_path):
    cfg = load_config()

    msg = EmailMessage()
    msg["Subject"] = cfg["email"]["subject"]
    msg["From"] = cfg["email"]["sender"]
    msg["To"] = cfg["email"]["recipient"]

    msg.set_content("Find the attached automated report.")

    with open(attachment_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="report.pdf"
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(cfg["email"]["sender"], cfg["email"]["password"])
        server.send_message(msg)