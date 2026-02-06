# RSS Feed Monitor Setup

## What's Installed

### RSS Monitor Script
- **Location:** `/home/skillman85/.openclaw/workspace/rss_monitor.sh`
- **Feeds Monitored:**
  - Hacker News (YC)
  - Product Hunt
  - TechCrunch
  - BBC News
  - BBC Business
  - The Guardian Business

### Cron Job
- **Schedule:** Every 6 hours (`0 */6 * * *`)
- **Log:** `/home/skillman85/.openclaw/workspace/rss_monitor.log`
- **Status:** Active ✅

## Usage

```bash
# Run manually
/home/skillman85/.openclaw/workspace/rss_monitor.sh

# View latest results
cat /home/skillman85/.openclaw/workspace/rss_monitor.log

# Add more feeds (edit the script)
nano /home/skillman85/.openclaw/workspace/rss_monitor.sh
```

## Add More Feeds

Edit the FEEDS array in the script:
```bash
FEEDS=(
  "https://news.ycombinator.com/rss"
  "https://www.producthunt.com/feed"
  "https://your-feed-here.com/rss"
)
```

## Future: Blogwatcher

If you want to install blogwatcher later (requires Go):
```bash
export PATH=$PATH:/usr/local/go/bin
go install github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest
```

Then use:
```bash
blogwatcher add "My Blog" https://example.com
blogwatcher scan
```
