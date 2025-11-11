# generate_substack_post.py
from scraper import get_reddit_digest
from datetime import datetime
import os

digest = get_reddit_digest()
subject = f"Reddit Digest — {datetime.now().strftime('%b %d')}"

# Save as .md file (Substack loves Markdown)
with open("substack_post.md", "w", encoding="utf-8") as f:
    f.write(f"# {subject}\n\n")
    f.write(digest.replace("↳ ", "→ ").replace("**", "*"))
    f.write("\n\n---\n")
    f.write("*Unsubscribe anytime. Made with ❤️ by your Reddit bot.*")

print("Substack post saved as substack_post.md")