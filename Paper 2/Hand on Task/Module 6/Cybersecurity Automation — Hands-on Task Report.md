# 🔐 Cybersecurity Automation — Hands-on Task Report

## 📌 Overview

This report documents five practical cybersecurity automation tasks using Python. The tasks cover log analysis, security monitoring, workflow automation, security report generation, and file integrity monitoring with email alerts.

**Overall Status:** Resources collected. Testing and implementation are pending.

## 📚 Table of Contents

- [1. Log Analysis Automation](#1-log-analysis-automation)
- [2. Security Monitoring Tool](#2-security-monitoring-tool)
- [3. Security Workflow Automation](#3-security-workflow-automation)
- [4. Automated Security Report Generation](#4-automated-security-report-generation)
- [5. File Integrity Monitoring and Email Alerts](#5-file-integrity-monitoring-and-email-alerts)
- [6. Overall Progress](#6-overall-progress)

---

## 1. Log Analysis Automation

### 🎯 Objective

Develop a Python script that reads security logs, identifies important events, counts failed login attempts, extracts IP addresses, and detects suspicious patterns.

### 🛠️ Tools and Libraries

- `re` — Extract IP-like patterns using regular expressions.
- `collections.Counter` — Count failed login attempts.
- `open()` — Read the log file.

### 💻 Code

```python
import re
from collections import Counter

failed_logins = Counter()
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

with open("security.log", "r") as file:
    for line in file:

        ips = re.findall(ip_pattern, line)

        if "Failed login" in line:
            for ip in ips:
                failed_logins[ip] += 1

        if "Successful login" in line:
            print("Successful login:", line.strip())

        if "ERROR" in line:
            print("Error detected:", line.strip())

print("\nFailed login attempts:")
for ip, count in failed_logins.items():
    print(ip, ":", count)

print("\nSuspicious IP addresses:")
for ip, count in failed_logins.items():
    if count >= 3:
        print(ip, "has", count, "failed attempts")
```

### 📄 Expected Results

- Display successful login entries.
- Display error entries.
- Count failed login attempts for each IP address.
- Flag IP addresses with three or more failed login attempts.

**Status:** Resource collected; testing pending.

---

## 2. Security Monitoring Tool

### 🎯 Objective

Create a Python script that repeatedly checks a security log file for failed login attempts and unauthorized access events.

### 🛠️ Tools and Libraries

- `time` — Wait between monitoring checks.
- `open()` — Read the log file.
- Conditional statements — Identify suspicious events.

### 💻 Code

```python
import time

log_file = "security.log"
check_interval = 10

while True:
    with open(log_file, "r") as file:
        for line in file:
            if "Failed login" in line or "Unauthorized access" in line:
                print("Suspicious event detected:", line.strip())

    print("Next check in 10 seconds...")
    time.sleep(check_interval)
```

### 📄 Expected Results

- Read the security log repeatedly.
- Detect failed login attempts.
- Detect unauthorized access entries.
- Display matching events in the terminal.
- Wait 10 seconds before the next check.

**Status:** Resource collected; testing pending.

**Note:** This version rereads the entire file each time, so old events may appear repeatedly. It also runs continuously until stopped.

---

## 3. Security Workflow Automation

### 🎯 Objective

Design an automated security workflow that collects logs, extracts useful information, detects suspicious activity, records incidents, generates reports, and sends notifications.

### 🔄 Workflow

| Step | Stage | Description | Python Tools |
|---|---|---|---|
| 1 | Log Collection | Read security logs | `open()` |
| 2 | Log Parsing | Extract IP addresses and event details | `re`, `split()` |
| 3 | Event Detection | Identify suspicious activity | `if`, `Counter` |
| 4 | Incident Recording | Store incident information | Lists, dictionaries |
| 5 | Report Generation | Summarize security events | `csv`, `json` |
| 6 | Alert Notification | Notify the administrator | `smtplib`, `email` |

### 🔗 Workflow Sequence

Collect Logs → Parse Entries → Detect Suspicious Events → Record Incidents → Generate Reports → Send Alerts

### 💻 Implementation Status

This task currently contains the workflow design rather than a separate implementation script. The other tasks provide starting components that can later be integrated into a complete workflow.

**Status:** Workflow designed; implementation pending.

---

## 4. Automated Security Report Generation

### 🎯 Objective

Create a Python script that generates a security incident report containing the generation time, incident description, severity, and status.

### 🛠️ Tools and Libraries

- `datetime` — Obtain the current date and time.
- File handling — Write the report to a text file.
- Formatted strings — Insert information into the report.

### 💻 Code

```python
from datetime import datetime

report = f"""
SECURITY INCIDENT REPORT
------------------------
Generated: {datetime.now()}
Incident: Multiple failed login attempts
Severity: High
Status: Open
"""

with open("security_report.txt", "w") as file:
    file.write(report)

print("Security report generated.")
```

### 📄 Expected Results

The script creates `security_report.txt` with the following information:

- Report title.
- Generation timestamp.
- Incident description.
- Severity level.
- Incident status.

**Status:** Resource collected; testing pending.

**Note:** The incident description, severity, and status are currently fixed values. They are not yet calculated from actual log analysis.

---

## 5. File Integrity Monitoring and Email Alerts

### 🎯 Objective

Develop a monitoring utility that calculates the SHA-256 hash of a security log file, detects file modifications, and sends an email alert when a change occurs.

### 🛠️ Tools and Libraries

- `hashlib` — Calculate the file's SHA-256 hash.
- `time` — Schedule repeated checks.
- `smtplib` — Send email notifications.
- `ssl` — Secure the SMTP connection.
- `EmailMessage` — Construct the email.
- `csv` — Read email credentials from a CSV file.

### 💻 Code

```python
import smtplib
import ssl
import time
from email.message import EmailMessage
import hashlib
import csv

def sendMail(subject, body):
    with open("mailPass.csv", "r", newline="") as file:
        data = csv.reader(file)
        for i in data:
            sender = i[0]
            appPassword = i[1]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = sender
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=context, timeout=10
        ) as server:
            server.login(sender, appPassword)
            server.send_message(msg)

        print("Alert!!! File has been modified... Email sent successfully.")

    except (smtplib.SMTPException, OSError) as error:
        print("Process Failed:", error)


filePath = "security.log"

def CalculateHash(filePath):
    Hash = hashlib.sha256()

    with open(filePath, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            Hash.update(data)

    HashVal = Hash.hexdigest()
    return HashVal


try:
    OrginalHash = CalculateHash(filePath)
    print("File Monitoring started..")

    while True:
        time.sleep(5)
        CurrentHash = CalculateHash(filePath)

        if OrginalHash != CurrentHash:
            sendMail(
                "Alert!!!",
                "File has been modified.."
            )
            OrginalHash = CurrentHash

        else:
            print("File is unchanged")

except FileNotFoundError:
    print(f"File: {filePath} not found")

except KeyboardInterrupt:
    print("Monitoring Stopped")
```

### 📁 Required Files

- `security.log` — The file being monitored.
- `mailPass.csv` — Contains the sender's email address and app password.
- Python script — Performs file integrity monitoring and sends alerts.

### 📄 Expected Results

- Calculate the initial SHA-256 hash.
- Check the file every five seconds.
- Compare the current hash with the previous hash.
- Send an email alert if a modification is detected.
- Display whether the file is unchanged.
- Stop monitoring when interrupted by the user.

**Status:** Resource collected; testing pending.

**Security Note:** Protect the credentials in `mailPass.csv`. Never upload a file containing real passwords to GitHub. This script sends an alert to the same email address used as the sender.

---



## 6. Additional project
### nMap Project
### 💻 Code

```python
import socket 

while True:
    url=str(input("Enter the url or the ip address(eg:google.com):")).strip()
    if not url:
        print("Enter a url or an ip:")
        continue
    try:
        ip=socket.gethostbyname(url)
        print("ip address resolved ",ip)
        break
    except socket.gaierror:
        print("unalble to resolve host name...")

while True:
    try:
        start=int(input("enter the staring port number:"))
        if not 1<= start <=65535:
            print("enter a vaild port number")
        else:
            print("port number accepted sucessfully......")
            break
    except ValueError:
        print("enter and integer")
  
while True:
    try:
        end=int(input("Enter the ending port number:"))
        if not 1<= end <=65535:
            print("enter a vaild port number")
        elif start>end:
            print("Error occured....End port is smaller than start...")
        else:
            print("port number accepted sucessfully....")
            break
    except ValueError:
        print("enter and integer")


openports=0
close=0
timeout=0
total=0
countError=0
openlist=[]
for port in range(start,end+1):
    try:
        client=socket.socket()
        client.settimeout(3)
        client.connect((ip,port))
        print(f"port {port} is open")
        openports+=1
        openlist.append(port)
    except socket.timeout:
        print(f"time out on port {port}")
        timeout+=1
    except ConnectionRefusedError:
        print(f"connection refused on {port}")
        close+=1
    except OSError as error:
        print(f"socket error on port {port}:{error}")
        
    
    finally:
        total+=1
        client.close()


print("\n" + "=" * 45)
print("             TCP PORT SCAN REPORT")
print("=" * 45)

print(f"Total Ports Checked : {total}")
print(f"Open Ports          : {openports}")
print(f"Closed Ports        : {close}")
print(f"Connection Timeouts : {timeout}")
print(f"Errors Occurred     : {countError}")

print("-" * 45)

if not openlist:
    print("No usable ports found!")
else:
    print("Usable Ports:")
    for port in openlist:
        print(f"  [+] Port {port}")

print("=" * 45)
print("              SCAN COMPLETED")
print("=" * 45)

```

## 🎯 Next Steps

1. Test the log analysis script with sample security logs.
2. Run the monitoring tool and observe its output.
3. Implement the complete security automation workflow.
4. Generate and verify the security report.
5. Test file integrity monitoring and email notifications.
6. Document errors, fixes, and final results for each task.

**Final Note:** The report contains the supplied code and workflow design. The code has not been tested or modified as part of this report.
