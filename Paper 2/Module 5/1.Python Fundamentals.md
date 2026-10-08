# 🐍 Python Fundamentals

> **Python fundamentals** are the basic concepts needed to write, understand, and maintain Python programs.

---

## 📚 Topics Covered

1. 🔤 [Variables and Data Types](#1--variables-and-data-types)
2. ➕ [Operators](#2--operators)
3. ⌨️ [Input and Output](#3--input-and-output)
4. 🔄 [Type Conversion](#4--type-conversion)
5. 🧹 [Python Coding Practices](#5--python-coding-practices)

---

# 1. 🔤 Variables and Data Types

A **variable** is a name used to store a value.

### 💻 Example

```python
name = "Shynu"
age = 18
height = 172.5
```

### 📦 Common Data Types

| Data Type | Example | Purpose |
|---|---|---|
| `str` | `"Hello"` | 📝 Text |
| `int` | `18` | 🔢 Whole numbers |
| `float` | `172.5` | 🔢 Decimal numbers |
| `bool` | `True` | ✅ True/False |
| `list` | `[1, 2, 3]` | 📋 Multiple values |
| `tuple` | `(1, 2, 3)` | 🔒 Fixed collection |
| `dict` | `{"name": "Shynu"}` | 🗂️ Key-value data |
| `set` | `{1, 2, 3}` | 🎯 Unique values |

---

# 2. ➕ Operators

**Operators** are symbols used to perform operations on values.

## 🧮 Arithmetic Operators

```python
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Remainder
```

### 📌 Common Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 3` |
| `-` | Subtraction | `10 - 3` |
| `*` | Multiplication | `10 * 3` |
| `/` | Division | `10 / 3` |
| `%` | Remainder | `10 % 3` |

---

## ⚖️ Comparison Operators

Comparison operators are used to **compare two values**.

```python
a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `==` | Equal to |
| `!=` | Not equal to |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## 🧠 Logical Operators

Logical operators are used to combine conditions.

```python
and
or
not
```

### Example

```python
age = 18

print(age >= 18 and age <= 60)
```

---

# 3. ⌨️ Input and Output

## 📤 Output

`print()` is used to display information on the screen.

```python
print("Hello World")
```

### Example

```python
name = "Shynu"
print("Hello", name)
```

---

## 📥 Input

`input()` is used to get information from the user.

```python
name = input("Enter your name: ")
print("Hello", name)
```

> ⚠️ **Important:** `input()` normally returns the entered value as a **string**.

---

# 4. 🔄 Type Conversion

**Type conversion** means changing a value from one data type to another.

### 🔧 Common Conversions

```python
int("10")       # String → Integer
float("10.5")   # String → Float
str(100)        # Integer → String
```

### 💻 Example

```python
age = input("Enter your age: ")
age = int(age)

print(age)
```

### 🧪 Practical Example

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Here:

```text
input() → string
       ↓
     int()
       ↓
   integer
```

---

# 5. 🧹 Python Coding Practices

Good coding practices make programs:

- 📖 Easy to read
- 🔧 Easy to maintain
- 🐛 Easier to debug
- 🤝 Easier for others to understand

---

## 🏷️ Use Meaningful Variable Names

❌ **Bad:**

```python
x = 18
```

✅ **Better:**

```python
age = 18
```

---

## 📐 Use Proper Indentation

Python uses indentation to define blocks of code.

```python
if age >= 18:
    print("Adult")
```

⚠️ Incorrect indentation can cause errors.

---

## 💬 Use Comments

Comments help explain what the code does.

```python
# Check whether the user is an adult
if age >= 18:
    print("Adult")
```

---

## 🧩 Keep Code Simple

Avoid unnecessary complexity.

```python
name = input("Enter your name: ")
print("Hello", name)
```

Simple and readable code is easier to understand.

---

## 📏 Follow PEP 8

**PEP 8** is Python's official style guide.

It provides recommendations for:

- ✨ Code formatting
- 🏷️ Naming conventions
- 📐 Indentation
- 📄 Code layout
- 👀 Readability

---

# 🔐 Python in Cybersecurity

Python is widely used in cybersecurity for tasks such as:

- 🔎 Log analysis
- 🌐 Network scanning
- 🤖 Security automation
- 📊 Data analysis
- 🛡️ Threat detection
- ⚙️ Security tools and scripts

### Example

```python
ip = input("Enter an IP address: ")
print("Checking:", ip)
```

This demonstrates how Python can accept information that could later be used in a security script.

---

# 🎯 Interview Answer

> **Python fundamentals include variables and data types, operators, input and output, type conversion, and good coding practices. These concepts are the foundation for writing clear, readable, and functional Python programs.**

---

## 🧠 Quick Revision

```text
🐍 Python Fundamentals
│
├── 🔤 Variables & Data Types
├── ➕ Operators
├── ⌨️ Input & Output
├── 🔄 Type Conversion
└── 🧹 Coding Practices
```

> ⭐ **Remember:** Learn these basics well before moving to advanced Python concepts.
