#!/bin/bash
# Voice Note Transcription for OpenClaw
# Usage: ./voice_transcribe.sh <audio_file>
# This script integrates with OpenClaw to transcribe voice notes

AUDIO_FILE="$1"
WHISPER_ENV="/home/skillman85/.openclaw/voice-env/bin/python"
SCRIPT_DIR="/home/skillman85/.openclaw/workspace"

if [ -z "$AUDIO_FILE" ]; then
    echo "Usage: voice_transcribe.sh <audio_file>"
    exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: File not found: $AUDIO_FILE"
    exit 1
fi

echo "Transcribing voice note..."

# Run whisper transcription
TRANSCRIPTION=$("$WHISPER_ENV" "$SCRIPT_DIR/transcribe.py" "$AUDIO_FILE" 2>&1)

# Output the transcription
echo "$TRANSCRIPTION"

# If running in OpenClaw context, this would be captured and processed
