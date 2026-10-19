# 🐍 Python `sys` Module

## 📌 Overview

The Python `sys` module provides functions and variables to interact with the Python interpreter and control program execution.

```python
import sys
```

## 📚 Table of Contents

1. [`sys.argv`](#1-sysargv)
2. [`sys.exit()`](#2-sysexit)
3. [`sys.path`](#3-syspath)
4. [`sys.version`](#4-sysversion)
5. [`sys.platform`](#5-sysplatform)
6. [`sys.stdin`](#6-sysstdin)
7. [`sys.stdout`](#7-sysstdout)
8. [`sys.stderr`](#8-sysstderr)
9. [`sys.getsizeof()`](#9-sysgetsizeof)
10. [`sys.executable`](#10-sysexecutable)

## 1. `sys.argv`

Reads command-line arguments provided when running a Python script.

```python
import sys

print(sys.argv)
```

Run:

```bash
python parser.py server.log
```

Output:

```text
['parser.py', 'server.log']
```

- `sys.argv[0]` — script name.
- `sys.argv[1]` — first argument after the script name.

**Use:** Select a log file without modifying the code.

## 2. `sys.exit()`

Stops program execution.

```python
import sys

print("Starting program")
sys.exit(1)
print("This will not execute")
```

**Use:** Stop a program when a required input is missing or an error prevents it from continuing.

- `sys.exit(0)` — conventionally indicates success.
- `sys.exit(1)` — conventionally indicates an error.

## 3. `sys.path`

Displays the directories Python searches when importing modules.

```python
import sys

print(sys.path)
```

**Use:** Troubleshoot module import errors.

## 4. `sys.version`

Displays information about the Python version currently running.

```python
import sys

print(sys.version)
```

**Use:** Check Python version compatibility.

## 5. `sys.platform`

Identifies the operating system platform.

```python
import sys

print(sys.platform)
```

| Output | Platform |
|---|---|
| `win32` | Windows |
| `linux` | Linux |
| `darwin` | macOS |

**Use:** Build scripts that behave differently across operating systems.

## 6. `sys.stdin`

Reads data from standard input, such as terminal input or data piped from another command.

```python
import sys

data = sys.stdin.readline()

print("Received:", data)
```

Linux example:

```bash
cat server.log | python parser.py
```

The script must explicitly read the incoming data through `sys.stdin` for this command to work as intended.

**Use:** Process log data supplied by another program.

## 7. `sys.stdout`

Writes normal output to standard output, usually the terminal.

```python
import sys

sys.stdout.write("Log parsing started\n")
```

This is similar to:

```python
print("Log parsing started")
```

Redirect output on Linux:

```bash
python parser.py > results.txt
```

**Use:** Display or redirect program results.

## 8. `sys.stderr`

Writes error messages to standard error, separately from normal output.

```python
import sys

sys.stderr.write("Error: Log file not found\n")
```

Redirect errors:

```bash
python parser.py 2> errors.txt
```

**Use:** Separate error messages from normal reports.

## 9. `sys.getsizeof()`

Returns the shallow memory size of an object in bytes.

```python
import sys

ips = ["192.0.2.1", "192.0.2.2"]

print(sys.getsizeof(ips))
```

**Use:** Explore memory usage when working with large datasets.

**Note:** This measures the list object itself, not the complete memory used by all objects inside it.

## 10. `sys.executable`

Displays the path of the Python interpreter running the program.

```python
import sys

print(sys.executable)
```

Example output:

```text
C:\Python313\python.exe
```

**Use:** Troubleshoot Python interpreter and virtual environment issues.

---

## 🔄 Quick Revision

| Feature | Purpose |
|---|---|
| `sys.argv` | Read command-line arguments |
| `sys.exit()` | Stop program execution |
| `sys.path` | View module search paths |
| `sys.version` | Check Python version |
| `sys.platform` | Identify the operating system |
| `sys.stdin` | Read standard input |
| `sys.stdout` | Write normal output |
| `sys.stderr` | Write error messages |
| `sys.getsizeof()` | Check shallow object size |
| `sys.executable` | Find the active Python interpreter |

## 🛡️ Cybersecurity Applications

For log parsing and automation projects:

- **`sys.argv`** — Specify which log file to analyze.
- **`sys.exit()`** — Stop execution when required input is missing.
- **`sys.stdin`** — Receive piped log data.
- **`sys.stdout`** — Display or redirect reports.
- **`sys.stderr`** — Separate errors from normal output.
- **`sys.executable`** — Identify the Python interpreter running the tool.

## ✅ Key Takeaway

The `sys` module helps Python programs interact with the interpreter and command-line environment. It does not parse logs by itself; your program must still read and analyze the log data.
