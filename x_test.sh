#!/bin/bash
# X/Twitter Autonomous Poster - Quick Test Script
# Tests the posting system

set -e

echo "========================================="
echo "X Autonomous Poster - System Test"
echo "========================================="

# Check Python environment
echo ""
echo "1. Checking Python environment..."
if [ -f "/home/skillman85/.openclaw/voice-env/bin/python" ]; then
    echo "   ✅ Python env found"
else
    echo "   ❌ Python env NOT found"
    exit 1
fi

# Check poster script
echo ""
echo "2. Checking poster script..."
if [ -f "/home/skillman85/.openclaw/workspace/x_poster.py" ]; then
    echo "   ✅ Poster script found"
else
    echo "   ❌ Poster script NOT found"
    exit 1
fi

# Check cookies
echo ""
echo "3. Checking X cookies..."
if [ -f "/home/skillman85/.config/bird/config.json5" ]; then
    if grep -q "authToken" /home/skillman85/.config/bird/config.json5; then
        echo "   ✅ Cookies configured"
    else
        echo "   ⚠️  Cookies may not be configured"
    fi
else
    echo "   ❌ No bird config found"
fi

# Check posts queue
echo ""
echo "4. Checking posts queue..."
if [ -f "/home/skillman85/.openclaw/workspace/x_posts_queue.md" ]; then
    POST_COUNT=$(grep -v "^#" /home/skillman85/.openclaw/workspace/x_posts_queue.md | grep -v "^$" | wc -l)
    echo "   ✅ $POST_COUNT posts in queue"
else
    echo "   ❌ No posts queue found"
fi

# Test Playwright import
echo ""
echo "5. Testing Playwright import..."
if source /home/skillman85/.openclaw/voice-env/bin/activate && python3 -c "import playwright" 2>/dev/null; then
    echo "   ✅ Playwright installed"
else
    echo "   ❌ Playwright NOT installed"
    exit 1
fi

echo ""
echo "========================================="
echo "Test Complete!"
echo "========================================="
echo ""
echo "To post a tweet manually:"
echo "  /home/skillman85/.openclaw/voice-env/bin/python /home/skillman85/.openclaw/workspace/x_poster.py 'Your tweet here'"
echo ""
echo "To run daily posting:"
echo "  bash /home/skillman85/.openclaw/workspace/x_daily_poster.sh"
echo ""
echo "Scheduled: Daily at 23:00 via cron"
echo ""
