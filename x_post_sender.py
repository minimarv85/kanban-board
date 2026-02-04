#!/usr/bin/env python3
"""
X Post Sender - Sends posts to Telegram for manual posting
Runs via cron: 8am, 12pm, 6pm
"""

import requests
import re
import sys
from datetime import datetime

# Configuration
BOT_TOKEN = "8518810123:AAGxv0k99Jvo76JxediAOur1g1XWJ7SD0aI"
CHAT_ID = "6397615458"
POSTS_FILE = "/home/skillman85/.openclaw/workspace/daily_posts.md"
LOG_FILE = "/home/skillman85/.openclaw/workspace/x_delivery.log"

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, "a") as f:
        f.write(formatted + "\n")

def get_next_post():
    if not POSTS_FILE:
        return None
    try:
        with open(POSTS_FILE, "r") as f:
            content = f.read()
        
        # Find posts section
        match = re.search(r'=== DAILY POSTS FOR.+?===\n(.+?)\n=== Research Sources ===', content, re.DOTALL)
        if match:
            posts_section = match.group(1)
            
            # Split by --- and clean up
            posts = []
            for post in posts_section.split('---'):
                post = post.strip()
                # Remove the POST header line if present
                post = re.sub(r'^\*\*📱 POST \d+.*?\*\*\s*\n?', '', post).strip()
                post = re.sub(r'^\*\*☕ POST \d+.*?\*\*\s*\n?', '', post).strip()
                post = re.sub(r'^\*\*🌙 POST \d+.*?\*\*\s*\n?', '', post).strip()
                if post and len(post) > 30:
                    posts.append(post)
            
            return posts[0] if posts else None
    except Exception as e:
        log(f"Error: {e}")
    return None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    return requests.post(url, json=data).status_code == 200

def main():
    post_type = sys.argv[1] if len(sys.argv) > 1 else "POST"
    log(f"=== Generating {post_type} ===")
    
    post = get_next_post()
    if not post:
        log("No posts available")
        sys.exit(1)
    
    message = f"📱 <b>X {post_type}</b>\n\n{post}\n\n<i>Copy above and post manually on X</i>"
    
    if send_telegram(message):
        log(f"✅ Sent: {post[:60]}...")
    else:
        log("❌ Failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
