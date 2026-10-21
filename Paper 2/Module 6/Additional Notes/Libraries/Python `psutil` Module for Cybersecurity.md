# 🐍 Python `psutil` Module for Cybersecurity

## 📚 Table of Contents

- [🎯 Overview](#-overview)
- [📌 Functions List](#-functions-list)
- [🖥️ 1. CPU Functions](#️-1-cpu-functions)
- [🧠 2. Memory Functions](#-2-memory-functions)
- [💾 3. Disk Functions](#-3-disk-functions)
- [⚙️ 4. Process Functions](#️-4-process-functions)
- [🌐 5. Network Functions](#-5-network-functions)
- [👤 6. User and System Functions](#-6-user-and-system-functions)
- [🔐 7. Cybersecurity Applications](#-7-cybersecurity-applications)
- [🎤 8. Interview Answer](#-8-interview-answer)

---

## 🎯 Overview

`psutil` stands for **Process and System Utilities**. It is a Python module used to retrieve system information and monitor resources such as CPU, memory, disk usage, running processes, and network connections.

In cybersecurity, `psutil` helps automate system monitoring, investigate running processes, inspect network connections, and generate resource usage alerts.

Install the module using:

```bash
pip install psutil
```

Import it into your Python program:

```python
import psutil
```

---

## 📌 Functions List

### 🖥️ CPU Functions
- [`psutil.cpu_percent()`](#1-cpu-functions) — Returns CPU usage as a percentage.
- [`psutil.cpu_count()`](#1-cpu-functions) — Returns the number of CPUs or CPU cores.
- [`psutil.cpu_times()`](#1-cpu-functions) — Returns CPU time statistics.
- [`psutil.cpu_stats()`](#1-cpu-functions) — Returns CPU statistics, such as context switches and interrupts.
- [`psutil.cpu_freq()`](#1-cpu-functions) — Returns CPU frequency information.
- [`psutil.getloadavg()`](#1-cpu-functions) — Returns system load averages where supported.

### 🧠 Memory Functions
- [`psutil.virtual_memory()`](#2-memory-functions) — Returns physical RAM statistics.
- [`psutil.swap_memory()`](#2-memory-functions) — Returns swap memory statistics.

### 💾 Disk Functions
- [`psutil.disk_usage()`](#3-disk-functions) — Returns disk space usage.
- [`psutil.disk_partitions()`](#3-disk-functions) — Lists mounted disk partitions.
- [`psutil.disk_io_counters()`](#3-disk-functions) — Returns disk input/output statistics.

### ⚙️ Process Functions
- [`psutil.pids()`](#4-process-functions) — Returns process IDs.
- [`psutil.process_iter()`](#4-process-functions) — Iterates through running processes.
- [`psutil.Process()`](#4-process-functions) — Creates an object for inspecting a specific process.
- [`psutil.pid_exists()`](#4-process-functions) — Checks whether a process ID exists.
- [`psutil.wait_procs()`](#4-process-functions) — Waits for processes to finish.
- [`psutil.process_iter()` with `process.info`](#4-process-functions) — Retrieves selected process information.

### 🌐 Network Functions
- [`psutil.net_connections()`](#5-network-functions) — Returns network connection information.
- [`psutil.net_if_addrs()`](#5-network-functions) — Returns network interface addresses.
- [`psutil.net_if_stats()`](#5-network-functions) — Returns network interface status and statistics.
- [`psutil.net_io_counters()`](#5-network-functions) — Returns network input/output statistics.

### 👤 User and System Functions
- [`psutil.boot_time()`](#6-user-and-system-functions) — Returns the system boot time.
- [`psutil.users()`](#6-user-and-system-functions) — Returns logged-in user information.
- [`psutil.sensors_temperatures()`](#6-user-and-system-functions) — Returns temperature sensor information where supported.
- [`psutil.sensors_fans()`](#6-user-and-system-functions) — Returns fan sensor information where supported.
- [`psutil.sensors_battery()`](#6-user-and-system-functions) — Returns battery information where supported.
- [`psutil.win_service_iter()`](#6-user-and-system-functions) — Iterates through Windows services.
- [`psutil.win_service_get()`](#6-user-and-system-functions) — Retrieves a Windows service by name.

---

## 🖥️ 1. CPU Functions

CPU functions help monitor processor usage, speed, and activity.

| Function | Definition |
|---|---|
| `psutil.cpu_percent(interval=1)` | Measures CPU usage as a percentage over the specified interval. |
| `psutil.cpu_count()` | Returns the number of logical CPUs by default. Use `logical=False` for physical cores when supported. |
| `psutil.cpu_times()` | Returns the time the CPU has spent in different states, such as user and system time. |
| `psutil.cpu_stats()` | Returns statistics such as context switches, interrupts, and system calls where available. |
| `psutil.cpu_freq()` | Returns the current, minimum, and maximum CPU frequency where supported. |
| `psutil.getloadavg()` | Returns the average system load over 1, 5, and 15 minutes where supported. |

**Example:**

```python
import psutil

print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
print("CPU Cores:", psutil.cpu_count())
```

---

## 🧠 2. Memory Functions

Memory functions help monitor RAM and swap memory usage.

| Function | Definition |
|---|---|
| `psutil.virtual_memory()` | Returns physical memory statistics, including total, available, used, and percentage used. |
| `psutil.swap_memory()` | Returns swap memory statistics, including total, used, free, and percentage used. |

**Example:**

```python
import psutil

memory = psutil.virtual_memory()

print("Total RAM:", memory.total)
print("Available RAM:", memory.available)
print("Memory Usage:", memory.percent, "%")
```

---

## 💾 3. Disk Functions

Disk functions help monitor storage capacity, partitions, and disk activity.

| Function | Definition |
|---|---|
| `psutil.disk_usage(path)` | Returns total, used, and free disk space for a specified path. |
| `psutil.disk_partitions()` | Returns mounted disk partitions and their mount points. |
| `psutil.disk_io_counters()` | Returns disk read/write statistics, such as bytes and operation counts. |

**Example:**

```python
import psutil

disk = psutil.disk_usage("C:\\")

print("Total Space:", disk.total)
print("Free Space:", disk.free)
print("Disk Usage:", disk.percent, "%")
```

---

## ⚙️ 4. Process Functions

Process functions help inspect and monitor running programs.

| Function | Definition |
|---|---|
| `psutil.pids()` | Returns a list of process IDs currently present on the system. |
| `psutil.process_iter()` | Iterates through processes and can retrieve selected process attributes. |
| `psutil.Process(pid)` | Creates a process object for inspecting a process with the specified ID. |
| `psutil.pid_exists(pid)` | Checks whether a process ID currently exists. |
| `psutil.wait_procs(procs)` | Waits for a group of processes to terminate, up to a specified timeout. |

A `Process` object provides methods such as:

| Method | Definition |
|---|---|
| `process.name()` | Returns the process name. |
| `process.exe()` | Returns the executable path when accessible. |
| `process.cmdline()` | Returns the command-line arguments. |
| `process.status()` | Returns the process status. |
| `process.cpu_percent()` | Measures CPU usage attributed to the process. |
| `process.memory_info()` | Returns memory usage information for the process. |
| `process.create_time()` | Returns the process creation time. |
| `process.username()` | Returns the username associated with the process when accessible. |
| `process.connections()` | Returns connections associated with the process in versions that provide this method; newer versions may expose `process.net_connections()`. |

**Example:**

```python
import psutil

for process in psutil.process_iter(["pid", "name"]):
    try:
        print(process.info)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
```

---

## 🌐 5. Network Functions

Network functions help inspect network interfaces, connections, and traffic statistics.

| Function | Definition |
|---|---|
| `psutil.net_connections(kind="inet")` | Returns internet socket connection information, including addresses and status when available. |
| `psutil.net_if_addrs()` | Returns addresses assigned to network interfaces. |
| `psutil.net_if_stats()` | Returns interface information, such as whether it is up, its speed, and MTU. |
| `psutil.net_io_counters()` | Returns network traffic statistics, including bytes and packets sent or received. |

**Example:**

```python
import psutil

for interface, addresses in psutil.net_if_addrs().items():
    print(interface, addresses)
```

**Note:** Some network and process details require elevated privileges. Function availability can differ across operating systems and `psutil` versions.

---

## 👤 6. User and System Functions

These functions provide information about system uptime, logged-in users, hardware sensors, and Windows services.

| Function | Definition |
|---|---|
| `psutil.boot_time()` | Returns the system boot time as a Unix timestamp. |
| `psutil.users()` | Returns information about users logged into the system. |
| `psutil.sensors_temperatures()` | Returns hardware temperature sensor readings where supported. |
| `psutil.sensors_fans()` | Returns fan speed readings where supported. |
| `psutil.sensors_battery()` | Returns battery status and related information where supported. |
| `psutil.win_service_iter()` | Iterates through Windows services. |
| `psutil.win_service_get(name)` | Retrieves a Windows service object by its service name. |

**Example:**

```python
import psutil
from datetime import datetime

boot_timestamp = psutil.boot_time()
boot_time = datetime.fromtimestamp(boot_timestamp)

print("System Boot Time:", boot_time)
```

---

## 🔐 7. Cybersecurity Applications

1. **System monitoring:** Track CPU, memory, and disk usage.
2. **Process investigation:** Inspect running programs and their executable paths.
3. **Network monitoring:** Review available network connections and interface activity.
4. **Resource alerts:** Detect unusually high resource usage.
5. **Security automation:** Collect system information for reports and monitoring scripts.
6. **Service monitoring:** Check the status of Windows services.

---

## 🎤 8. Interview Answer

**What is the `psutil` module in Python?**

The `psutil` module stands for Process and System Utilities. It is used to retrieve system information and monitor CPU, memory, disk usage, running processes, and network connections. In cybersecurity, it helps automate system monitoring, investigate processes, and develop security monitoring tools.

---

> 💡 **Important:** This is a practical reference list of commonly used `psutil` functions, not every function in the library. Some functions are platform-specific, and APIs can vary by version. Consult the [official `psutil` documentation](https://psutil.readthedocs.io/) for the complete API reference.
