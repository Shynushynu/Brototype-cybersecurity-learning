# 🐧 1. Understand Linux Fundamentals

Linux is an **open-source operating system** widely used in servers, cloud computing, cybersecurity, networking, embedded systems, and personal computers.

---

## 📚 Overview

Linux fundamentals help us understand how a Linux system is organized and how its main components work.

### 🔗 Topics Covered

* [🐧 Linux Ecosystem](#-a-linux-ecosystem)
* [📁 File System Hierarchy](#-b-file-system-hierarchy)
* [👥 Users and Groups](#-c-users-and-groups)
* [⚙️ Processes](#-d-processes)
* [🔧 System Services](#-e-system-services)

---

## 🐧 A. Linux Ecosystem

The **Linux ecosystem** includes the Linux kernel, distributions, command-line tools, desktop environments, applications, package managers, and other software.

### 🔹 Linux Kernel

The **kernel** is the core part of Linux. It acts like a middleman between the hardware and the software. It manages:

* CPU
* Memory
* Hardware devices
* Processes
* Network communication
* System resources

### 🔹 Linux Distributions

A **Linux distribution (distro)** combines the Linux kernel with software and tools.

| Distribution                | Common Use                            |
| --------------------------- | ------------------------------------- |
| 🟠 Ubuntu                   | General use, servers, learning        |
| 🔴 Red Hat Enterprise Linux | Enterprise environments               |
| 🟢 Linux Mint               | Desktop use                           |
| 🟣 Kali Linux               | Cybersecurity and penetration testing |
| 🔵 Fedora                   | Development and modern Linux features |

---

## 📁 B. File System Hierarchy

Linux organizes files and directories in a **hierarchical structure** that starts from the root directory `/`.

```text
/
├── /bin      → Essential commands
├── /boot     → Boot-related files
├── /dev      → Device files
├── /etc      → Configuration files
├── /home     → Users' personal directories
├── /opt      → Optional software
├── /proc     → Process and kernel information
├── /root     → Home directory of root user
├── /tmp      → Temporary files
├── /usr      → User applications and utilities
└── /var      → Logs and frequently changing data
```

### ⭐ Important Directories

| Directory | Purpose                                |
| --------- | -------------------------------------- |
| `/`       | Root of the entire filesystem          |
| `/home`   | Personal files of normal users         |
| `/etc`    | System configuration files             |
| `/var`    | Logs and changing data                 |
| `/tmp`    | Temporary files                        |
| `/dev`    | Represents hardware devices            |
| `/proc`   | Information about processes and kernel |
| `/root`   | Home directory of the root user        |

---

## 👥 C. Users and Groups

Linux uses **users and groups** to control access to files, directories, and system resources.

### 👤 Users

A **user account** represents an individual or system account.

Common types include:

* **Normal user** → Used for everyday activities
* **Root user** → Has administrative privileges
* **System users** → Used by services and applications

### 👥 Groups

A **group** is a collection of users.

Groups make it easier to manage permissions.

For example:

```text
Developers
├── Alice
├── Bob
└── Charlie
```

Instead of giving permissions individually, permissions can be assigned to the **Developers** group.

### 🔐 Linux Permissions

Linux commonly uses three permission types:

| Permission | Meaning |
| ---------- | ------- |
| `r`        | Read    |
| `w`        | Write   |
| `x`        | Execute |

Example:

```text
-rwxr-xr--
```

These permissions determine what the **owner**, **group**, and **others** can do with a file.

---

## ⚙️ D. Processes

A **process** is a running instance of a program.

For example, when you open a terminal and run a command, Linux creates a process to execute it.

### 🔄 Process Lifecycle

```text
Program
   ↓
Process Created
   ↓
Running
   ↓
Waiting / Sleeping
   ↓
Completed
   ↓
Terminated
```

Each pr
