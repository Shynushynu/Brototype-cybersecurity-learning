# 🐍 Python Data Types

Python has different **data types** for storing different kinds of values. Think of a data type as a type of **box** used to store a particular kind of information.

---

## 📋 Overview

| Category | Data Types |
| :--- | :--- |
| 📝 Text Type | `str` |
| 🔢 Numeric Types | `int`, `float`, `complex` |
| 📦 Sequence Types | `list`, `tuple`, `range` |
| 🗂️ Mapping Type | `dict` |
| 🔵 Set Types | `set`, `frozenset` |
| ✅ Boolean Type | `bool` |
| 💾 Binary Types | `bytes`, `bytearray`, `memoryview` |
| 🚫 None Type | `NoneType` |

---

## 📝 1. Text Type — `str`

`str` is used to store **text or characters**.

```python
name = "Shynu"
message = "Hello World"
```

Text is usually written inside quotes:

```python
"Hello"
'Python'
```

### Accessing Characters

You can access individual characters using an index.

```python
name = "Shynu"

print(name[0])
```

**Output:**

```text
S
```

---

## 🔢 2. Numeric Types

Python has three main numeric data types:

- `int`
- `float`
- `complex`

### 🔹 `int` — Integer

Used for **whole numbers**.

```python
age = 18
marks = 95
```

There is no decimal point.

---

### 🔹 `float` — Floating-Point Number

Used for numbers containing **decimal values**.

```python
height = 172.5
price = 99.99
```

---

### 🔹 `complex` — Complex Number

Used for **complex mathematical numbers**.

```python
z = 3 + 4j
```

Here, `j` represents the **imaginary part**.

---

## 📦 3. Sequence Types

Sequence types store **multiple values in an ordered way**.

Python has three common sequence types:

- `list`
- `tuple`
- `range`

---

### 🔹 `list`

A list is an **ordered and changeable** collection.

```python
fruits = ["apple", "banana", "mango"]
```

You can change an element:

```python
fruits[0] = "orange"
```

Now:

```text
["orange", "banana", "mango"]
```

---

### 🔹 `tuple`

A tuple is **ordered but cannot be changed** after creation.

```python
coordinates = (10, 20)
```

You cannot modify its elements:

```python
coordinates[0] = 50  # ❌ Error
```

### Key Point

> `list` → Changeable  
> `tuple` → Unchangeable

---

### 🔹 `range`

`range` is used to generate a **sequence of numbers**.

```python
numbers = range(5)
```

This represents:

```text
0, 1, 2, 3, 4
```

It is commonly used with loops.

```python
for number in range(5):
    print(number)
```

---

## 🗂️ 4. Mapping Type — `dict`

A dictionary stores data as **key-value pairs**.

```python
student = {
    "name": "Shynu",
    "age": 18,
    "course": "Cybersecurity"
}
```

### Accessing a Value

You access a value using its key.

```python
print(student["name"])
```

**Output:**

```text
Shynu
```

Think of a dictionary like this:

```text
key       → value
--------------------
name      → Shynu
age       → 18
course    → Cybersecurity
```

---

## 🔵 5. Set Types

Python has two set-related types:

- `set`
- `frozenset`

---

### 🔹 `set`

A set stores **unique values** and does not maintain an index-based order.

```python
numbers = {1, 2, 3, 3, 4}
```

The duplicate `3` is removed.

```text
{1, 2, 3, 4}
```

You cannot access a set using an index:

```python
numbers[0]  # ❌ Error
```

### Key Point

> A `set` is useful when you want to store **unique values**.

---

### 🔹 `frozenset`

A `frozenset` is an **unchangeable set**.

```python
numbers = frozenset([1, 2, 3])
```

You cannot add or remove elements from a `frozenset`.

### Key Point

> `set` → Changeable  
> `frozenset` → Unchangeable

---

## ✅ 6. Boolean Type — `bool`

`bool` represents one of two values:

```python
True
False
```

Example:

```python
is_logged_in = True
is_admin = False
```

Booleans are commonly used in **conditions**.

```python
age = 18

print(age >= 18)
```

**Output:**

```text
True
```

---

## 💾 7. Binary Types

Binary types are used for working with **binary data**.

Python has three binary-related types:

- `bytes`
- `bytearray`
- `memoryview`

---

### 🔹 `bytes`

`bytes` stores **immutable binary data**.

```python
data = b"Hello"
```

The `b` before the string indicates bytes.

---

### 🔹 `bytearray`

`bytearray` is similar to `bytes`, but it is **changeable**.

```python
data = bytearray(b"Hello")
```

---

### 🔹 `memoryview`

`memoryview` allows you to access the memory of binary data **without creating a copy**.

```python
data = memoryview(b"Hello")
```

Binary types are commonly encountered when working with:

- 📁 Files
- 🌐 Networking
- 🔐 Encryption
- ⚙️ Low-level data

---

## 🚫 8. None Type — `NoneType`

`None` represents **no value** or the **absence of a value**.

```python
result = None
```

For example:

```python
username = None
```

This could mean:

> "We don't have a username yet."

You can check for `None` using `is`.

```python
if username is None:
    print("Username not available")
```

---

# 🧠 Quick Revision Table

| Data Type | Simple Meaning | Example |
| :--- | :--- | :--- |
| `str` | Text | `"Hello"` |
| `int` | Whole number | `10` |
| `float` | Decimal number | `10.5` |
| `complex` | Complex number | `3 + 4j` |
| `list` | Changeable collection | `[1, 2, 3]` |
| `tuple` | Unchangeable collection | `(1, 2, 3)` |
| `range` | Sequence of numbers | `range(5)` |
| `dict` | Key → value | `{"name": "Shynu"}` |
| `set` | Unique values | `{1, 2, 3}` |
| `frozenset` | Unchangeable set | `frozenset([1, 2])` |
| `bool` | True/False | `True` |
| `bytes` | Binary data | `b"Hello"` |
| `bytearray` | Changeable binary data | `bytearray(b"Hi")` |
| `memoryview` | View of binary memory | `memoryview(b"Hi")` |
| `NoneType` | No value | `None` |

---

## ⭐ Important Types to Learn First

For **Python fundamentals**, focus on these first:

```text
str
int
float
bool
list
tuple
set
dict
```

Once these are clear, the other data types will be much easier to understand.
