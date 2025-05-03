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
__________________________________
# School Uniform Compliance Directive.py Overview
This project serves as a tool for automating school uniform compliance reminders. The system sends regular reminders to students regarding the strict uniform policy enforced by the school. These emails are intended to ensure that all students meet the school's dress code and grooming standards without exception, contributing to a professional and disciplined learning environment. The school’s policy requires students to arrive in full formal uniform every Monday. This includes wearing the official shirt, trousers or skirt, approved belt and shoes, and ensuring grooming aligns with the institution's standards. Additionally, any unsanctioned social ideologies, including but not limited to Pride-related expressions, are strictly prohibited on school grounds. Any violations of this policy will lead to disciplinary actions. This project is NOT related or affiliated to the School Of Science and Technology, Singapore.

![image](https://github.com/user-attachments/assets/8e67b1b2-36a3-4c39-90d6-925a559d9a54)

The main goals of this project are as follows:
1. Ensure consistent uniform compliance by reminding students about the importance of following the school uniform guidelines consistently.
2. Automate the reminder process through hourly emails that help students prepare their uniforms and follow school rules.
3. Enforce strict policy adherence by emphasizing, in each reminder, that violations of the uniform code will result in immediate and formal disciplinary actions, with no appeals allowed.

(Key Features):
1. Automated email reminders are sent once every hour, ensuring that students stay informed about the uniform policy.
2. High-impact messaging is used to communicate the seriousness of compliance, leaving no room for excuses.
3. Compliance tracking can be configured to verify whether reminders are being sent and if the directive is being followed.
4. Strict disciplinary measures are clearly outlined in the emails, including item confiscation, demerits, privilege suspension, and referral to the disciplinary board.

(Automation Overview) How the System Works:
1. The system sends automated email reminders every hour to a designated recipient. Each message includes a reminder of the school’s uniform policy and potential consequences for violations. A Python script manages this process using the smtplib library for sending and the email.message library for formatting.
2. The script checks uniform compliance according to school standards and ensures reminders persist until the student complies.

(Email Template) Each reminder email contains:
1. A subject line warning about uniform compliance.
2. An introduction from the school outlining the formal compliance directive.
3.A breakdown of uniform and grooming requirements.
4. Consequences for non-compliance, such as confiscation, demerits, and privilege suspension.
5. A call to action encouraging students to prepare in advance.
6. A note advising students with genuine issues to contact Student Services beforehand.

![image](https://github.com/user-attachments/assets/0c58a467-614c-4da2-b274-939053fe15e6)

(Technical Details) The script includes:
1. Creation of email messages using the EmailMessage class.
2. SMTP connection to Gmail’s server with user credentials.
3. Cron job-based scheduling to send emails hourly.
4. Basic error handling for reliable operation.

(Running the Script) To run the script locally:
1. Ensure Python 3 is installed.
2. Install required libraries using:
pip install smtplib email
3. Edit the script with sender, recipient, and app password details.
- Make the script executable: chmod +x /path/to/your/script.py
4. What is a Cron Job?
A cron job is a time-based scheduler in Unix-like systems that automates the execution of scripts at set intervals.

1. How to Set Up a Cron Job on macOS
Step 1: Open Terminal
Launch Terminal from Applications > Utilities or by searching "Terminal".

Step 2: Set Default Text Editor to nano
Set nano as the default editor by entering:
export VISUAL=nano  
export EDITOR=nano

Step 3: Make the Python Script Executable
Run:
chmod +x "/Users/..."

Step 4: Open Crontab
Use the command:
crontab -e

Step 5: Add the Cron Job
To run the script hourly, add:
0 * * * * /usr/bin/python3 "/Users/..."

Step 6: Save and Exit
In nano, press Ctrl + O to save, then Enter, and Ctrl + X to exit.

Step 7: Confirm Cron Job
Check with:
crontab -l

Step 8: Test the Script
Wait until the next hour and check the email inbox to confirm.

_________________________________
Conclusion
You now have a functioning hourly cron job on macOS to run the uniform compliance reminder script. Update it at any time using crontab -e.
_________________________________
