#!/usr/bin/env python3
"""
Whisper Voice Transcription Script
Used by OpenClaw to transcribe voice notes from Telegram
"""

import sys
import whisper
import ffmpy
import tempfile
import os
from pathlib import Path

def transcribe_audio(audio_path):
    """
    Transcribe audio file using OpenAI Whisper
    
    Args:
        audio_path: Path to audio file (ogg, mp3, wav, etc.)
    
    Returns:
        str: Transcribed text
    """
    try:
        # Check if audio file exists
        if not os.path.exists(audio_path):
            return f"Error: Audio file not found: {audio_path}"
        
        # Convert audio to WAV format (Whisper works best with WAV)
        wav_path = audio_path
        if not audio_path.endswith('.wav'):
            wav_path = tempfile.mktemp(suffix='.wav')
            try:
                ff = ffmpy.FFmpeg(inputs={audio_path: None}, outputs={wav_path: ['-y', '-ar', '16000', '-ac', '1']})
                ff.run()
            except Exception as e:
                # If ffmpeg fails, try using the original file
                wav_path = audio_path
        
        # Load Whisper model (tiny is fastest, base is good balance, small is better quality)
        print("Loading Whisper model...", file=sys.stderr)
        model = whisper.load_model("tiny")
        
        # Transcribe
        print("Transcribing audio...", file=sys.stderr)
        result = model.transcribe(wav_path)
        text = result["text"].strip()
        
        # Clean up temp file if created
        if wav_path != audio_path and os.path.exists(wav_path):
            os.remove(wav_path)
        
        # Delete original audio file after transcription
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
                print(f"Cleaned up: {audio_path}", file=sys.stderr)
            except Exception as e:
                print(f"Warning: Could not delete {audio_path}: {e}", file=sys.stderr)
        
        return text if text else "Could not transcribe audio"
        
    except Exception as e:
        return f"Transcription error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: transcribe.py <audio_file>", file=sys.stderr)
        sys.exit(1)
    
    audio_file = sys.argv[1]
    result = transcribe_audio(audio_file)
    print(result)
