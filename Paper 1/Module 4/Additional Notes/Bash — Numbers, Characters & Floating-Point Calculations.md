# 🐚 Bash — Numbers, Characters & Floating-Point Calculations

> 🧑‍💻 Learn how Bash handles **integers, floating-point numbers, characters, strings, and arithmetic calculations**.

---

## 📑 Contents

* [🔢 Integer Arithmetic](#-integer-arithmetic)
* [🔢 Floating-Point Numbers](#-floating-point-numbers)
* [🧮 The `bc` Command](#-the-bc-command)
* [🔤 Characters in Bash](#-characters-in-bash)
* [✂️ Extracting a Character](#️-extracting-a-character)
* [📊 Bash Data Types](#-bash-data-types)
* [⚡ Quick Reference](#-quick-reference)

---

# 🔢 Integer Arithmetic

Bash can perform basic arithmetic using:

```bash
$(( expression ))
```

### 💡 Example

```bash
a=10
b=5

result=$((a + b))

echo "$result"
```

**Output:**

```text
15
```

### ➕ Supported Operators

| Operation      | Operator | Example       |
| -------------- | -------: | ------------- |
| Addition       |      `+` | `$((10 + 5))` |
| Subtraction    |      `-` | `$((10 - 5))` |
| Multiplication |      `*` | `$((10 * 5))` |
| Division       |      `/` | `$((10 / 5))` |
| Remainder      |      `%` | `$((10 % 3))` |

---

# 🔢 Floating-Point Numbers

> ⚠️ Bash's built-in `$(( ))` arithmetic works with **integers**, not decimal/floating-point numbers.

### ❌ Integer Division

```bash
result=$((5 / 2))

echo "$result"
```

**Output:**

```text
2
```

Even though mathematically:

```text
5 ÷ 2 = 2.5
```

Bash's integer arithmetic gives:

```text
5 / 2 → 2
```

---

## ✅ Floating-Point Division with `bc`

For decimal calculations, we can use the **`bc` (Basic Calculator)** command.

```bash
result=$(echo "5 / 2" | bc -l)

echo "$result"
```

**Output:**

```text
2.50000000000000000000
```

### 🔍 How it works

```text
┌──────────────┐
│ echo "5 / 2" │
└──────┬───────┘
       │
       │  pipe |
       ▼
┌──────────────┐
│    bc -l     │
└──────┬───────┘
       │
       ▼
  2.500000...
```

* `echo` → sends the expression
* `|` → sends the output to the next command
* `bc` → performs the calculation
* `-l` → loads the math library

---

# 🧮 The `bc` Command

`bc` stands for **Basic Calculator**.

It is useful when Bash's built-in arithmetic isn't enough, especially for **floating-point calculations**.

### 📌 Basic Syntax

```bash
echo "expression" | bc
```

### 📌 Floating-Point Syntax

```bash
echo "expression" | bc -l
```

---

## 🎯 Controlling Decimal Places

Use `scale` to specify how many decimal places you want.

```bash
result=$(echo "scale=2; 5 / 2" | bc)

echo "$result"
```

**Output:**

```text
2.50
```

### 🧠 Example

```bash
echo "scale=3; 10 / 3" | bc
```

**Output:**

```text
3.333
```

---

## 🔬 Mathematical Functions

`bc -l` also provides mathematical functions.

### Square Root

```bash
echo "sqrt(25)" | bc -l
```

**Output:**

```text
5.00000000000000000000
```

### 📌 Important

```bash
bc -l
```

* `bc` → Basic Calculator
* `-l` → loads the **math library**

> ⚠️ **Important:** `-l` is a lowercase **letter L**, not the number `1`.

```text
-l  ✅
-1  ❌
```

---

# 🔤 Characters in Bash

Bash does **not** have a separate `char` data type like C or Java.

A single character can simply be stored as a **string**.

### 💡 Example

```bash
letter="A"

echo "$letter"
```

**Output:**

```text
A
```

You can also store multiple characters:

```bash
letter="ABC"

echo "$letter"
```

---

# ⌨️ Taking Character Input

You can use `read` to take input from the user.

```bash
read -p "Enter a character: " letter

echo "$letter"
```

Example:

```text
Enter a character: A
A
```

> 💡 Bash doesn't automatically restrict the input to one character.

---

# ✂️ Extracting a Character

If you have a string and want to extract a specific character, use **substring expansion**.

### 📌 Syntax

```bash
${variable:start:length}
```

### 💡 Example

```bash
word="Hello"

first=${word:0:1}

echo "$first"
```

**Output:**

```text
H
```

### 🔢 Character Positions

```text
H   e   l   l   o
↑   ↑   ↑   ↑   ↑
0   1   2   3   4
```

Therefore:

```bash
${word:0:1}    # H
${word:1:1}    # e
${word:2:1}    # l
```

---

# 📊 Bash Data Types

Bash is **not strongly typed** like languages such as C or Java.

| Type         | Bash Example      | Notes                                        |
| ------------ | ----------------- | -------------------------------------------- |
| 🔢 Integer   | `age=18`          | Supported directly                           |
| 🔢 Float     | `2.5`             | Use tools such as `bc`                       |
| 🔤 Character | `letter="A"`      | Stored as a string                           |
| 📝 String    | `name="Shynu"`    | Commonly used                                |
| 📦 Array     | `items=("A" "B")` | Stores multiple values                       |
| ✅ Boolean    | `true` / `false`  | Usually handled through commands/exit status |

---

# ⚡ Quick Reference

### 🔢 Integer

```bash
result=$((10 + 5))
```

### 🧮 Floating Point

```bash
result=$(echo "5 / 2" | bc -l)
```

### 🎯 Decimal Places

```bash
result=$(echo "scale=2; 5 / 2" | bc)
```

### 🔤 Character

```bash
letter="A"
```

### ✂️ First Character

```bash
first=${word:0:1}
```

### 🧮 Square Root

```bash
echo "sqrt(25)" | bc -l
```

---

# 🧠 Key Points to Remember

```text
🐚 Bash
│
├── 🔢 Integer arithmetic
│   └── $(( ))
│
├── 🧮 Floating-point arithmetic
│   └── bc -l
│
├── 🔤 Character
│   └── Stored as a string
│
├── 📝 String
│   └── "Hello"
│
└── 📦 Array
    └── ("A" "B" "C")
```

> 🚀 **Remember:** Bash handles integer arithmetic directly. For floating-point calculations, tools such as `bc` are commonly used. Bash also treats individual characters as strings rather than having a separate `char` type.
