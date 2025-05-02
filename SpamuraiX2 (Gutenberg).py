#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Last Updated: 2 May 2025
# Copyright © 2024 Gedeon Koh All rights reserved.

import requests
from math import floor
import time
import smtplib
from email.message import EmailMessage

# Book source: Use plain-text version to avoid HTML tag mess
book_url = 'https://www.gutenberg.org/files/66251/66251-0.txt'
r = requests.get(book_url)
book_data = r.text.encode('ascii', 'ignore').decode('ascii')

# Split book into words
word_list = book_data.split(" ")
msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)

print(f"Words per message: {msg_size}\nFinal message size: {final_msg_size}")

# Email credentials (Ensure App Passwords are enabled in Google)
user = ''
password = ''
fr_address = user
to_address = ''
smtp_host = 'smtp.gmail.com'
smtp_port = 587

subject = 'XXX - Part '

msg_count = 0

# Send 20 batches of 50 emails (1000 emails total)
for batch in range(20):
    server = smtplib.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(user=user, password=password)

    for i in range(50):
        # Prepare message content
        if msg_count == 999:
            start_pos = len(word_list) - final_msg_size
            msg_text = ' '.join(word_list[start_pos:])
        else:
            start_pos = msg_count * msg_size
            msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])

        # Create HTML-safe email
        msg = EmailMessage()
        msg['From'] = fr_address
        msg['To'] = to_address
        msg['Subject'] = subject + str(msg_count + 1)
        msg.set_content(msg_text)  # plain text is fine for .txt books
        # msg.set_content(f"<p>{msg_text}</p>", subtype='html')  # use this for HTML books

        server.send_message(msg)
        msg_count += 1

        # Delay between messages
        time.sleep(0.5)

    # Delay between batches
    time.sleep(20)
    server.quit()


# In[ ]:




