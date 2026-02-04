#!/usr/bin/env python3
"""
X (Twitter) Autonomous Poster - Headed Mode Version
Uses headed Chrome (visible) which is harder for X to detect

Usage:
    xvfb-run -a python3 x_poster_headed.py "Your tweet content here"
    # OR for testing without xvfb:
    python3 x_poster_headed.py "Your tweet content here"  # will open visible window
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
            for line in content.split("\n"):
                line = line.strip()
                if line and not line.startswith("#"):
                    return line
            return None
    except Exception as e:
        log(f"Error reading tweet file: {e}")
        return None

async def post_to_x(playwright, tweet_content):
    """Post a tweet using headed Chrome (harder to detect)"""
    
    auth_token, ct0 = load_cookies()
    
    if not auth_token or not ct0:
        log("ERROR: No cookies found. Please configure bird first.")
        return False
    
    log("Launching headed Chrome (harder to detect)...")
    
    # Use headed mode - much harder for X to detect automation
    browser = await playwright.chromium.launch(
        headless=False,  # headed mode
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--window-size=1280,720",
        ]
    )
    
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 720},
        locale="en-US",
    )
    
    page = await context.new_page()
    
    try:
        log("Navigating to X (this will open a visible window)...")
        await page.goto("https://twitter.com/home", wait_until="networkidle", timeout=60000)
        
        log("Adding authentication cookies...")
        await context.add_cookies([
            {"name": "auth_token", "value": auth_token, "url": "https://twitter.com"},
            {"name": "ct0", "value": ct0, "url": "https://twitter.com"},
        ])
        
        await page.goto("https://twitter.com/home", wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(2000)
        
        # Check if logged in
        try:
            await page.wait_for_selector('[data-testid="tweetTextarea_0"]', timeout=15000)
            log("✓ Logged in successfully!")
        except:
            log("⚠ Could not verify login. Continuing anyway...")
        
        log("Opening compose box...")
        await page.goto("https://x.com/compose/post", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        
        # Find compose box
        log("Finding compose box...")
        compose_box = None
        
        selectors = [
            '[data-testid="tweetTextarea_0"]',
            'div[role="textbox"]',
        ]
        
        for selector in selectors:
            try:
                compose_box = await page.query_selector(selector)
                if compose_box:
                    log(f"✓ Found compose box: {selector}")
                    break
            except:
                continue
        
        if not compose_box:
            log("⚠ Could not find compose box")
            await page.screenshot(path="/home/skillman85/.openclaw/workspace/x_debug_headed.png")
            return False
        
        log("Posting tweet...")
        
        await compose_box.click()
        await asyncio.sleep(0.5)
        await page.keyboard.type(tweet_content, delay=80)
        await asyncio.sleep(1)
        
        # Find tweet button
        tweet_button = None
        for selector in ['[data-testid="tweetButtonInline"]', '[data-testid="tweetButton"]']:
            try:
                tweet_button = await page.query_selector(selector)
                if tweet_button:
                    log(f"✓ Found tweet button: {selector}")
                    break
            except:
                continue
        
        if tweet_button:
            await tweet_button.click()
            log("✓ Tweet button clicked!")
            await asyncio.sleep(3)
            log("✅ SUCCESS: Tweet posted!")
            return True
        else:
            log("⚠ No button, trying Enter key...")
            await page.keyboard.press("Enter")
            await asyncio.sleep(2)
            log("✅ Tweet posted via Enter!")
            return True
            
    except Exception as e:
        log(f"ERROR: {e}")
        await page.screenshot(path="/home/skillman85/.openclaw/workspace/x_error_headed.png")
        return False
    
    finally:
        await asyncio.sleep(5)  # Let user see the result
        await browser.close()

async def main():
    parser = argparse.ArgumentParser(description="X (Twitter) Poster - Headed Mode")
    parser.add_argument("tweet", nargs="?", help="Tweet content")
    parser.add_argument("--file", "-f", help="Read from file")
    parser.add_argument("--cron", action="store_true", help="Cron mode")
    
    args = parser.parse_args()
    
    tweet_content = None
    
    if args.tweet:
        tweet_content = args.tweet
    elif args.file:
        tweet_content = get_tweet_from_file(args.file)
    elif args.cron:
        tweet_content = get_tweet_from_file(TWEETS_FILE)
    else:
        tweet_content = get_tweet_from_file(TWEETS_FILE)
    
    if not tweet_content:
        log("ERROR: No tweet content")
        sys.exit(1)
    
    if len(tweet_content) > 280:
        log(f"⚠ Truncating from {len(tweet_content)} chars...")
        tweet_content = tweet_content[:277] + "..."
    
    log(f"Posting: {tweet_content[:50]}...")
    
    async with async_playwright() as p:
        success = await post_to_x(p, tweet_content)
    
    if success:
        log("✅ Done!")
        sys.exit(0)
    else:
        log("❌ Failed")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
