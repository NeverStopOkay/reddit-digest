# scraper.py — Core Reddit scraping logic
import httpx
from bs4 import BeautifulSoup
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_digest() -> str:
    """Scrape top 5 posts from old.reddit.com and return formatted email body."""
    headers = {
        "User-Agent": "RedditDigestBot/1.0 (by /u/yourusername)"
    }
    try:
        with httpx.Client(timeout=10.0) as client:
            resp = client.get("https://old.reddit.com/", headers=headers)
            resp.raise_for_status()
    except Exception as e:
        return f"Error scraping Reddit: {e}"

    soup = BeautifulSoup(resp.text, 'html.parser')
    posts = soup.find_all('div', class_='thing')[:5]

    lines = [f"Reddit Digest — {datetime.now().strftime('%B %d, %Y')}\n"]
    lines.append("Your 2-minute cure for FOMO:\n")

    for i, post in enumerate(posts, 1):
        try:
            title = post.find('a', class_='title').text.strip()
            permalink = post['data-permalink']
            comments = post.find('a', string=lambda t: t and 'comment' in t.lower())
            comments_text = comments.text if comments else "0 comments"
            url = f"https://reddit.com{permalink}"
            lines.append(f"{i}. **{title}**")
            lines.append(f"   ↳ [{comments_text}]({url})\n")
        except:
            continue  # Skip malformed posts

    lines.append("—\nSent with ❤️ by your Reddit Digest bot.")
    return "\n".join(lines)