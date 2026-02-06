#!/bin/bash
# X/Twitter Autonomous Poster - Daily Cron Script
# Posts content to X automatically every day

set -e

# Configuration
PYTHON_ENV="/home/skillman85/.openclaw/voice-env/bin/python"
POSTER_SCRIPT="/home/skillman85/.openclaw/workspace/x_poster.py"
POSTS_FILE="/home/skillman85/.openclaw/workspace/x_posts_queue.md"
LOG_FILE="/home/skillman85/.openclaw/workspace/x_posting.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "========================================="
log "X Autonomous Posting - Starting"
log "========================================="

# Check if posts file exists
if [ ! -f "$POSTS_FILE" ]; then
    log "ERROR: Posts file not found: $POSTS_FILE"
    exit 1
fi

# Get next tweet from file
TWEET=$(grep -v "^#" "$POSTS_FILE" | grep -v "^$" | head -1)

if [ -z "$TWEET" ]; then
    log "ERROR: No tweets found in $POSTS_FILE"
    exit 1
fi

log "Posting tweet: ${TWEET:0:50}..."

# Run the poster
$PYTHON_ENV "$POSTER_SCRIPT" "$TWEET" >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    log "SUCCESS: Tweet posted!"
    
    # Remove posted tweet from file
    sed -i '1d' "$POSTS_FILE" 2>/dev/null || true
    
    # Add to posted log
    echo "[$(date '+%Y-%m-%d')] $TWEET" >> /home/skillman85/.openclaw/workspace/posted_tweets.log
else
    log "ERROR: Failed to post tweet"
    exit 1
fi

log "Done!"
