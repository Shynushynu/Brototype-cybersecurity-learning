
## 📌 Table of Contents

* [a. Navigation Commands](#a-navigation-commands)
* [b. File Management](#b-file-management)
* [c. Text Processing](#c-text-processing)
* [d. Search Operations](#d-search-operations)
* [e. Administrative Commands](#e-administrative-commands)
* [🔑 Important Command Options](#-important-command-options)

---

# a. 🧭 Navigation Commands

Navigation commands are used to move around the Linux filesystem and view directories.

| Command | Purpose                     | Common Variations                                       |
| ------- | --------------------------- | ------------------------------------------------------- |
| `pwd`   | Show current directory      | `pwd -L`, `pwd -P`                                      |
| `ls`    | List files and directories  | `ls -l`, `ls -a`, `ls -la`, `ls -lh`, `ls -R`, `ls -lt` |
| `cd`    | Change directory            | `cd ..`, `cd ~`, `cd -`, `cd /path`                     |
| `tree`  | Display directory structure | `tree -L 2`, `tree -a`                                  |

### 🔹 `pwd`

Displays the current working directory.

```bash
pwd
```

#### Variations

```bash
pwd -L
pwd -P
```

* `-L` → **Logical path** — shows the path as reached through symbolic links.
* `-P` → **Physical path** — shows the actual filesystem path and resolves symbolic links.

> 🧠 **Easy way to remember:**
> `-L` = Logical
> `-P` = Physical

### 🔹 `ls`

Lists files and directories.

```bash
ls
ls -l
ls -a
ls -la
ls -lh
ls -R
ls -lt
```

| Option | Meaning                   |
| ------ | ------------------------- |
| `-l`   | Long/detailed listing     |
| `-a`   | Show hidden files         |
| `-h`   | Human-readable file sizes |
| `-R`   | List recursively          |
| `-t`   | Sort by modification time |

### 🔹 `cd`

Changes the current directory.

```bash
cd /home
cd ..
cd ~
cd -
```

| Command    | Meaning                           |
| ---------- | --------------------------------- |
| `cd /path` | Go to a specific directory        |
| `cd ..`    | Go to the parent directory        |
| `cd ~`     | Go to the user's home directory   |
| `cd -`     | Go back to the previous directory |

---

# b. 📁 File Management

File-management commands are used to create, copy, move, rename, and delete files and directories.

| Command | Purpose                  | Common Variations                   |
| ------- | ------------------------ | ----------------------------------- |
| `touch` | Create a file            | `touch file.txt`                    |
| `mkdir` | Create directory         | `mkdir test`, `mkdir -p a/b/c`      |
| `cp`    | Copy files/directories   | `cp file1 file2`, `cp -r dir1 dir2` |
| `mv`    | Move/rename files        | `mv old new`                        |
| `rm`    | Delete files/directories | `rm -r`, `rm -f`, `rm -i`           |
| `rmdir` | Remove empty directory   | `rmdir folder`                      |
| `file`  | Identify file type       | `file file.txt`                     |
| `stat`  | Show file information    | `stat file.txt`                     |

### Important Options

| Option     | Meaning                             |
| ---------- | ----------------------------------- |
| `mkdir -p` | Create parent directories if needed |
| `cp -r`    | Copy directories recursively        |
| `rm -r`    | Remove directories recursively      |
| `rm -f`    | Force removal                       |
| `rm -i`    | Ask for confirmation before removal |

> ⚠️ Be careful with `rm -rf`. It can permanently delete files and directories.

---

# c. 📝 Text Processing

Text-processing commands are used to read, search, filter, count, and modify text.

| Command | Purpose                      | Common Variations                        |
| ------- | ---------------------------- | ---------------------------------------- |
| `cat`   | Display file contents        | `cat -n file.txt`                        |
| `less`  | Read file page by page       | `less file.txt`                          |
| `head`  | Show beginning of file       | `head -n 10 file.txt`                    |
| `tail`  | Show end of file             | `tail -n 10 file.txt`, `tail -f log.txt` |
| `grep`  | Search text                  | `grep -i`, `grep -r`, `grep -n`          |
| `sort`  | Sort lines                   | `sort -r`, `sort -n`                     |
| `uniq`  | Handle duplicate lines       | `uniq -c`, `uniq -d`                     |
| `wc`    | Count lines/words/characters | `wc -l`, `wc -w`, `wc -c`                |
| `cut`   | Extract sections/columns     | `cut -d: -f1 file`                       |
| `tr`    | Translate/replace characters | `tr 'a-z' 'A-Z'`                         |
| `sed`   | Process/modify text          | `sed 's/old/new/g' file`                 |
| `awk`   | Process structured text      | `awk '{print $1}' file`                  |

### 🔹 `grep` Options

```bash
grep "error" file.txt
grep -i "error" file.txt
grep -n "error" file.txt
grep -r "error" directory/
grep -v "error" file.txt
```

| Option | Meaning                           |
| ------ | --------------------------------- |
| `-i`   | Ignore case                       |
| `-r`   | Search recursively                |
| `-n`   | Show line numbers                 |
| `-v`   | Show lines that do not match      |
| `-c`   | Count matching lines              |
| `-l`   | Show filenames containing matches |

---

# d. 🔍 Search Operations

Search commands help locate files, directories, commands, and text.

| Command   | Purpose                      | Common Variations      |
| --------- | ---------------------------- | ---------------------- |
| `find`    | Search for files/directories | `find . -name "*.txt"` |
| `locate`  | Quickly locate files         | `locate file.txt`      |
| `which`   | Find command location        | `which python`         |
| `whereis` | Find binary/source/man page  | `whereis python`       |
| `grep`    | Search inside files          | `grep "text" file.txt` |

### 🔹 `find` Examples

```bash
find . -name "*.txt"
```

Find `.txt` files in the current directory.

```bash
find /home -type f
```

Find regular files under `/home`.

```bash
find . -type d
```

Find directories.

```bash
find . -size +10M
```

Find files larger than 10 MB.

```bash
find . -mtime -7
```

Find files modified within the last 7 days.

---

# e. 🛠️ Administrative Commands

Administrative commands are used to manage users, permissions, processes, services, storage, and system resources.

| Command     | Purpose                              | Common Variations         |
| ----------- | ------------------------------------ | ------------------------- |
| `sudo`      | Run command with elevated privileges | `sudo command`            |
| `su`        | Switch user                          | `su user`, `su -`         |
| `whoami`    | Show current user                    | `whoami`                  |
| `id`        | Show user/group IDs                  | `id username`             |
| `useradd`   | Create user                          | `useradd -m user`         |
| `passwd`    | Change password                      | `passwd`                  |
| `usermod`   | Modify user                          | `usermod -aG group user`  |
| `groupadd`  | Create group                         | `groupadd groupname`      |
| `groups`    | Show user's groups                   | `groups user`             |
| `chmod`     | Change permissions                   | `chmod 755 file`          |
| `chown`     | Change ownership                     | `chown user file`         |
| `chgrp`     | Change group ownership               | `chgrp group file`        |
| `ps`        | Show processes                       | `ps aux`, `ps -ef`        |
| `top`       | Monitor processes                    | `top`                     |
| `kill`      | Terminate process                    | `kill PID`, `kill -9 PID` |
| `systemctl` | Manage services                      | `systemctl status ssh`    |
| `df`        | Show disk usage                      | `df -h`                   |
| `du`        | Show file/directory size             | `du -sh folder`           |
| `free`      | Show memory usage                    | `free -h`                 |
| `shutdown`  | Shut down system                     | `shutdown now`            |
| `reboot`    | Restart system                       | `reboot`                  |

---

# 🔥 Important Command Variations

## `ls`

```bash
ls
ls -l
ls -a
ls -la
ls -lh
ls -R
ls -lt
```

---

## `grep`

```bash
grep "text" file
grep -i "text" file
grep -n "text" file
grep -r "text" directory
grep -v "text" file
```

---

## `find`

```bash
find . -name "*.txt"
find . -type f
find . -type d
find . -size +10M
find . -mtime -7
```

---

## `chmod`

```bash
chmod 755 file
chmod 644 file
chmod +x script.sh
chmod u+x file
chmod g+w file
chmod o-r file
```

---

## `ps`

```bash
ps
ps aux
ps -ef
```

---

## `systemctl`

```bash
systemctl status service
systemctl start service
systemctl stop service
systemctl restart service
systemctl enable service
systemctl disable service
```

---

# 🧠 What Are Command Options?

The letters after a command are usually called **options**, **flags**, or **switches**.

For example:

```bash
ls -lah
```

Here:

* `-l` → Long/detailed listing
* `-a` → Show all files, including hidden files
* `-h` → Human-readable sizes

Multiple options can often be combined:

```bash
ls -l -a -h
```

is equivalent to:

```bash
ls -lah
```

---

# 🎯 Quick Revision

| Category           | Important Commands                                             |
| ------------------ | -------------------------------------------------------------- |
| 🧭 Navigation      | `pwd`, `ls`, `cd`, `tree`                                      |
| 📁 File Management | `touch`, `mkdir`, `cp`, `mv`, `rm`                             |
| 📝 Text Processing | `cat`, `head`, `tail`, `grep`, `sort`, `cut`, `sed`, `awk`     |
| 🔍 Search          | `find`, `locate`, `which`, `whereis`, `grep`                   |
| 🛠️ Administration | `sudo`, `useradd`, `chmod`, `chown`, `ps`, `kill`, `systemctl` |

> 💡 **Cybersecurity Tip:** Commands such as `grep`, `find`, `ps`, `tail`, `chmod`, `systemctl`, and `journalctl` are especially useful when investigating Linux systems.
