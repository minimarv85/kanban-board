#!/usr/bin/env python3
"""
X (Twitter) Autonomous Poster using Playwright + Stealth Scripts
Posts content to X using browser automation with stealth evasion

Usage:
    python3 x_poster_stealth.py "Your tweet content here"

Features:
- Uses Playwright with stealth evasion scripts
- Authenticates via cookies
- Posts like a real user
- Runs headless
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

# Stealth evasion scripts
STEALTH_SCRIPTS = """
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined,
});

Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3, 4, 5],
});

Object.defineProperty(navigator, 'languages', {
    get: () => ['en-US', 'en'],
});

Object.defineProperty(navigator, 'platform', {
    get: () => 'Win32',
});

Object.defineProperty(navigator, 'vendor', {
    get: () => 'Google Inc.',
});

window.chrome = {
    runtime: {},
};

Object.defineProperty(window, 'chrome', {
    get: () => window.chrome,
});

Object.defineProperty(navigator, 'hardwareConcurrency', {
    get: () => 8,
});

delete navigator.__proto__.webdriver;
"""

async def post_to_x(playwright, tweet_content):
    """Post a tweet using Playwright with stealth"""
    
    auth_token, ct0 = load_cookies()
    
    if not auth_token or not ct0:
        log("ERROR: No cookies found. Please configure bird first.")
        return False
    
    log("Launching browser with stealth patches...")
    browser = await playwright.chromium.launch(
        headless=True,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-gpu",
            "--disable-web-security",
            "--disable-features=IsolateOrigins,site-per-process",
        ]
    )
    
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 720},
        locale="en-US",
        timezone_id="America/New_York",
    )
    
    page = await context.new_page()
    
    # Apply stealth scripts
    await page.add_init_script(STEALTH_SCRIPTS)
    
    # Patch CDP detection
    await page.route("**/*", lambda route: route.continue_())
    
    try:
        log("Navigating to X...")
        await page.goto("https://twitter.com/home", wait_until="networkidle", timeout=60000)
        
        # Add cookies to authenticate
        log("Adding authentication cookies...")
        await context.add_cookies([
            {"name": "auth_token", "value": auth_token, "url": "https://twitter.com"},
            {"name": "ct0", "value": ct0, "url": "https://twitter.com"},
        ])
        
        # Refresh to apply cookies
        await page.goto("https://twitter.com/home", wait_until="networkidle", timeout=60000)
        
        await page.wait_for_timeout(3000)
        
        # Check if logged in
        try:
            await page.wait_for_selector('[data-testid="tweetTextarea_0"]', timeout=15000)
            log("Logged in successfully!")
        except:
            log("WARNING: Could not verify login. Trying anyway...")
        
        # Navigate to compose
        log("Opening compose box...")
        await page.goto("https://x.com/compose/post", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        
        # Find compose box
        log("Finding compose box...")
        compose_box = None
        
        selectors = [
            '[data-testid="tweetTextarea_0"]',
            'div[role="textbox"]',
            '[contenteditable="true"]',
        ]
        
        for selector in selectors:
            try:
                compose_box = await page.query_selector(selector)
                if compose_box:
                    log(f"Found compose box with selector: {selector}")
                    break
            except:
                continue
        
        if not compose_box:
            log("WARNING: Could not find compose box")
            await page.screenshot(path="/home/skillman85/.openclaw/workspace/x_debug_stealth.png")
            log("Screenshot saved to /home/skillman85/.openclaw/workspace/x_debug_stealth.png")
            return False
        
        log("Posting tweet...")
        
        await compose_box.click()
        await asyncio.sleep(0.5)
        
        # Type the tweet
        await page.keyboard.type(tweet_content, delay=80)
        
        await asyncio.sleep(1)
        
        # Find tweet button
        tweet_button = None
        button_selectors = [
            '[data-testid="tweetButtonInline"]',
            '[data-testid="tweetButton"]',
        ]
        
        for selector in button_selectors:
            try:
                tweet_button = await page.query_selector(selector)
                if tweet_button:
                    log(f"Found tweet button with selector: {selector}")
                    break
            except:
                continue
        
        if tweet_button:
            await tweet_button.click()
            log("Tweet button clicked!")
            await asyncio.sleep(3)
            log("SUCCESS: Tweet posted!")
            return True
        else:
            log("WARNING: Could not find tweet button, trying Enter key...")
            await page.keyboard.press("Enter")
            await asyncio.sleep(2)
            log("Tweet posted via Enter key")
            return True
            
    except Exception as e:
        log(f"ERROR posting tweet: {e}")
        await page.screenshot(path="/home/skillman85/.openclaw/workspace/x_error_stealth.png")
        return False
    
    finally:
        await browser.close()

async def main():
    parser = argparse.ArgumentParser(description="X (Twitter) Autonomous Poster with Stealth")
    parser.add_argument("tweet", nargs="?", help="Tweet content to post")
    parser.add_argument("--file", "-f", help="Read tweet from file")
    parser.add_argument("--cron", action="store_true", help="Run in cron mode (use daily_posts.md)")
    
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
        log("ERROR: No tweet content provided")
        sys.exit(1)
    
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
