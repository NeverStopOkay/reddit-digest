# main.py — Test the full flow
from scraper import get_reddit_digest
from send_email import send_digest_via_mailgun
from datetime import datetime
import os  # ← ADD THIS LINE

if __name__ == "__main__":
    digest = get_reddit_digest()
    subject = f"Reddit Digest — {datetime.now().strftime('%b %d')}"
    test_email = os.getenv("TEST_EMAIL", "dbaneverstop@proton.me")

    print("\n" + "="*50)
    print("PREVIEW:")
    print("="*50)
    print(digest)
    print("="*50 + "\n")

    send_digest_via_mailgun(subject, digest, test_email)