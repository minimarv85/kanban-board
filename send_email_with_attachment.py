#!/usr/bin/env python3
"""Send email via Gmail SMTP with attachments"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import os

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "minimarv85@gmail.com"
SENDER_PASSWORD = "plyp zktw vkzd wvyj"

def send_email(to_email, subject, body_text, attachments=None):
    """Send email via Gmail with optional attachments"""
    try:
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"Marv - AI Assistant <{SENDER_EMAIL}>"
        msg["To"] = to_email
        
        # Attach plain text version
        part1 = MIMEText(body_text, "plain")
        msg.attach(part1)
        
        # Attach files if provided
        if attachments:
            for filepath in attachments:
                if os.path.exists(filepath):
                    with open(filepath, "rb") as f:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                    encoders.encode_base64(part)
                    filename = os.path.basename(filepath)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
                    )
                    msg.attach(part)
        
        # Send via Gmail SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return True, "Email sent successfully"
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_email_with_attachment.py <to_email> <subject> <body_file> [attachment1] [attachment2]...")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body_file = sys.argv[3]
    attachments = sys.argv[4:] if len(sys.argv) > 4 else []
    
    with open(body_file, 'r') as f:
        body_text = f.read()
    
    success, message = send_email(to_email, subject, body_text, attachments)
    print(message)
    sys.exit(0 if success else 1)
