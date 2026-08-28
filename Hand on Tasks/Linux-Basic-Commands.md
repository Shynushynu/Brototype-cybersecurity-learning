# 🐧 Linux Basic Commands — Complete Beginner Guide

Linux commands are instructions typed into the **Terminal** to interact with the operating system. They are especially important for **cybersecurity, system administration, and programming**.

---

## 📁 1. File & Directory Commands

### `pwd` — Print Working Directory

Shows your current location.

```bash
pwd
```

Example:

```text
/home/shynu
```

### `ls` — List Files

Shows files and folders in the current directory.

```bash
ls
```

Useful options:

```bash
ls -l    # Detailed list
ls -a    # Show hidden files
ls -la   # Detailed + hidden files
```

### `cd` — Change Directory

Moves to another directory.

```bash
cd Documents
```

Go back one directory:

```bash
cd ..
```

Go to your home directory:

```bash
cd ~
```

---

## 📂 2. Creating Files & Directories

### `mkdir` — Make Directory

Creates a new directory.

```bash
mkdir projects
```

### `touch` — Create a File

Creates an empty file.

```bash
touch notes.txt
```

### `rmdir` — Remove Empty Directory

Removes an empty directory.

```bash
rmdir projects
```

> ⚠️ `rmdir` works only when the directory is empty.

---

## 🗑️ 3. Copy, Move & Delete

### `cp` — Copy

Copies a file.

```bash
cp notes.txt backup.txt
```

Copy a directory:

```bash
cp -r folder1 folder2
```

### `mv` — Move or Rename

Move a file:

```bash
mv notes.txt Documents/
```

Rename a file:

```bash
mv old.txt new.txt
```

### `rm` — Remove

Deletes a file.

```bash
rm notes.txt
```

Remove a directory and its contents:

```bash
rm -r folder
```

> ⚠️ Be careful with `rm`; deleted files may not go to a recycle bin.

---

## 📖 4. Reading Files

### `cat`

Displays the contents of a file.

```bash
cat notes.txt
```

### `less`

Useful for reading large files.

```bash
less largefile.txt
```

Press **`q`** to exit.

### `head`

Shows the beginning of a file.

```bash
head notes.txt
```

### `tail`

Shows the end of a file.

```bash
tail notes.txt
```

---

## 🔎 5. Searching

### `grep`

Searches for text inside files.

```bash
grep "password" notes.txt
```

Example:

```bash
grep "error" logfile.txt
```

### `find`

Searches for files and directories.

```bash
find . -name "notes.txt"
```

`.` means the current directory.

---

## 🖥️ 6. System Information

### `whoami`

Shows the current user.

```bash
whoami
```

### `uname`

Shows system information.

```bash
uname -a
```

### `hostname`

Shows the computer's hostname.

```bash
hostname
```

### `date`

Shows the current date and time.

```bash
date
```

---

## 💾 7. Disk & Memory

### `df`

Shows available disk space.

```bash
df -h
```

### `du`

Shows how much space files or directories use.

```bash
du -sh folder
```

### `free`

Shows memory usage.

```bash
free -h
```

---

## ⚙️ 8. Processes

### `ps`

Shows running processes.

```bash
ps
```

More detailed:

```bash
ps aux
```

### `top`

Displays running processes and resource usage.

```bash
top
```

Press **`q`** to exit.

---

## 🌐 9. Network Commands

### `ip`

Displays network information.

```bash
ip addr
```

### `ping`

Tests network connectivity.

```bash
ping example.com
```

Stop it with:

```text
Ctrl + C
```

### `curl`

Makes requests to a URL and can retrieve data.

```bash
curl https://example.com
```

### `ss`

Shows network connections and listening sockets.

```bash
ss -tuln
```

---

## 🔐 10. Permissions

### `chmod`

Changes file permissions.

```bash
chmod +x script.sh
```

Makes a script executable.

### `chown`

Changes file ownership.

```bash
sudo chown user:user file.txt
```

### `ls -l`

Displays file permissions.

```bash
ls -l
```

Example:

```text
-rw-r--r-- 1 user user 120 Aug 28 notes.txt
```

---

## 👤 11. User Commands

### `id`

Displays user and group information.

```bash
id
```

### `sudo`

Runs a command with administrator privileges.

```bash
sudo command
```

> ⚠️ Only use `sudo` when necessary and make sure you understand the command first.

---

## 📦 12. Installing Software

On Debian/Ubuntu-based systems:

### Update Package Information

```bash
sudo apt update
```

### Upgrade Installed Packages

```bash
sudo apt upgrade
```

### Install a Package

```bash
sudo apt install package-name
```

Example:

```bash
sudo apt install git
```

---

## 🧹 13. Terminal Utilities

### `clear`

Clears the terminal screen.

```bash
clear
```

### `history`

Shows previously executed commands.

```bash
history
```

### `man`

Shows the manual for a command.

```bash
man ls
```

### `echo`

Prints text.

```bash
echo "Hello Linux"
```

---

# ⭐ Essential Commands to Remember

| Command   | Purpose                |
| --------- | ---------------------- |
| `pwd`     | Show current directory |
| `ls`      | List files             |
| `cd`      | Change directory       |
| `mkdir`   | Create directory       |
| `touch`   | Create file            |
| `cp`      | Copy                   |
| `mv`      | Move/rename            |
| `rm`      | Delete                 |
| `cat`     | Read file              |
| `grep`    | Search text            |
| `find`    | Find files             |
| `whoami`  | Show current user      |
| `ps`      | Show processes         |
| `df`      | Show disk space        |
| `ip`      | Network information    |
| `ping`    | Test connectivity      |
| `chmod`   | Change permissions     |
| `sudo`    | Run as administrator   |
| `man`     | Command manual         |
| `history` | Command history        |

---

# 🎯 Beginner Practice

Try these commands inside a safe practice folder:

```bash
mkdir linux-practice
cd linux-practice
touch notes.txt
echo "Learning Linux" > notes.txt
cat notes.txt
cp notes.txt backup.txt
ls -l
mv backup.txt backup-notes.txt
ls
```

These commands cover the **core Linux skills you should know as a beginner**, especially when learning **cybersecurity, system administration, and programming**.
