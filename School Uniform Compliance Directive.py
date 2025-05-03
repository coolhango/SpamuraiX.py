#!/usr/bin/env python
# coding: utf-8

# In[4]:


import smtplib
from email.message import EmailMessage
import sys
import time

def create_message(sender_email, recipient_email, recipient_name, i):
    """Creates a strict and official school uniform reminder email message."""
    msg = EmailMessage()
    msg['Subject'] = f'⚠️ Official School Uniform Compliance Directive {i}'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    body = f"""Dear {recipient_name},

⚠️ This is a FINAL COMPLIANCE DIRECTIVE issued by the SST Discipline & Compliance Office.  

This communication serves as a high-priority reminder that all students are required to report to school on Monday in full formal school uniform, without exception. This includes:

- Official SST regulation shirt (tucked in)  
- SST trousers/skirt (no alterations)
- SST-approved belt and shoes  
- School tie (if mandated by level)  
- Grooming in line with institutional standards  

Failure to comply with any of the above is a direct violation of school policy and will not be tolerated. There will be no verbal reminders on Monday morning. Additionally, any display—whether through attire, accessories, or conduct—of unsanctioned social ideologies, including Pride-related expressions, is strictly prohibited on school grounds. Violations will result in immediate confiscation of offending items, formal demerit entries, suspension of student privileges, and may escalate to disciplinary board review for repeated noncompliance. This directive is non-negotiable and will be enforced without exception.

📣 If you ignore this and arrive in improper attire, disciplinary actions will be immediate and formal. No appeals will be entertained for claims of ignorance or forgetfulness.
✅ Prepare your uniform tonight. Lay out every required item. Double-check compliance.  
🕗 You are expected to arrive on time, fully attired, and visibly aligned with SST standards.

If you are facing genuine difficulty or require assistance, you must inform the Student Services Office before the end of Sunday. Silence will be treated as acknowledgement of your ability to comply.

Respectfully,  
SST School Discipline & Compliance Office 
sstuniformcompliance@gmail.com
"""
    msg.set_content(body)
    return msg

def send_uniform_reminder(sender_email, app_password, recipient_email, recipient_name, reminder_number, count=1):
    """Sends the reminder email 'count' number of times with short intervals."""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender_email, app_password)

            for i in range(count):
                msg = create_message(sender_email, recipient_email, recipient_name, f"{reminder_number}.{i+1}")
                smtp.send_message(msg)
                print(f"Reminder {reminder_number}.{i+1} sent to {recipient_email}")
                if i < count - 1:
                    time.sleep(1)  # 1 second between emails
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# === CONFIG ===
SENDER_EMAIL = 'sstuniformcompliance@gmail.com'
APP_PASSWORD = 'ldnj vanc vlyx cvyr'
RECIPIENT_EMAIL = 'officialdailydoseofbooks@gmail.com'
RECIPIENT_NAME = 'Barna Shogh'

NUM_EMAILS_PER_HOUR = 1
COUNT = NUM_EMAILS_PER_HOUR

REMINDER_NUMBER = 1

send_uniform_reminder(SENDER_EMAIL, APP_PASSWORD, RECIPIENT_EMAIL, RECIPIENT_NAME, REMINDER_NUMBER, COUNT)


# In[ ]:




