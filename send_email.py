# send_email.py — Send via Mailgun (or print for testing)
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_digest_via_mailgun(subject: str, body: str, to_email: str):
    api_key = os.getenv("MAILGUN_API_KEY")
    domain = os.getenv("MAILGUN_DOMAIN")
    from_email = os.getenv("FROM_EMAIL")

    if not all([api_key, domain, from_email]):
        print("MAILGUN NOT CONFIGURED — printing email:")
        print(f"To: {to_email}\nSubject: {subject}\n\n{body}")
        return

    url = f"https://api.mailgun.net/v3/{domain}/messages"
    data = {
        "from": from_email,
        "to": [to_email],
        "subject": subject,
        "text": body,
        "html": f"<pre>{body}</pre>"  # Keeps formatting
    }

    response = requests.post(url, auth=("api", api_key), data=data)
    if response.status_code == 200:
        print(f"Email sent to {to_email}")
    else:
        print(f"Failed: {response.text}")