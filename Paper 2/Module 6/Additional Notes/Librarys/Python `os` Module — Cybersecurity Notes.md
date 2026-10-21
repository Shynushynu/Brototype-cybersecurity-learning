# 🐍 Python `os` Module — Cybersecurity Notes

## 📚 Table of Contents

- [🎯 1. Overview](#-1-overview)
- [📌 2. Functions List](#-2-functions-list)
- [📂 3. File and Directory Management](#-3-file-and-directory-management)
- [🔎 4. Path Checking Functions](#-4-path-checking-functions)
- [🛡️ 5. System and Process Information](#️-5-system-and-process-information)
- [🔐 6. Directory Traversal Using `os.walk()`](#-6-directory-traversal-using-oswalk)
- [🚨 7. Practical Cybersecurity Example](#-7-practical-cybersecurity-example)
- [🧠 8. Important Differences](#-8-important-differences)
- [🎤 9. Interview Answer](#-9-interview-answer)

---

## 🎯 1. Overview

The `os` module is a built-in Python module that allows Python programs to interact with the operating system.

It helps manage files, directories, environment variables, paths, and operating-system processes.

In cybersecurity, the `os` module is useful for log processing, file monitoring, security automation, and managing system resources.

### 📦 Importing the Module

The `os` module comes built into Python, so you do not need to install it.

```python
import os
```

---

## 📌 2. Functions List

### 📂 File and Directory Functions

| Function | Definition |
|---|---|
| `os.getcwd()` | Returns the current working directory. |
| `os.chdir()` | Changes the current working directory. |
| `os.listdir()` | Lists files and directories in a location. |
| `os.mkdir()` | Creates a single directory. |
| `os.makedirs()` | Creates directories, including missing parent directories. |
| `os.rmdir()` | Removes an empty directory. |
| `os.remove()` | Deletes a file. |
| `os.rename()` | Renames or moves a file or directory. |
| `os.walk()` | Traverses a directory tree. |

### 🔎 Path Functions

| Function | Definition |
|---|---|
| `os.path.exists()` | Checks whether a path exists. |
| `os.path.isfile()` | Checks whether a path points to a file. |
| `os.path.isdir()` | Checks whether a path points to a directory. |
| `os.path.join()` | Combines path components using the correct separator. |
| `os.path.getsize()` | Returns the size of a file in bytes. |

### 🛡️ System and Process Functions

| Function | Definition |
|---|---|
| `os.stat()` | Retrieves file or directory metadata. |
| `os.environ` | Provides access to environment variables. |
| `os.getenv()` | Retrieves an environment variable. |
| `os.cpu_count()` | Returns the number of logical CPUs, when available. |
| `os.getpid()` | Returns the current process ID. |
| `os.system()` | Executes a command through the operating system's command processor. |

---

## 📂 3. File and Directory Management

### A. `os.getcwd()`

Returns the current working directory.

```python
import os

print(os.getcwd())
```

**Example output:**

```text
C:\Users\Student\Documents
```

**Use:** Find the directory in which your Python program is working.

### B. `os.chdir()`

Changes the current working directory.

```python
import os

os.chdir("C:\\Temp")

print(os.getcwd())
```

**Use:** Work with files relative to a different directory.

### C. `os.listdir()`

Lists files and directories inside a specified directory.

```python
import os

files = os.listdir("C:\\Temp")

for file in files:
    print(file)
```

**Use:** Identify files in a directory during security investigations or automated file processing.

### D. `os.mkdir()`

Creates a single directory.

```python
import os

os.mkdir("security_logs")
```

The directory must not already exist, and its parent directory must exist.

### E. `os.makedirs()`

Creates a directory and any missing parent directories.

```python
import os

os.makedirs("security/reports/daily", exist_ok=True)
```

The `exist_ok=True` argument prevents an error if the target directory already exists.

### F. `os.remove()`

Deletes a file.

```python
import os

os.remove("old_log.txt")
```

⚠️ **Warning:** Check the file path before deleting anything.

### G. `os.rename()`

Renames a file or directory, or moves it to another location when supported.

```python
import os

os.rename("old_report.txt", "new_report.txt")
```

### H. `os.rmdir()`

Removes an empty directory.

```python
import os

os.rmdir("empty_folder")
```

The directory must be empty.

---

## 🔎 4. Path Checking Functions

### A. `os.path.exists()`

Checks whether a path exists.

```python
import os

print(os.path.exists("security.log"))
```

Returns `True` if the path exists and `False` otherwise.

### B. `os.path.isfile()`

Checks whether a path points to a file.

```python
import os

print(os.path.isfile("security.log"))
```

### C. `os.path.isdir()`

Checks whether a path points to a directory.

```python
import os

print(os.path.isdir("security_logs"))
```

### D. `os.path.join()`

Combines path components using the correct path separator for the operating system.

```python
import os

folder = "security_logs"
filename = "events.txt"

file_path = os.path.join(folder, filename)

print(file_path)
```

**Example output on Windows:**

```text
security_logs\events.txt
```

### E. `os.path.getsize()`

Returns a file's size in bytes.

```python
import os

size = os.path.getsize("security.log")

print("File size:", size, "bytes")
```

**Cybersecurity use:** Monitor log file sizes to help detect unusual growth.

---

## 🛡️ 5. System and Process Information

### A. `os.environ`

Provides access to environment variables.

```python
import os

for name, value in os.environ.items():
    print(name, value)
```

⚠️ Environment variables may contain sensitive information. Avoid printing or sharing them indiscriminately.

### B. `os.getenv()`

Retrieves the value of a particular environment variable.

```python
import os

print(os.getenv("USERNAME"))
```

On Windows, this commonly returns the current username.

### C. `os.getpid()`

Returns the process ID of the currently running Python program.

```python
import os

print("Process ID:", os.getpid())
```

### D. `os.cpu_count()`

Returns the number of logical CPUs.

```python
import os

print("CPU Count:", os.cpu_count())
```

### E. `os.stat()`

Retrieves metadata about a file or directory, including its size and timestamps.

```python
import os

details = os.stat("security.log")

print("File Size:", details.st_size)
print("Last Modified:", details.st_mtime)
```

### F. `os.system()`

Executes a command through the operating system's command processor.

```python
import os

os.system("whoami")
```

This example runs the `whoami` command on Windows and many Unix-like systems.

⚠️ **Security warning:** Avoid passing untrusted input to `os.system()`, because it can lead to command injection. Prefer safer alternatives, such as `subprocess.run()` with a list of arguments and `shell=False`.

---

## 🔐 6. Directory Traversal Using `os.walk()`

`os.walk()` traverses a directory and its subdirectories. It provides the current directory, its subdirectories, and its filenames.

```python
import os

for root, directories, files in os.walk("security_logs"):
    for filename in files:
        file_path = os.path.join(root, filename)
        print(file_path)
```

### 🔍 Explanation

- `root` — The current directory path.
- `directories` — The subdirectories inside the current directory.
- `files` — The filenames inside the current directory.
- `os.path.join()` — Combines the directory path and filename.

**Cybersecurity uses:**

- Locating log files.
- Creating file inventories.
- Finding files with specific extensions.
- Automating directory audits.

---

## 🚨 7. Practical Cybersecurity Example

### Check Whether a Log File Exists and Report Its Size

```python
import os

file_path = "security.log"

if os.path.isfile(file_path):
    size = os.path.getsize(file_path)

    print("Log file found.")
    print("File size:", size, "bytes")
else:
    print("Log file not found.")
```

### 📝 How It Works

1. `os.path.isfile()` checks whether the file exists and is a regular file.
2. `os.path.getsize()` retrieves its size in bytes.
3. The `if` statement displays the result.
4. If the file is missing, the program reports that it was not found.

**Practical application:** This approach can be extended to monitor log files and generate alerts when their sizes change unexpectedly.

---

## 🧠 8. Important Differences

| Function | Main Purpose |
|---|---|
| `os.remove()` | Deletes a file. |
| `os.rmdir()` | Removes an empty directory. |
| `os.mkdir()` | Creates one directory. |
| `os.makedirs()` | Creates nested directories. |
| `os.listdir()` | Lists immediate directory contents. |
| `os.walk()` | Traverses an entire directory tree. |
| `os.getenv()` | Reads one environment variable. |
| `os.environ` | Provides access to the environment-variable mapping. |
| `os.path.exists()` | Checks whether a path exists. |
| `os.path.isfile()` | Checks whether a path is a file. |
| `os.path.isdir()` | Checks whether a path is a directory. |

---

## 🎤 9. Interview Answer

**What is the `os` module in Python?**

The `os` module is a built-in Python module that allows programs to interact with the operating system. It provides functions for file and directory management, path checking, environment-variable access, and process information. In cybersecurity, it is commonly used for log processing, file monitoring, and security automation.

---

## 💡 Practical Task

Create a Python program that:

1. Lists all files in a specified folder.
2. Checks whether each item is a file or directory.
3. Reports the size of each file.
4. Displays a message if a specified log file does not exist.

### 📖 Official Documentation

[Python `os` Module Documentation](https://docs.python.org/3/library/os.html)
