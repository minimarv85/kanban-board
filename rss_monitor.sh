#!/bin/bash
# RSS Feed Monitor for Business/Research Trends
# Add to cron for automated monitoring: crontab -e
# 0 */6 * * * /home/skillman85/.openclaw/workspace/rss_monitor.sh >> /home/skillman85/.openclaw/workspace/rss_monitor.log 2>&1

FEEDS=(
  "https://news.ycombinator.com/rss"
  "https://www.producthunt.com/feed"
  "https://techcrunch.com/feed/"
  "https://www.bbc.co.uk/news/rss.xml"
  "https://feeds.bbci.co.uk/news/business/rss.xml"
  "https://www.theguardian.com/uk/business/rss"
)

OUTPUT_DIR="/home/skillman85/.openclaw/workspace/RSS_FEEDS"
mkdir -p "$OUTPUT_DIR"

echo "=== RSS Feed Monitor - $(date) ==="
echo ""

for feed in "${FEEDS[@]}"; do
  feed_name=$(echo "$feed" | sed 's|https://||; s|/||; s|\.|_|g')
  echo "📰 Fetching: $feed"
  
  # Fetch and save
  curl -s "$feed" -o "$OUTPUT_DIR/${feed_name}.xml" 2>/dev/null
  
  # Extract titles (basic XML parsing)
  if [ -f "$OUTPUT_DIR/${feed_name}.xml" ]; then
    echo "  Latest entries:"
    grep -o '<title>[^<]*</title>' "$OUTPUT_DIR/${feed_name}.xml" | head -5 | sed 's/<title>//; s/<\/title>//; s/^/    - /'
  fi
  echo ""
done

echo "=== Done ==="
