#!/usr/bin/env python3
"""
X (Twitter) Autonomous Poster using Playwright
Posts content to X using browser automation with cookies

Usage:
    python3 x_poster.py "Your tweet content here"
    python3 x_poster.py --file /path/to/tweet.txt
    python3 x_poster.py --cron --schedule 23:00

Features:
- Uses Playwright for browser automation
- Authenticates via cookies (no API needed)
- Posts like a real user (human-like behavior)
- Runs headless (invisible browser)
- Logs all activity
"""

import asyncio
import sys
import os
import json
import argparse
from datetime import datetime
from pathlib import Path

# Playwright
from playwright.async_api import async_playwright

# Configuration
COOKIES_FILE = os.path.expanduser("~/.config/bird/config.json5")
LOG_FILE = "/home/skillman85/.openclaw/workspace/x_posting.log"
TWEETS_FILE = "/home/skillman85/.openclaw/workspace/daily_posts.md"

def log(message):
    """Log message to file and stdout"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted)
    with open(LOG_FILE, "a") as f:
        f.write(formatted + "\n")

def load_cookies():
    """Load cookies from bird config"""
    try:
        with open(COOKIES_FILE, "r") as f:
            content = f.read()
            # Parse simple JSON5-like format
            auth_token = None
            ct0 = None
            for line in content.split("\n"):
                if "authToken" in line:
                    parts = line.split(":")
                    if len(parts) > 1:
                        auth_token = parts[1].strip().strip(",").strip('"')
                elif "ct0" in line:
                    parts = line.split(":")
                    if len(parts) > 1:
                        ct0 = parts[1].strip().strip(",").strip('"')
            return auth_token, ct0
    except Exception as e:
        log(f"Error loading cookies: {e}")
        return None, None

def get_tweet_from_file(filepath):
    """Get next tweet from file"""
    try:
        with open(filepath, "r") as f:
            content = f.read()
            # Simple parsing - get first non-empty, non-comment line
            for line in content.split("\n"):
                line = line.strip()
                if line and not line.startswith("#"):
                    return line
            return None
    except Exception as e:
        log(f"Error reading tweet file: {e}")
        return None

async def post_to_x(playwright, tweet_content):
    """Post a tweet using Playwright"""
    
    auth_token, ct0 = load_cookies()
    
    if not auth_token or not ct0:
        log("ERROR: No cookies found. Please configure bird first.")
        return False
    
    log("Launching browser...")
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    )
    
    page = await context.new_page()
    
    try:
        log("Navigating to X...")
        await page.goto("https://twitter.com/i/flow/login", wait_until="networkidle")
        
        # Add cookies to authenticate
        log("Adding authentication cookies...")
        await context.add_cookies([
            {"name": "auth_token", "value": auth_token, "url": "https://twitter.com"},
            {"name": "ct0", "value": ct0, "url": "https://twitter.com"},
        ])
        
        # Refresh to apply cookies
        await page.goto("https://twitter.com/home", wait_until="networkidle")
        
        # Check if logged in
        await page.wait_for_timeout(2000)
        
        # Try to find compose button
        try:
            compose_button = await page.query_selector('[data-testid="tweetTextarea_0"]')
            if not compose_button:
                # Try alternative selectors
                compose_button = await page.query_selector('div[role="textbox"]')
        except:
            compose_button = None
        
        if not compose_button:
            log("WARNING: Could not find compose box. Might need human login.")
            # Save screenshot for debugging
            await page.screenshot(path="/home/skillman85/.openclaw/workspace/x_debug.png")
            log("Screenshot saved to /home/skillman85/.openclaw/workspace/x_debug.png")
            return False
        
        log("Found compose box! Posting tweet...")
        
        # Click and type (human-like behavior)
        await compose_button.click()
        await asyncio.sleep(0.5)
        
        # Type the tweet
        await page.keyboard.type(tweet_content, delay=50)  # Human-like typing
        
        await asyncio.sleep(0.5)
        
        # Find and click tweet button
        tweet_button = await page.query_selector('[data-testid="tweetButtonInline"]')
        
        if tweet_button:
            await tweet_button.click()
            log(f"SUCCESS: Tweet posted!")
            await asyncio.sleep(2)
            return True
        else:
            log("WARNING: Could not find tweet button")
            return False
            
    except Exception as e:
        log(f"ERROR posting tweet: {e}")
        await page.screenshot(path="/home/skillman85/.openclaw/workspace/x_error.png")
        return False
    
    finally:
        await browser.close()

async def main():
    parser = argparse.ArgumentParser(description="X (Twitter) Autonomous Poster")
    parser.add_argument("tweet", nargs="?", help="Tweet content to post")
    parser.add_argument("--file", "-f", help="Read tweet from file")
    parser.add_argument("--cron", action="store_true", help="Run in cron mode (use daily_posts.md)")
    parser.add_argument("--schedule", "-s", help="Schedule time (e.g., 23:00)")
    
    args = parser.parse_args()
    
    # Get tweet content
    tweet_content = None
    
    if args.tweet:
        tweet_content = args.tweet
    elif args.file:
        tweet_content = get_tweet_from_file(args.file)
    elif args.cron:
        tweet_content = get_tweet_from_file(TWEETS_FILE)
    else:
        # Default: use daily_posts.md
        tweet_content = get_tweet_from_file(TWEETS_FILE)
    
    if not tweet_content:
        log("ERROR: No tweet content provided")
        sys.exit(1)
    
    # Truncate if too long
    if len(tweet_content) > 280:
        log(f"WARNING: Tweet too long ({len(tweet_content)} chars), truncating...")
        tweet_content = tweet_content[:277] + "..."
    
    log(f"Posting tweet: {tweet_content[:50]}...")
    
    async with async_playwright() as p:
        success = await post_to_x(p, tweet_content)
    
    if success:
        log("Tweet posted successfully!")
        sys.exit(0)
    else:
        log("Failed to post tweet")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
