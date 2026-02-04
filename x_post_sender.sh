#!/bin/bash
# X Post Sender - Generates content and sends to Telegram for manual posting

SCRIPT_DIR="/home/skillman85/.openclaw/workspace"
POSTS_FILE="$SCRIPT_DIR/daily_posts.md"
TELEGRAM_DATA="$SCRIPT_DIR/telegram_bot_data.json"
LOG_FILE="$SCRIPT_DIR/x_delivery.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Get next post from queue
get_next_post() {
    if [ -f "$POSTS_FILE" ]; then
        # Get first non-empty, non-comment line
        sed '/^#/d; /^$/d' "$POSTS_FILE" | head -1
    fi
}

# Send to Telegram
send_to_telegram() {
    local message="$1"
    local bot_token=$(cat "$TELEGRAM_DATA" 2>/dev/null | grep '"token"' | cut -d'"' -f4)
    local chat_id=$(cat "$TELEGRAM_DATA" 2>/dev/null | grep '"chat_id"' | cut -d'"' -f4)
    
    if [ -z "$bot_token" ] || [ -z "$chat_id" ]; then
        log "ERROR: Telegram credentials not found"
        return 1
    fi
    
    curl -s -X POST "https://api.telegram.org/bot$bot_token/sendMessage" \
        -d "chat_id=$chat_id" \
        -d "text=$message" \
        -d "parse_mode=HTML" > /dev/null
}

# Main
POST_TYPE="$1"
if [ -z "$POST_TYPE" ]; then
    POST_TYPE="POST"
fi

log "=== Generating $POST_TYPE ==="

# Generate new content
cd "$SCRIPT_DIR"
NEW_POST=$(bash ai_content_curator.sh 2>/dev/null)

if [ -z "$NEW_POST" ]; then
    # Fallback to queued post
    NEW_POST=$(get_next_post)
fi

if [ -z "$NEW_POST" ]; then
    log "ERROR: No content available"
    exit 1
fi

# Format message
MESSAGE="📱 <b>X $POST_TYPE</b>

$NEW_POST

<i>Copy and post manually</i>"

# Send to Telegram
send_to_telegram "$MESSAGE"

if [ $? -eq 0 ]; then
    log "✅ Sent: $NEW_POST"
else
    log "❌ Failed to send"
fi
