# SpamuraiX.py
SpamuraiX.py is a bulk SMTP flooding script that slices payloads (e.g., Project Gutenberg books) into crafted message chunks for sequential dispatch—paired with a forged Pornhub Compliance notice to simulate phishing, scareware, and inbox exploit tactics for red teaming, spam filter stress testing, and payload injection research. 

This is an updated iteration of the Bulk Email Exploitation Framework (BEEF), now in its second version. This release addresses and resolves several issues identified in earlier versions, including improved error handling, enhanced performance, and better stability. These fixes ensure that the framework operates more efficiently and securely, enhancing the user experience while maintaining its intended educational and research purposes.

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
1. Clone or download the script: First, grab the script by either cloning the GitHub repository or downloading the .zip file. ![image](https://github.com/user-attachments/assets/2eec748b-4edb-4fd0-922c-467caf1ff698)

2. Replace email and app password inside the code: In order to authenticate with Gmail's SMTP server, you’ll need to provide a valid email address and an App Password instead of your regular Gmail password. Google requires the use of App Passwords if you have 2-Factor Authentication (2FA) enabled on your Google account. App passwords are a special type of one-time   password designed specifically for use with apps or scripts like Spamurai.py, allowing you to log in to your Google account without exposing your primary password. This adds an extra layer of security and prevents unauthorized access. If you don’t have 2FA enabled, you can use your standard Gmail password, but it’s strongly recommended to enable 2FA for added security.
3. Run the script: Once your email and app password are configured in the script, simply run it using Python. The script will handle sending emails in batches, using the credentials you provided, while following the specified timings.
   
<img width="519" alt="Screenshot 2025-05-02 at 20 30 07" src="https://github.com/user-attachments/assets/61b3406a-6fe8-4746-a114-107812208575" />
<img width="304" alt="Screenshot 2025-05-02 at 20 30 23" src="https://github.com/user-attachments/assets/2e00288c-7fb0-48e7-a188-163c8209a119" />

How to generate an App Password: https://support.google.com/accounts/answer/185833?hl=en
1. Go to your Google account settings.
2. Under "Security," find "App Passwords" and click on it.
3. Follow the prompts to create a new App Password. Choose “Mail” as the app and “Other” for the device (you can name it anything you want, e.g., “Spamurai”).
4. Google will generate a 16-character app password that you’ll input into the script in place of your regular Gmail password.

Emails are automatically sent out in timed waves.
1. To use a custom file: Replace the Project Gutenberg link with a local file loader
2. SMTP Settings: Default uses Gmail (smtp.gmail.com, port 587). Change as needed.

<img width="590" alt="Screenshot 2025-05-02 at 20 33 02" src="https://github.com/user-attachments/assets/824275e7-ce72-44ae-a887-ed0a80a423c0" />
<img width="252" alt="Screenshot 2025-05-02 at 20 32 52" src="https://github.com/user-attachments/assets/2c6be270-a00f-44b7-96b7-943c6f0aa70c" />

Dependencies:
requests
smtplib
email.message
time
math

Known Issues and Limitations:
1. No Stop Mechanism: The script does not currently provide an in-built method for stopping or pausing the process once it's initiated. If you need to halt the execution, you will need to manually terminate the process (e.g., by pressing Ctrl + C).
2. SMTP Provider Limitation: The script is specifically configured to work with Gmail’s SMTP server. To use a different email provider, users will need to modify the SMTP settings accordingly.

![image](https://github.com/user-attachments/assets/3749148b-03b1-465f-b621-a956d8291b8d)

__________________________________
![image](https://github.com/user-attachments/assets/dc982fab-30bb-4b4b-853b-19e30bb652fe)

Disclaimer:
This script is intended solely for educational purposes and must be used responsibly. It is strictly prohibited to use the script for pranks, harassment, or to send unsolicited emails to individuals or organizations without their consent. Any misuse of this script may result in legal consequences and violations of the terms of service of email providers, such as Gmail. Engaging in spamming or any other non-consensual activities can lead to account suspensions, blacklisting, or more severe legal actions. It is imperative to ensure that all activities conducted with this script adhere to ethical standards and comply with applicable laws and regulations. This repository and its contents are provided to demonstrate the principles of email flooding and payload delivery systems within controlled, ethical testing environments. The use of this script on live targets or for malicious purposes is strictly prohibited. Users assume full responsibility for any consequences resulting from the use of this script.

__________________________________
Built for intense stress testing, spam modeling, phishing sim payloads, or mass mail campaigns.

Author: Gedeon Koh
Copyright © 2025
All rights reserved.

Contributions ✨: We welcome contributions to improve the functionality and usability of this script. If you have identified bugs, security improvements, or new features, feel free to fork the repository and submit a pull request. Please ensure that all contributions follow ethical guidelines and are in line with the educational nature of the project. If you're unsure about any changes, please open an issue to discuss it first. Contributions should adhere to coding standards and include appropriate documentation for any new features or changes.

Other Random Information: No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in reviews and certain other non-commercial uses permitted by copyright law. THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR OR COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE Any unauthorized use or dissemination of the results produced by this program is unethical and may result in legal consequences. Any damage, disciplinary actions or death from this material is not in fault in the publisher's or owner.
