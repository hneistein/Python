import smtplib
from email.mime.text import MIMEText
import os
from pathlib import Path
from dotenv import load_dotenv

def send_break_over_sms():

    # Force Python to look in the exact same folder as this script file
    env_path = Path(__file__).resolve().parent / '.env'
    load_dotenv(dotenv_path=env_path)

    # Configuration
    smtp_server = os.getenv("SMTP_SERVER") # I used gmail
    smtp_port = os.getenv("SMTP_PORT") # I used 587
    sender_email = os.getenv("SENDER_EMAIL") # I used my gmail email address
    # Note: Gmail requires an "App Password" rather than your normal password
    sender_password = os.getenv("SENDER_PASSWORD") 

    # Recipient's phone number + their carrier's gateway domain
    # T-Mobile: [number]@tmomail.net
    # AT&T: [number]@txt.att.net
    # Verizon: [number]@vtext.com
    recipient_sms_gateway = os.getenv("RECIPIENT_SMS_GATEWAY") # I have T-Mobile
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
        print ("Text message sent successfully!")
    except Exception as e:
        print (f"Failed to send text: {e}")

if __name__ == "__main__":
    send_break_over_sms()        