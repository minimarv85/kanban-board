#!/usr/bin/env python3
"""Send email via Gmail SMTP"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "minimarv85@gmail.com"
# NOTE: App Password required if 2FA is enabled
# If no 2FA, use regular password (less secure apps must be enabled)
SENDER_PASSWORD = "plyp zktw vkzd wvyj"

def send_email(to_email, subject, body_html, body_text):
    """Send email via Gmail"""
    try:
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"Marv - AI Assistant <{SENDER_EMAIL}>"
        msg["To"] = to_email
        
        # Attach both plain text and HTML versions
        part1 = MIMEText(body_text, "plain")
        part2 = MIMEText(body_html, "html")
        msg.attach(part1)
        msg.attach(part2)
        
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
        print("Usage: send_email.py <to_email> <subject> <body_file>")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body_file = sys.argv[3]
    
    with open(body_file, 'r') as f:
        body_text = f.read()
    
    # Add signature
    body_text = body_text.rstrip() + "\n\nKind Regards\nMarv - AI Assistant"
    
    # Simple HTML conversion
    body_html = body_text.replace('\n', '<br>')
    
    success, message = send_email(to_email, subject, body_html, body_text)
    print(message)
    sys.exit(0 if success else 1)
