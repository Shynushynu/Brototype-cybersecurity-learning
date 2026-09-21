# 🐧 Linux Command Line – Essential Commands

## 📌 Overview

Linux provides a powerful command-line interface (CLI) for navigating the system, managing files, processing text, searching for information, and performing administrative tasks.

---

## 🧭 1. Navigation Commands

| Command  | Purpose                                  | Example    |
| -------- | ---------------------------------------- | ---------- |
| `pwd`    | Show current directory                   | `pwd`      |
| `ls`     | List files and directories               | `ls`       |
| `cd`     | Change directory                         | `cd /home` |
| `cd ..`  | Go to parent directory                   | `cd ..`    |
| `cd ~`   | Go to home directory                     | `cd ~`     |
| `ls -la` | Show all files with detailed information | `ls -la`   |

---

## 📁 2. File Management Commands

| Command | Purpose                   | Example                  |
| ------- | ------------------------- | ------------------------ |
| `touch` | Create a file             | `touch file.txt`         |
| `mkdir` | Create a directory        | `mkdir test`             |
| `cp`    | Copy a file or directory  | `cp file.txt backup.txt` |
| `mv`    | Move or rename a file     | `mv old.txt new.txt`     |
| `rm`    | Delete a file             | `rm file.txt`            |
| `rmdir` | Delete an empty directory | `rmdir test`             |
| `cat`   | Display file contents     | `cat file.txt`           |
| `less`  | Read a file page by page  | `less file.txt`          |
| `file`  | Identify file type        | `file file.txt`          |

---

## 📝 3. Text Processing Commands

| Command | Purpose                            | Example                   |
| ------- | ---------------------------------- | ------------------------- |
| `cat`   | Display text                       | `cat file.txt`            |
| `head`  | Display the beginning of a file    | `head file.txt`           |
| `tail`  | Display the end of a file          | `tail file.txt`           |
| `grep`  | Search for text                    | `grep "error" log.txt`    |
| `sort`  | Sort lines                         | `sort names.txt`          |
| `uniq`  | Remove consecutive duplicate lines | `uniq names.txt`          |
| `wc`    | Count lines, words, and characters | `wc file.txt`             |
| `cut`   | Extract fields or columns          | `cut -d: -f1 /etc/passwd` |
| `tr`    | Translate or replace characters    | `tr 'a-z' 'A-Z'`          |

---

## 🔎 4. Search Operations

| Command   | Purpose                                     | Example                    |
| --------- | ------------------------------------------- | -------------------------- |
| `find`    | Search for files and directories            | `find /home -name "*.txt"` |
| `locate`  | Quickly search for files                    | `locate file.txt`          |
| `grep`    | Search inside files                         | `grep "password" file.txt` |
| `which`   | Find the location of a command              | `which python`             |
| `whereis` | Locate a command, binary, and documentation | `whereis bash`             |

---

## 🛠️ 5. Administrative Commands

| Command     | Purpose                                     | Example                      |
| ----------- | ------------------------------------------- | ---------------------------- |
| `sudo`      | Run a command with administrator privileges | `sudo apt update`            |
| `whoami`    | Show the current user                       | `whoami`                     |
| `id`        | Display user and group information          | `id`                         |
| `passwd`    | Change a user's password                    | `passwd`                     |
| `useradd`   | Create a new user                           | `sudo useradd john`          |
| `usermod`   | Modify a user account                       | `sudo usermod -aG sudo john` |
| `userdel`   | Delete a user                               | `sudo userdel john`          |
| `systemctl` | Manage system services                      | `sudo systemctl status ssh`  |
| `ps`        | Display running processes                   | `ps aux`                     |
| `kill`      | Terminate a process                         | `kill 1234`                  |
| `df`        | Display disk space usage                    | `df -h`                      |
| `du`        | Display directory/file size                 | `du -sh /home`               |
| `free`      | Display memory usage                        | `free -h`                    |

---

## ⭐ Essential Commands to Practice

```bash
pwd
ls
cd
mkdir
touch
cp
mv
rm
cat
less
head
tail
grep
cut
find
which
whoami
sudo
ps
kill
systemctl
df
du
free
```

---

## 🎯 Quick Practice

Try these commands in a Linux terminal:

```bash
mkdir linux-practice
cd linux-practice
touch file.txt
echo "Hello Linux" > file.txt
cat file.txt
cp file.txt backup.txt
ls -la
grep "Linux" file.txt
mv backup.txt copy.txt
find . -name "*.txt"
```

### 💡 Tip

> Practice each command yourself instead of only memorizing it. Understanding what a command does and how its options work is more important than memorizing commands.
