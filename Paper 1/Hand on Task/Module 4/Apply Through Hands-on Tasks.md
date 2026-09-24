# 🛠️ 9. Apply Through Hands-on Tasks

This section focuses on **practicing Linux and cybersecurity skills through real-world tasks** rather than only learning theory.

---

## 🖥️ a. Administer Linux Systems

Practice managing a Linux system, including:

* Creating and managing users and groups
* Managing file permissions and ownership
* Installing and updating software
* Managing system services
* Monitoring system resources
* Managing processes
* Performing basic system troubleshooting

### Example

```bash
sudo systemctl status ssh
```

Checks the status of the SSH service.

---

## 🔍 b. Analyze Security Logs

Learn to examine logs to identify **authentication issues, suspicious activity, and security events**.

### Practice Tasks

* Check authentication logs
* Find failed login attempts
* Identify successful logins
* Search for suspicious commands or events
* Filter important log entries

### Example

```bash
grep "Failed password" /var/log/auth.log
```

Finds failed SSH login attempts on systems that use `auth.log`.

---

## 🐚 c. Build Shell Scripts

Create Bash scripts to automate repetitive tasks and perform security-related operations.

### Practice

* Variables
* Conditions
* Loops
* Functions
* User input
* Command execution
* Error handling

### Example

```bash
#!/bin/bash

echo "System Information"
hostname
uptime
```

---

## ⚙️ d. Automate Administrative Tasks

Use Bash scripts and Linux tools to automate routine administration tasks.

### Examples

* Create users automatically
* Backup files
* Clean temporary files
* Check disk usage
* Monitor services
* Generate system reports

### Example

```bash
#!/bin/bash

df -h > disk_report.txt
echo "Disk report created."
```

---

## 🛡️ e. Create Security Monitoring Scripts

Build scripts that check for security-related events periodically or continuously.

### Examples

* Monitor failed login attempts
* Check unusual user activity
* Monitor disk usage
* Check running processes
* Detect changes in important files
* Generate security reports

### Example

```bash
#!/bin/bash

echo "Failed login attempts:"
grep "Failed password" /var/log/auth.log
```

---

## 🔄 Hands-on Workflow

```text
Linux Administration
        ↓
Log Analysis
        ↓
Shell Scripting
        ↓
Task Automation
        ↓
Security Monitoring
        ↓
Practical Cybersecurity Skills
```

### 🎯 Goal

Build practical experience by using **Linux commands, Bash scripts, log analysis, and automation** to solve real administrative and security problems.
