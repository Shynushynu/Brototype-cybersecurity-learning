# 🔐 Python System Monitoring & Automated Gmail Alert Project

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🛠️ Technologies Used](#️-technologies-used)
- [📂 Project Structure](#-project-structure)
- [1️⃣ Understanding File Integrity Monitoring](#1️⃣-understanding-file-integrity-monitoring)
- [2️⃣ Understanding the Gmail Alert Workflow](#2️⃣-understanding-the-gmail-alert-workflow)
- [3️⃣ Configuring Gmail Credentials](#3️⃣-configuring-gmail-credentials)
- [4️⃣ Testing Gmail SMTP Connectivity](#4️⃣-testing-gmail-smtp-connectivity)
- [5️⃣ Creating `test_email.py`](#5️⃣-creating-test_emailpy)
- [6️⃣ Integrating Gmail Alerts into `monitor.py`](#6️⃣-integrating-gmail-alerts-into-monitorpy)
- [7️⃣ Testing the Complete Project](#7️⃣-testing-the-complete-project)
- [8️⃣ Current Project Progress](#8️⃣-current-project-progress)
- [🚀 Future Improvements](#-future-improvements)
- [📚 What I Learned](#-what-i-learned)
- [🏁 Conclusion](#-conclusion)

  
## 📌 Project Overview

This project uses Python to monitor file changes and send email alerts when a monitored file is modified.

It combines file integrity monitoring with automated email notifications to demonstrate a basic security monitoring workflow.

### 🎯 Project Objectives

- Monitor a file for unexpected changes.
- Calculate SHA-256 hashes to identify file modifications.
- Configure Gmail for automated email notifications.
- Test Gmail SMTP connectivity and authentication.
- Integrate email alerts with the file monitoring program.
- Understand how monitoring and alerting work in cybersecurity.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| `hashlib` | Calculate SHA-256 file hashes |
| `os` | Read environment variables |
| `smtplib` | Connect to Gmail SMTP |
| `ssl` | Secure the SMTP connection |
| `email.message` | Create email messages |
| Gmail | Deliver email alerts |
| VS Code | Development environment |
| Windows | Operating system |

---

## 📂 Project Structure

The project can be organized as follows:

```text
Python-Security-Monitor/
│
├── monitor.py
├── test_email.py
└── security.log
```

**File descriptions:**

- `monitor.py` — Monitors the target file and detects changes using SHA-256. Gmail alert integration is the next step.
- `test_email.py` — Tests Gmail authentication and email delivery.
- `security.log` — The file being monitored for changes.

---

## 1️⃣ Understanding File Integrity Monitoring

File integrity monitoring checks whether a file has changed by comparing its current state with a previously recorded state.

For this project, we use the SHA-256 hashing algorithm.

### What is SHA-256?

SHA-256 is a cryptographic hash function that generates a 256-bit hash value, usually represented as 64 hexadecimal characters.

Even a small change in a file's contents will normally produce a different hash.

For example:

```text
Original file hash:
a1b2c3...

Modified file hash:
x9y8z7...
```

*These are illustrative examples, not actual SHA-256 results.*

### How change detection works

1. Read the file's contents.
2. Calculate its SHA-256 hash.
3. Store the initial hash.
4. Calculate the hash again during monitoring.
5. Compare the current hash with the previous hash.
6. If the hashes differ, report that the file has changed.

**Important:** A hash comparison detects content changes, not necessarily every filesystem change. Changes to permissions or timestamps alone may not change the file's content hash.

---

## 2️⃣ Understanding the Gmail Alert Workflow

The email alert system notifies the user when the monitoring program detects a file change.

### Alert workflow

```text
File Monitoring
      |
      v
Calculate SHA-256 Hash
      |
      v
Compare Hash Values
      |
      v
File Changed?
      |
      +---- No ----> Continue Monitoring
      |
      +---- Yes ---> Prepare Alert
                         |
                         v
                   Connect to Gmail
                         |
                         v
                   Authenticate
                         |
                         v
                    Send Email
```

The email integration must be connected to the existing file-change detection condition so alerts are sent only when a change is detected.

---

## 3️⃣ Configuring Gmail Credentials

The project uses two Windows environment variables to store the email credentials separately from the Python source code.

### Environment variables

| Variable | Purpose |
|---|---|
| `ALERT_EMAIL` | Gmail account used to send alerts |
| `ALERT_PASSWORD` | Gmail App Password |

### Step 1: Create a Gmail App Password

1. Open [Google App Passwords](https://myaccount.google.com/apppasswords).
2. Sign in to the relevant Google Account.
3. Ensure 2-Step Verification is enabled.
4. Create an App Password for the Python monitoring project.
5. Store the generated password securely.

An App Password is different from the normal Gmail account password. App Password availability depends on the account's security configuration.

### Step 2: Configure environment variables in Windows

Open Command Prompt and run:

```cmd
setx ALERT_EMAIL "your_email@gmail.com"
setx ALERT_PASSWORD "your_16_character_app_password"
```

Replace the example values with your own credentials.

**Security precautions:**

- Never publish your App Password on GitHub.
- Never share your credentials in screenshots or source code.
- Do not commit a `.env` file containing real credentials.
- If a credential is accidentally exposed, revoke it and generate a replacement.

### Step 3: Verify the variables

Open a new VS Code terminal and run:

```python
import os

print("Email configured:", bool(os.getenv("ALERT_EMAIL")))
print("Password configured:", bool(os.getenv("ALERT_PASSWORD")))
```

Expected output:

```text
Email configured: True
Password configured: True
```

This verifies that both environment variables are available without printing their actual values.

---

## 4️⃣ Testing Gmail SMTP Connectivity

SMTP stands for **Simple Mail Transfer Protocol**. It is used to send email messages between mail systems.

During troubleshooting, we checked connectivity to these Gmail SMTP ports:

| Port | Connection type | Test result |
|---|---|---|
| 465 | SMTP over SSL/TLS | Reachable |
| 587 | SMTP with STARTTLS | Reachable |

Both ports were reachable during our earlier connectivity test.

### Understanding the SMTP response

We also received this server response:

```text
250 2.0.0 OK
```

This indicates that Gmail accepted the particular SMTP command and reported success for that step.

It does not, by itself, prove that the complete email-sending process succeeded. Authentication, message submission, and delivery must be verified separately.

---

## 5️⃣ Creating `test_email.py`

We created a separate Python script to test Gmail authentication and email delivery before integrating it into the monitoring program.

The script uses:

- `os.getenv()` to retrieve environment variables.
- `EmailMessage` to construct the email.
- `SMTP_SSL()` to establish a secure connection to Gmail.
- `server.login()` to authenticate.
- `server.send_message()` to submit the email.

### SMTP configuration

```python
with smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465,
    context=ssl.create_default_context(),
    timeout=10
) as server:
    server.login(sender_email, app_password)
    server.send_message(message)
```

This configuration uses Gmail's SMTP server over SSL on port 465.

### Running the test

```cmd
python test_email.py
```

A successful test prints:

```text
Email sent successfully!
```

We then confirmed that the Gmail test was completed. This establishes the test-email stage as completed in our project workflow.

---

## 6️⃣ Integrating Gmail Alerts into `monitor.py`

The next development step is to connect the email function to the existing SHA-256 file monitoring logic.

### Required imports

```python
import os
import smtplib
import ssl
from email.message import EmailMessage
```

Keep any existing imports, including `hashlib`, that your monitoring program already uses.

### Email alert function

```python
def send_email_alert(subject, body):
    sender_email = os.getenv("ALERT_EMAIL")
    app_password = os.getenv("ALERT_PASSWORD")

    if not sender_email or not app_password:
        print("Email credentials are not configured.")
        return

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = sender_email
    message.set_content(body)

    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            context=context,
            timeout=10
        ) as server:
            server.login(sender_email, app_password)
            server.send_message(message)

        print("Email alert sent successfully!")

    except (smtplib.SMTPException, OSError) as error:
        print("Failed to send email alert:", error)
```

### Calling the function after detecting a change

Inside the existing file-change detection condition, add:

```python
send_email_alert(
    "Security Alert: File Changed",
    "A change was detected in security.log."
)
```

This call should run only when the monitoring program detects a change.

**Integration status:** The alert function and the proposed integration call have been prepared. The complete integration into the user's existing `monitor.py` still needs to be performed and tested.

---

## 7️⃣ Testing the Complete Project

After integration, perform the following tests.

| Test | Expected result |
|---|---|
| Start monitoring an unchanged file | No change alert |
| Modify the contents of `security.log` | Change detected |
| Change the file and allow the monitor to check again | Email alert sent |
| Temporarily use invalid credentials in a controlled test | Authentication failure reported |
| Stop and restart the monitor | Initial hash is established again |

For reliable testing, ensure the monitoring loop has enough time to detect the change. Avoid deliberately exposing real credentials while testing errors.

### Important implementation details

- The monitor should establish a baseline hash before checking for subsequent changes.
- If the file changes repeatedly, the program should update its stored hash after detection.
- A simple polling loop may send repeated alerts if the hash is not updated.
- A network failure should not silently terminate the monitoring program.
- Restarting the program may establish a new baseline, so changes made while it was stopped may not be reported.

---

## 8️⃣ Current Project Progress

| Task | Status |
|---|---|
| Understand SHA-256 file change detection | Completed previously |
| Create the file monitoring program | Existing `monitor.py` |
| Configure Gmail environment variables | Completed |
| Test Gmail SMTP connectivity | Completed |
| Run the Gmail email test | Completed |
| Prepare the email alert function | Prepared |
| Integrate the function into existing change detection | Pending |
| Test a real file change and email alert | Pending |
| Handle repeated alerts and failures | Pending |

---

## 🚀 Future Improvements

Once the basic project works, it can be extended with:

1. **System monitoring:** Monitor CPU, memory, and disk usage with `psutil`.
2. **Service monitoring:** Check whether important system services are running.
3. **Log analysis:** Detect selected security-related events in log files.
4. **Alert categorization:** Assign severity levels to different events.
5. **Automated reporting:** Generate JSON or CSV reports.
6. **Reliable monitoring:** Add logging, exception handling, and configurable polling intervals.
7. **Alert control:** Prevent repeated emails for the same unchanged condition.

These are future enhancements and are not yet confirmed as implemented.

---

## 📚 What I Learned

Through this project, I am learning how to:

- Use cryptographic hashes for file integrity monitoring.
- Automate file monitoring with Python.
- Configure environment variables in Windows.
- Use SMTP to send email notifications.
- Authenticate securely with Gmail using an App Password.
- Handle network and email-related exceptions.
- Connect event detection with an automated alerting workflow.
- Build practical cybersecurity automation tools.

---

## 🏁 Conclusion

The project combines Python file integrity monitoring with Gmail-based alerting. The SHA-256 monitoring logic already exists, the Gmail credentials have been configured, and the email test has been completed.

The next milestone is to integrate the alert function into the existing `monitor.py`, then verify that modifying `security.log` automatically triggers a real email notification.

**Project goal:** Detect a file change, identify the event, and notify the user automatically.
