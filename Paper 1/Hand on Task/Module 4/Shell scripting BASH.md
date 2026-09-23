# 🐚 Bash Scripting Fundamentals

> 📚 A clean syntax reference for learning **Bash Shell Scripting**.

---

## 📑 Table of Contents

* [📝 1. Variables](#-1-variables)
* [⌨️ 2. User Input](#️-2-user-input)
* [🔀 3. Conditional Statements](#-3-conditional-statements)

  * [if](#if)
  * [if-else](#if-else)
  * [if-elif-else](#if-elif-else)
* [🔁 4. Loops](#-4-loops)

  * [for Loop](#for-loop)
  * [while Loop](#while-loop)
  * [do-while Equivalent](#do-while-equivalent)
* [🔀 5. Switch Equivalent — case](#-5-switch-equivalent--case)
* [📦 6. Arrays](#-6-arrays)

  * [Creating an Array](#creating-an-array)
  * [Accessing Elements](#accessing-array-elements)
  * [All Elements](#getting-all-array-elements)
  * [Array Length](#getting-array-length)
* [🔁 7. Looping Through an Array](#-7-looping-through-an-array)
* [⚡ 8. Quick Reference](#-8-quick-reference)
* [🧠 9. Important Bash Keywords](#-9-important-bash-keywords)

---

# 📝 1. Variables

Variables are used to **store values** that can be reused in a script.

### 📌 Syntax

```bash
variable_name="value"
```

### 💡 Example

```bash
name="Shynu"
age=18
directory="/home/user"
```

### 🔍 Accessing a Variable

Use `$` before the variable name:

```bash
echo "$name"
echo "$age"
echo "$directory"
```

> 💡 **Remember:**
> `$` is used when **accessing** a variable, not when assigning a value.

---

# ⌨️ 2. User Input

The `read` command is used to take input from the user.

### 📌 Basic Syntax

```bash
read variable_name
```

### 💡 Example

```bash
echo "Enter your name:"
read name

echo "Hello $name"
```

### ✨ Using `-p`

You can display the prompt and take input in the same line:

```bash
read -p "Enter your age: " age
```

---

# 🔀 3. Conditional Statements

Conditional statements allow a script to **make decisions** based on conditions.

---

## `if`

### 📌 Syntax

```bash
if [ condition ]; then
    commands
fi
```

### 💡 Example

```bash
if [ "$age" -ge 18 ]; then
    echo "You are an adult"
fi
```

---

## `if-else`

Used when there are **two possible outcomes**.

### 📌 Syntax

```bash
if [ condition ]; then
    commands
else
    commands
fi
```

### 💡 Example

```bash
if [ "$age" -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are a minor"
fi
```

---

## `if-elif-else`

Bash uses **`elif`** instead of `else if`.

### 📌 Syntax

```bash
if [ condition1 ]; then
    commands
elif [ condition2 ]; then
    commands
else
    commands
fi
```

### 💡 Example

```bash
if [ "$age" -ge 18 ]; then
    echo "Adult"
elif [ "$age" -ge 13 ]; then
    echo "Teenager"
else
    echo "Child"
fi
```

---

# 🔁 4. Loops

Loops are used to **repeat commands** multiple times.

---

## 🔄 `for` Loop

### 📌 Syntax

```bash
for variable in values
do
    commands
done
```

### 💡 Example

```bash
for number in 1 2 3 4 5
do
    echo "$number"
done
```

### ⚡ One-Line Syntax

```bash
for number in 1 2 3 4 5; do echo "$number"; done
```

---

## 🔄 `while` Loop

A `while` loop runs **as long as the condition is true**.

### 📌 Syntax

```bash
while [ condition ]
do
    commands
done
```

### 💡 Example

```bash
count=1

while [ "$count" -le 5 ]
do
    echo "$count"
    count=$((count + 1))
done
```

---

## 🔄 `do-while` Equivalent

⚠️ Bash does **not** have a traditional `do-while` loop.

You can achieve similar behavior using `while` with `break`.

### 📌 Syntax

```bash
while true
do
    commands

    if [ condition ]; then
        break
    fi
done
```

### 💡 Example

```bash
count=1

while true
do
    echo "$count"
    count=$((count + 1))

    if [ "$count" -gt 5 ]; then
        break
    fi
done
```

> 💡 This structure ensures the commands execute **at least once** before the exit condition is checked.

---

# 🔀 5. Switch Equivalent — `case`

Bash does not have a traditional `switch` statement.

Instead, Bash uses **`case`**.

### 📌 Syntax

```bash
case "$variable" in

    pattern1)
        commands
        ;;

    pattern2)
        commands
        ;;

    *)
        default_commands
        ;;

esac
```

### 🧠 Important

| Keyword | Purpose                   |
| ------- | ------------------------- |
| `case`  | Starts the case statement |
| `in`    | Begins pattern matching   |
| `;;`    | Ends a case option        |
| `*`     | Default case              |
| `esac`  | Ends the case statement   |

> 💡 `esac` is **`case` written backwards**.

---

## 💻 Examples of Switch — `case`

### 1. 📋 Menu Selection

```bash
#!/bin/bash

echo "1. Start"
echo "2. Stop"
echo "3. Restart"
echo "4. Exit"

read -p "Choose an option: " choice

case "$choice" in
    1)
        echo "Starting..."
        ;;
    2)
        echo "Stopping..."
        ;;
    3)
        echo "Restarting..."
        ;;
    4)
        echo "Exiting..."
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

---

### 2. 🌐 Check a Protocol

```bash
#!/bin/bash

read -p "Enter a protocol: " protocol

case "$protocol" in
    http)
        echo "HTTP uses port 80"
        ;;
    https)
        echo "HTTPS uses port 443"
        ;;
    ssh)
        echo "SSH uses port 22"
        ;;
    ftp)
        echo "FTP commonly uses port 21"
        ;;
    *)
        echo "Unknown protocol"
        ;;
esac
```

---

### 3. 🐧 Check Linux Distribution

```bash
#!/bin/bash

read -p "Enter your distribution: " distro

case "$distro" in
    ubuntu)
        echo "Ubuntu is Debian-based"
        ;;
    debian)
        echo "Debian is a Linux distribution"
        ;;
    fedora)
        echo "Fedora is RPM-based"
        ;;
    arch)
        echo "Arch Linux is independently developed"
        ;;
    *)
        echo "Unknown distribution"
        ;;
esac
```

---

### 4. 🔤 Matching Multiple Values

Multiple patterns can use the **same action**.

```bash
#!/bin/bash

read -p "Enter a letter: " letter

case "$letter" in
    a|e|i|o|u)
        echo "Vowel"
        ;;
    *)
        echo "Not a vowel"
        ;;
esac
```

### 🧠 Meaning of `|`

```bash
a|e|i|o|u)
```

means:

> `a` **OR** `e` **OR** `i` **OR** `o` **OR** `u`

---

### 5. 📁 Check File Extension

```bash
#!/bin/bash

read -p "Enter a filename: " file

case "$file" in
    *.txt)
        echo "Text file"
        ;;
    *.jpg|*.png)
        echo "Image file"
        ;;
    *.sh)
        echo "Bash script"
        ;;
    *.log)
        echo "Log file"
        ;;
    *)
        echo "Unknown file type"
        ;;
esac
```

### 🧠 Pattern Example

```bash
*.txt
```

means:

> Any filename that ends with `.txt`.

For example:

```text
notes.txt     ✅
report.txt    ✅
image.jpg     ❌
```

---

### ⭐ Quick `case` Structure

```text
Input
  ↓
case
  ↓
┌───────────────┐
│ Match Pattern │
└───────┬───────┘
        ↓
    Run Action
        ↓
      `;;`
        ↓
   Next Pattern
        ↓
       `*`
        ↓
     Default
        ↓
      `esac`
```

> 🎯 **Remember:** Bash uses `case` instead of a traditional `switch` statement.

# 📦 6. Arrays

Arrays allow you to **store multiple values in one variable**.

---

## 🆕 Creating an Array

### 📌 Syntax

```bash
array_name=(value1 value2 value3)
```

### 💡 Example

```bash
fruits=("Apple" "Banana" "Orange")
```

---

## 🔢 Accessing Array Elements

### 📌 Syntax

```bash
${array_name[index]}
```

### 💡 Example

```bash
echo "${fruits[0]}"
echo "${fruits[1]}"
echo "${fruits[2]}"
```

### 📤 Output

```text
Apple
Banana
Orange
```

> ⚠️ Bash arrays start with **index `0`**.

```text
Index:    0        1         2
          ↓        ↓         ↓
        Apple    Banana    Orange
```

---

## 📋 Getting All Array Elements

```bash
echo "${fruits[@]}"
```

This prints all elements of the array.

---

## 📏 Getting Array Length

```bash
echo "${#fruits[@]}"
```

This returns the **number of elements** in the array.

---

# 🔁 7. Looping Through an Array

You can use a `for` loop to process every element.

### 📌 Syntax

```bash
for item in "${array[@]}"
do
    commands
done
```

### 💡 Example

```bash
fruits=("Apple" "Banana" "Orange")

for fruit in "${fruits[@]}"
do
    echo "$fruit"
done
```

### 📤 Output

```text
Apple
Banana
Orange
```

---

# ⚡ 8. Quick Reference

| Feature          | Bash Syntax                              |
| ---------------- | ---------------------------------------- |
| 📝 Variable      | `name="value"`                           |
| ⌨️ Input         | `read name`                              |
| 🔀 If            | `if [ condition ]; then ... fi`          |
| 🔀 If-Else       | `if [ condition ]; then ... else ... fi` |
| 🔀 Else-If       | `elif [ condition ]; then`               |
| 🔁 For           | `for x in values; do ... done`           |
| 🔄 While         | `while [ condition ]; do ... done`       |
| 🔄 Do-While      | `while` + `break`                        |
| 🔀 Switch        | `case ... in ... esac`                   |
| 📦 Array         | `arr=(value1 value2)`                    |
| 🔢 Array Element | `${arr[0]}`                              |
| 📋 All Elements  | `${arr[@]}`                              |
| 📏 Array Length  | `${#arr[@]}`                             |

---

# 🧠 9. Important Bash Keywords

### 🔀 Conditions

```text
if       → Starts a condition
then     → Starts the true block
elif     → Checks another condition
else     → Runs when conditions are false
fi       → Ends the if statement
```

### 🔁 Loops

```text
for      → Starts a for loop
while    → Starts a while loop
do       → Starts the loop body
done     → Ends the loop
break    → Exits the loop
continue → Skips to the next iteration
```

### 🔀 Case

```text
case     → Starts case selection
in       → Defines patterns
;;       → Ends a case option
esac     → Ends the case statement
```

---

# 🚀 Bash Structure at a Glance

```text
🐚 Bash Scripting
│
├── 📝 Variables
│   ├── Assignment
│   └── Accessing values
│
├── ⌨️ User Input
│   └── read
│
├── 🔀 Conditions
│   ├── if
│   ├── if-else
│   └── if-elif-else
│
├── 🔁 Loops
│   ├── for
│   ├── while
│   └── do-while equivalent
│
├── 🔀 Selection
│   └── case
│
└── 📦 Arrays
    ├── Create
    ├── Access
    ├── Length
    └── Loop through
```

> 🎯 **Goal:** Learn these basic structures first. They form the foundation for writing useful Bash automation and cybersecurity scripts.
