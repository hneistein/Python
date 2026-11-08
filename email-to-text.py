import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Configuration
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
# Note: Gmail requires an "App Password" rather than your normal password
sender_password = os.getenv("SENDER_PASSWORD") 

# Recipient's phone number + their carrier's gateway domain
# T-Mobile: [number]@tmomail.net
# AT&T: [number]@txt.att.net
# Verizon: [number]@vtext.com
recipient_sms_gateway = os.getenv("RECIPIENT_SMS_GATEWAY") 
message_subject = "Pomodoro Timer"
message_body = "Break time is over, back to work!"

# Set up the MIME message
msg = MIMEText(message_body)
msg['Subject'] = message_subject
msg['From'] = sender_email
msg['To'] = recipient_sms_gateway

try:
    # Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_sms_gateway, msg.as_string())
    server.quit()
    print("Text message sent successfully!")
except Exception as e:
    print(f"Failed to send text: {e}")