#!/usr/bin/env python3
"""
Voice Note Transcription for OpenClaw

This script integrates with OpenClaw to transcribe voice notes
sent via Telegram and process them as commands.

Usage:
    python3 voice_processor.py <audio_file> [--process]
    
With --process flag: automatically processes the transcription
as an OpenClaw command.
"""

import sys
import os
import json
import subprocess
from pathlib import Path

# Add OpenClaw to path
OPENCLAW_PATH = "/home/skillman85/.openclaw"

# Whisper environment
WHISPER_ENV = os.path.join(OPENCLAW_PATH, "voice-env", "bin", "python")
SCRIPT_PATH = os.path.join(OPENCLAW_PATH, "workspace", "transcribe.py")

def transcribe(audio_path):
    """Transcribe audio file using Whisper"""
    result = subprocess.run(
        [WHISPER_ENV, SCRIPT_PATH, audio_path],
        capture_output=True,
        text=True,
        cwd=OPENCLAW_PATH
    )
    return result.stdout.strip(), result.stderr.strip()

def send_to_session(text):
    """Send transcribed text to OpenClaw main session"""
    try:
        # Send as a system event or message to main session
        # This depends on OpenClaw's session API
        result = subprocess.run(
            ["openclaw", "message", "--session", "main", "--text", text],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Failed to send to session: {e}", file=sys.stderr)
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: voice_processor.py <audio_file> [--process]", file=sys.stderr)
        sys.exit(1)
    
    audio_file = sys.argv[1]
    process = "--process" in sys.argv
    
    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found: {audio_file}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Transcribing: {audio_file}", file=sys.stderr)
    text, stderr = transcribe(audio_file)
    
    if text.startswith("Error") or not text:
        print(f"Transcription failed: {text}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Transcription: {text}", file=sys.stderr)
    
    if process:
        print(f"Sending to OpenClaw session...", file=sys.stderr)
        # The transcription will be processed by OpenClaw
        print(text)
    else:
        print(text)

if __name__ == "__main__":
    main()
