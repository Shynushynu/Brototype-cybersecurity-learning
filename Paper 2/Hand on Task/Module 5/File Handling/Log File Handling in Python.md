# 📝 Log File Handling in Python

## 📌 Overview

Log file handling means storing and reading records of events that happen in a program.

For example, in a cybersecurity application, logs can record login attempts, errors, and suspicious activities.

## 📚 Table of Contents

- [1. What Is a Log File?](#1-what-is-a-log-file)
- [2. Do We Need a Library?](#2-do-we-need-a-library)
- [3. Reading a Log File](#3-reading-a-log-file)
- [4. Writing to a Log File](#4-writing-to-a-log-file)
- [5. Appending to a Log File](#5-appending-to-a-log-file)
- [6. Using Python's Logging Module](#6-using-pythons-logging-module)
- [7. Common Logging Levels](#7-common-logging-levels)
- [8. Cybersecurity Example](#8-cybersecurity-example)
- [9. Quick Revision](#9-quick-revision)
- [10. Practice Question](#10-practice-question)

---

## 1. What Is a Log File?

A **log file** is a text file that stores information about events that happen in a program.

Example: `app.log`

```text
Program started
User logged in successfully
Invalid password entered
File not found
```

## 2. Do We Need a Library?

It depends on what you want to do.

| Task | Required library |
|---|---|
| Read a log file | No extra library |
| Write to a log file | No extra library |
| Append records to a log file | No extra library |
| Automatically manage log levels and timestamps | `logging` (built-in) |

Python's `logging` module is built in, so you do not need to install it.

## 3. Reading a Log File

Suppose `app.log` contains:

```text
Program started
User logged in
An error occurred
```

Python code:

```python
with open("app.log", "r") as file:
    for line in file:
        print(line.strip())
```

### Explanation

- `open()` opens the file.
- `"r"` means read mode.
- `for line in file` reads the file one line at a time.
- `strip()` removes surrounding whitespace, including the newline at the end.

## 4. Writing to a Log File

```python
with open("app.log", "w") as file:
    file.write("Program started\n")
    file.write("User logged in\n")
```

**Important:** `"w"` means write mode. It overwrites existing contents if the file already exists.

## 5. Appending to a Log File

Appending means adding new records without deleting the old ones.

```python
with open("app.log", "a") as file:
    file.write("Invalid login attempt\n")
```

Here, `"a"` means append mode.

## 6. Using Python's Logging Module

The `logging` module is a standard way to create application logs.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("Suspicious login attempt")
logging.error("File not found")
```

### Example Output in `app.log`

```text
2026-10-12 18:10:00,000 - INFO - Program started
2026-10-12 18:10:01,000 - WARNING - Suspicious login attempt
2026-10-12 18:10:02,000 - ERROR - File not found
```

*Note: The timestamps are examples. Actual timestamps depend on when the records are created.*

## 7. Common Logging Levels

| Level | Purpose |
|---|---|
| `DEBUG` | Detailed information for debugging |
| `INFO` | Normal program events |
| `WARNING` | Something unexpected may happen |
| `ERROR` | An operation failed |
| `CRITICAL` | A serious problem |

## 8. Cybersecurity Example 🔐

Imagine monitoring login activity.

```python
import logging

logging.basicConfig(
    filename="security.log",
    level=logging.INFO
)

username = "admin"

logging.info(f"Login attempt for user: {username}")
logging.warning("Multiple failed login attempts detected")
```

This creates a record of security-related events.

**Security tip:** Never record passwords in log files.

## 9. Quick Revision

- **Read:** `"r"`
- **Write:** `"w"`
- **Append:** `"a"`
- **Basic file operations:** Built-in `open()`
- **Structured application logging:** `logging` module
- **Common log file extension:** `.log`

## 10. Practice Question

If you want to add a new failed-login message to `security.log` without deleting previous records, which mode should you use?

- A. `"r"`
- B. `"w"`
- C. `"a"`
