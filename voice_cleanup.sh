#!/bin/bash
# Weekly Voice Note Cleanup Script
# Deletes audio files older than 7 days
# Run via cron: 0 3 * * 0 /home/skillman85/.openclaw/workspace/voice_cleanup.sh

MEDIA_DIR="/home/skillman85/.openclaw/media/inbound"
DAYS_OLD=7
LOG_FILE="/home/skillman85/.openclaw/workspace/voice_cleanup.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

log "Starting voice note cleanup..."

# Check if directory exists
if [ ! -d "$MEDIA_DIR" ]; then
    log "Directory not found: $MEDIA_DIR"
    exit 0
fi

# Count files to be deleted
FILE_COUNT=$(find "$MEDIA_DIR" -name "*.mp3" -o -name "*.ogg" -o -name "*.wav" -o -name "*.mp4" -o -name "*.m4a" -o -name "*.oga" -type f -mtime +$DAYS_OLD 2>/dev/null | wc -l)

if [ "$FILE_COUNT" -eq 0 ]; then
    log "No old voice files to clean"
    exit 0
fi

# Delete old files
find "$MEDIA_DIR" -name "*.mp3" -o -name "*.ogg" -o -name "*.wav" -o -name "*.mp4" -o -name "*.m4a" -o -name "*.oga" -type f -mtime +$DAYS_OLD -delete 2>/dev/null

log "Cleaned $FILE_COUNT old voice note files"

# Also clean up any stuck temp files from transcription
find "$MEDIA_DIR" -name "tmp*" -type f -mtime +1 -delete 2>/dev/null

log "Cleanup complete"
