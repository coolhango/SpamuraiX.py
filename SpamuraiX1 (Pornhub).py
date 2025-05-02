#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib
from email.message import EmailMessage
import time

def create_message(sender_email, recipient_email, recipient_name, i):
    """Creates a personalized email message."""
    msg = EmailMessage()
    msg['Subject'] = f'Official Warning Regarding Prohibited Content Activity ⚠️ Warning {i+1}'  # Use the incremented value of i
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    body = f"""Dear {recipient_name},

We are contacting you in connection with a serious breach of our platform’s acceptable use policies.

Our monitoring systems have identified search activity on your account that includes terms or content which may involve the sexual exploitation of minors. We must emphasize that any form of child sexual abuse material (CSAM) is strictly illegal, gravely unethical, and absolutely prohibited on Pornhub. The possession, distribution, or solicitation of such material constitutes a federal crime and is subject to criminal prosecution.

This email serves as an official warning. Continued violations will result in immediate termination of access to our services and referral to the appropriate law enforcement authorities.

We urge you to immediately cease all prohibited activity. Your full compliance with our platform’s Terms of Service and with applicable local, national, and international laws is mandatory.

Please acknowledge receipt of this warning by replying to this email with the word "Received." If you believe this message was sent in error, or if your account may have been compromised, please report this immediately via the official Pornhub Support Page.

Sincerely,
Pornhub Compliance & Investigations Team
"""
    msg.set_content(body)
    return msg

def send_multiple_emails(sender_email, app_password, recipient_email, recipient_name, num_emails):
    """Sends a specified number of emails to a recipient."""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender_email, app_password)

            for i in range(num_emails):
                # Re-create the message inside the loop with the correct warning number
                message = create_message(sender_email, recipient_email, recipient_name, i)
                smtp.send_message(message)
                print(f"[{i+1}] Email sent to {recipient_email}")
                time.sleep(1)  # 1 second pause between emails

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# === USER INPUT SECTION ===

# 🛑 Use dummy or test accounts only. DO NOT use this for pranks, threats, or non-consensual testing.
SENDER_EMAIL = ''
APP_PASSWORD = ''
RECIPIENT_EMAIL = ''
RECIPIENT_NAME = ''
NUM_EMAILS_TO_SEND = 500

# === Run the function ===
send_multiple_emails(SENDER_EMAIL, APP_PASSWORD, RECIPIENT_EMAIL, RECIPIENT_NAME, NUM_EMAILS_TO_SEND)

