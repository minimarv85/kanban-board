#!/usr/bin/env python3
"""
OpenClaw Voice Note Processor

This script enables voice note transcription for OpenClaw.
When a voice note is sent to OpenClaw on Telegram,
this script will transcribe it and process it as a command.

Setup:
1. Install dependencies: pip install openai-whisper ffmpy
2. Configure voice_config.json
3. Add as a message handler or custom command

Usage:
    python3 voice_handler.py <audio_file> [--session main]
"""

import sys
import os
import json
import subprocess
import tempfile
from pathlib import Path

# Configuration
CONFIG_PATH = "/home/skillman85/.openclaw/workspace/voice_config.json"
OPENCLAW_WS = "/home/skillman85/.openclaw/workspace"
WHISPER_ENV = "/home/skillman85/.openclaw/voice-env/bin/python"
TRANSCRIBE_SCRIPT = "/home/skillman85/.openclaw/workspace/transcribe.py"

def load_config():
    """Load voice configuration"""
    try:
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}", file=sys.stderr)
        return None

def transcribe(audio_path):
    """Transcribe audio file using Whisper"""
    try:
        result = subprocess.run(
            [WHISPER_ENV, TRANSCRIBE_SCRIPT, audio_path],
            capture_output=True,
            text=True,
            cwd=OPENCLAW_WS
        )
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return None, str(e)

def process_command(text):
    """Process transcribed text as OpenClaw command"""
    # This would integrate with OpenClaw's command processing
    # For now, just return the text
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: voice_handler.py <audio_file> [--session session_name]", file=sys.stderr)
        sys.exit(1)
    
    audio_file = sys.argv[1]
    session = "main"
    
    if "--session" in sys.argv:
        idx = sys.argv.index("--session")
        if len(sys.argv) > idx + 1:
            session = sys.argv[idx + 1]
    
    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found: {audio_file}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing voice note: {audio_file}", file=sys.stderr)
    
    # Transcribe
    text, error = transcribe(audio_file)
    
    if error:
        print(f"Transcription error: {error}", file=sys.stderr)
        sys.exit(1)
    
    if not text:
        print("No transcription available", file=sys.stderr)
        sys.exit(1)
    
    # Process as command
    result = process_command(text)
    
    # Output for OpenClaw
    print("=== TRANSCRIPTION ===")
    print(text)
    print("=== END TRANSCRIPTION ===")
    
    # Clean up
    try:
        os.remove(audio_file)
    except:
        pass

if __name__ == "__main__":
    main()
