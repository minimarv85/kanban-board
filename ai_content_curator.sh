#!/bin/bash
# AI/Tech Content Curator - Autonomous X Posting via Playwright
# Runs at 8am, 12pm, 6pm - researches fresh content and posts autonomously
# IMPORTANT: All posts MUST be under 280 characters

PYTHON_ENV="/home/skillman85/.openclaw/voice-env/bin/python"
POSTER_SCRIPT="/home/skillman85/.openclaw/workspace/x_poster.py"
POSTS_QUEUE="/home/skillman85/.openclaw/workspace/x_posts_queue.md"
LOG_FILE="/home/skillman85/.openclaw/workspace/x_posting.log"
HOUR=$(date +%H)
DATE=$(date +%Y-%m-%d)

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
    echo "$1"
}

research_topics() {
    log "🔍 Researching trending AI/tech topics..."
    
    # Search DuckDuckGo for latest AI news
    TOPICS=$(curl -s "https://duckduckgo.com/html/?q=AI+technology+news+trending+site:news" 2>/dev/null | grep -oP '(?<=<a class="result__a" href=")[^"]*' | head -5 | sed 's|https://||' | cut -d'/' -f1 | head -3)
    
    # Search X (Twitter) trending
    TRENDING=$(curl -s "https://nitter.net/api/v1/trends" 2>/dev/null | grep -oP '"name":"[^"]*' | head -10 | cut -d'"' -f4 | grep -i "AI\|Tech\|OpenAI\|Google\|Microsoft" | head -3)
    
    log "Found topics: $TOPICS $TRENDING"
    echo "$TOPICS $TRENDING"
}

generate_post() {
    TOPICS="$1"
    
    # Simple templates based on current date/time
    HOUR=$((10#$HOUR))
    
    if [ $HOUR -ge 5 ] && [ $HOUR -lt 12 ]; then
        TYPE="morning"
    elif [ $HOUR -ge 12 ] && [ $HOUR -lt 18 ]; then
        TYPE="midday"
    else
        TYPE="evening"
    fi
    
    # Generate post based on current day for variety
    DAY=$(date +%u)
    
    case $DAY in
        1)  # Monday
            POST="Monday mood: AI tools that actually ship > endless理论研究. Build more, theorize less. 🚀" ;;
        2)  # Tuesday
            POST="Just checked what Claude Code can do now. These autonomous agents are moving FAST. 2025 gonna be wild. 🔥" ;;
        3)  # Wednesday
            POST="The boring AI stuff is winning. Not the flashiest. Not the most hyped. Just the stuff that works. 💡" ;;
        4)  # Thursday
            POST="Hot take: OpenAI might not be the winner long-term. Niche > generalist when the generalist gets commoditized. 🎯" ;;
        5)  # Friday
            POST="Week in review: AI progress is actually INSANE when you stop doomscrolling. Small models getting big capabilities. 📈" ;;
        6)  # Saturday
            POST="Saturday thought: The real AI advantage isn't the model. It's the workflow integration. Build better processes. ⚡" ;;
        7)  # Sunday
            POST="Sunday vibe: Rest up. Next week's AI developments gonna be busy. Stay curious. 🧠" ;;
        *)  POST="AI update mode: ON. The pace isn't slowing down. Adaptation is the skill. 📊" ;;
    esac
    
    echo "$POST"
}

log "=== X Content Curator - $DATE ==="

# Always research and add fresh content first
FRESH_TOPICS=$(research_topics)
NEW_POST=$(generate_post "$FRESH_TOPICS")

# Add new post to top of queue
sed -i "1i\\$NEW_POST" "$POSTS_QUEUE"
log "Added fresh post: ${NEW_POST:0:50}..."

# Check if there are posts to post now (not just added)
CURRENT_HOUR_POSTS=$(grep -c "^🚀\|^Just\|^Hot\|^What'\|^The\|^Sometimes\|^AI\|^\[.*\]" "$POSTS_QUEUE" 2>/dev/null || echo "0")

if [ "$CURRENT_HOUR_POSTS" -gt "1" ]; then
    log "Multiple posts available, will post from queue"
fi

# Get next post from queue (skip the one we just added if this is a posting time)
if [ "$HOUR" = "08" ] || [ "$HOUR" = "12" ] || [ "$HOUR" = "18" ]; then
    NEXT_POST=$(grep -v "^#" "$POSTS_QUEUE" | grep -v "^$" | head -1)
    
    if [ -z "$NEXT_POST" ]; then
        log "No posts in queue!"
        exit 1
    fi
    
    log "Posting: ${NEXT_POST:0:50}..."
    
    # Post via Playwright
    $PYTHON_ENV "$POSTER_SCRIPT" "$NEXT_POST" >> "$LOG_FILE" 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Post successful!"
        
        # Remove posted tweet from queue (only if it's the one we posted)
        FIRST_POST=$(grep -v "^#" "$POSTS_QUEUE" | grep -v "^$" | head -1)
        if [ "$FIRST_POST" = "$NEXT_POST" ]; then
            sed -i '1d' "$POSTS_QUEUE" 2>/dev/null
        fi
        
        # Add to posted log
        echo "[$DATE $HOUR] $NEXT_POST" >> /home/skillman85/.openclaw/workspace/posted_tweets.log
    else
        log "❌ Post failed"
    fi
else
    log "Not a posting hour ($HOUR). Fresh content added to queue."
fi

log "=== Done ==="
