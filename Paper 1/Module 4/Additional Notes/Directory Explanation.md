# Linux Directory Structure — Beginner Guide

Think of the Linux `/` directory as the **main folder of the entire operating system**. Everything in Linux starts from `/`.

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── tmp
├── usr
└── var
```

## 1. `/` — The Main Folder

`/` is called the **root directory**.

Think of it like the **C: drive in Windows**.

Everything in Linux is organized under `/`.

```text
/
├── home
├── etc
├── usr
└── var
```

> **Remember:** `/` = The main/root folder of the Linux system.

---

## 2. `/bin` — Basic Commands

Contains basic programs and commands used by users.

Examples:

```bash
ls
cp
mv
cat
```

> **Remember:** `bin` = Basic commands.

---

## 3. `/boot` — Files Needed to Start Linux

Contains files required when the computer **starts (boots)**.

> **Remember:** `boot` = Starting Linux.

---

## 4. `/dev` — Devices

Linux treats hardware devices like files, and many device files are found here.

Examples:

```text
/dev/sda    → Hard disk
/dev/tty    → Terminal
```

> **Remember:** `dev` = Devices.

---

## 5. `/etc` — Configuration

Contains **configuration and settings** for Linux and installed services.

Examples:

```text
/etc/hosts
/etc/passwd
```

> **Remember:** `etc` = Configuration/settings.

---

## 6. `/home` — Users' Personal Folders

This is where normal users keep their personal files.

For example:

```text
/home/rahul
/home/arun
```

Inside a user's home directory, you might find:

```text
Documents
Downloads
Pictures
Videos
```

> **Remember:** `home` = Users' personal files.

---

## 7. `/lib` — Libraries

Contains libraries needed by programs and the operating system.

A **library** is reusable code that programs depend on.

> **Remember:** `lib` = Supporting code for programs.

---

## 8. `/media` — Removable Devices

When you connect devices such as a **USB drive**, Linux may make them available under `/media`.

Example:

```text
/media/rahul/USB
```

> **Remember:** `media` = USB/CD and other removable storage.

---

## 9. `/mnt` — Temporary Mount Location

Used to **manually attach (mount) storage**, such as another disk or partition.

Example:

```text
/mnt/mydisk
```

> **Remember:** `mnt` = Place to temporarily attach storage.

---

## 10. `/opt` — Optional Software

Used for additional or third-party software that isn't part of the core system.

Example:

```text
/opt/mysoftware
```

> **Remember:** `opt` = Optional software.

---

## 11. `/proc` — System and Process Information

Contains information about:

* Running processes
* CPU
* Memory
* Kernel

Examples:

```text
/proc/cpuinfo
/proc/meminfo
```

These are not normal files stored permanently on the hard disk. Linux creates this information dynamically.

> **Remember:** `proc` = Processes and system information.

---

## 12. `/root` — Root User's Home

`root` is the **administrator user** in Linux.

The root user's home directory is:

```text
/root
```

Don't confuse:

```text
/       → Root directory
/root   → Root user's home directory
```

> **Remember:** `/root` = Administrator's home.

---

## 13. `/run` — Information About Running Programs

Contains temporary information about programs and services that are **currently running**.

It can contain information about:

* Processes
* Services
* Login sessions

> **Remember:** `run` = What's running now.

---

## 14. `/sbin` — System Administration Commands

Contains important commands mainly used for **system administration**.

These commands can be related to:

* Disk management
* Networking
* System configuration

> **Remember:** `sbin` = System administration commands.

---

## 15. `/tmp` — Temporary Files

Programs use `/tmp` to store files temporarily.

Example:

```text
/tmp/download.tmp
```

Temporary files may be deleted when the system restarts or through system cleanup.

> **Remember:** `tmp` = Temporary files.

---

## 16. `/usr` — Programs and Resources

Contains a large part of the software and resources installed on the system.

Examples:

```text
/usr/bin
/usr/lib
/usr/share
```

> **Remember:** `usr` = Programs and resources.

**Note:** `/usr` does not mean one particular user's folder.

---

## 17. `/var` — Changing Data

Contains data that **changes while the system is running**.

Examples:

```text
/var/log
/var/cache
/var/tmp
```

One important directory is:

```text
/var/log
```

It contains system and application logs.

> **Remember:** `var` = Variable/changing data.

---

# Quick Reference

| Directory | Simple Meaning                 |
| --------- | ------------------------------ |
| `/`       | Everything starts here         |
| `/bin`    | Basic commands                 |
| `/boot`   | Files needed to start Linux    |
| `/dev`    | Devices                        |
| `/etc`    | Configuration                  |
| `/home`   | Users' personal files          |
| `/lib`    | Libraries                      |
| `/media`  | USB/CD/removable storage       |
| `/mnt`    | Manually mounted storage       |
| `/opt`    | Optional software              |
| `/proc`   | System/process information     |
| `/root`   | Administrator's home           |
| `/run`    | Currently running information  |
| `/sbin`   | System administration commands |
| `/tmp`    | Temporary files                |
| `/usr`    | Programs and resources         |
| `/var`    | Changing data/logs             |

# Easy Way to Remember

Imagine a **Linux house**:

```text
/                  🏠 Linux House
│
├── bin             🛠️ Tools
├── boot            🚀 Starting the house
├── dev             🔌 Devices
├── etc             ⚙️ Settings
├── home            🛏️ Users' rooms
├── lib             📚 Supporting libraries
├── media           💾 USB/CD storage
├── mnt             💿 Attached storage
├── opt             📦 Extra software
├── proc            📊 System information
├── root            👑 Admin's room
├── run             🏃 What's happening now
├── sbin            🔧 Admin tools
├── tmp             🗑️ Temporary things
├── usr             📦 Installed programs
└── var             📝 Logs/changing data
```

## What Should a Fresher Learn First?

Focus on these directories first:

1. `/` — Root directory
2. `/home` — User files
3. `/etc` — Configuration
4. `/bin` — Basic commands
5. `/usr` — Programs and resources
6. `/var` — Logs and changing data
7. `/tmp` — Temporary files
8. `/root` — Administrator's home
9. `/boot` — Boot-related files

These are the most useful directories to understand when you're starting with Linux.
