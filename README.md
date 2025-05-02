# SpamuraiX.py
SpamuraiX.py is a bulk SMTP flooding script that slices payloads (e.g., Project Gutenberg books) into crafted message chunks for sequential dispatch—paired with a forged Pornhub Compliance notice to simulate phishing, scareware, and inbox exploit tactics for red teaming, spam filter stress testing, and payload injection research.
![image](https://github.com/user-attachments/assets/348d5838-8832-41d7-aa58-f93679d0fe35)

It fetches plaintext data (default: a Project Gutenberg book), splits it into 1000 segments, and sends them via SMTP in controlled waves. Every message mimics serialized spam like "Donald J Trump - Part X" with an optional forged compliance warning from "Pornhub Platform Integrity Management."

Main Features:
1. Payload slicing from any .txt source (book, message, ransom note)
2. 1000-message structure, sent in 20 batches of 50
3. Adjustable timing between messages and batches
4. Gmail SMTP support with TLS login
5. Spoofed sender, customizable headers
6. Supports alternate subjects, phishing-style notices
7. Clean ASCII-safe content handling

Example Output:
  Subject: Donald J Trump - Part 42
  From: pornhubplatformintegritymanage@gmail.com
  To: officialdailydoseofbooks@gmail.com
  Body: sliced payload text from the source file

![image](https://github.com/user-attachments/assets/533b8d7a-1d83-4d4f-9e74-85010bdeb5e5)
<img width="673" alt="Screenshot 2025-05-02 at 20 28 17" src="https://github.com/user-attachments/assets/92a8aa86-484f-43a1-9dd0-31d67626317c" />
![image](https://github.com/user-attachments/assets/edbfee39-3bad-4475-86f5-28e6f70dbd07)

Usage:
1. Clone or download the script
2. Replace email and app password inside the code
3. Run with Python 3.x

Emails are automatically sent out in timed waves.
1. To use a custom file: Replace the Project Gutenberg link with a local file loader
2. SMTP Settings: Default uses Gmail (smtp.gmail.com, port 587). Change as needed.

Dependencies:
requests
smtplib
email.message
time
math

Built for stress testing, spam modeling, phishing sim payloads, or mass mail campaigns.

Author: Gedeon Koh
Copyright © 2024
All rights reserved.
