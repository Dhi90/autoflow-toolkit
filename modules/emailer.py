import smtplib, ssl, yaml
from email.message import EmailMessage
import csv

def send_emails(config_path: str, contacts_csv: str):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)["email"]

    print("[INFO] Connecting to SMTP server...")
    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP(config["smtp_server"], config["port"]) as server:
            server.starttls(context=context)
            server.login(config["sender"], config["password"])
            print("[SUCCESS] Logged into email server.")

            with open(contacts_csv, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(f"[INFO] Sending email to: {row['email']}")
                    msg = EmailMessage()
                    msg['From'] = config["sender"]
                    msg['To'] = row["email"]
                    msg['Subject'] = config["subject"].replace("{{name}}", row["name"])
                    msg.set_content(config["body"].replace("{{name}}", row["name"]))
                    server.send_message(msg)
                    print(f"[SENT] Email sent to: {row['email']}")
    except Exception as e:
        print("[ERROR]", e)
