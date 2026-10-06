# 🐍 Python Data Types

Python has different **data types** for storing different kinds of values. Think of a data type as a type of **box** used to store a particular kind of information.

---

## 📋 Table of Contents

- [📝 Text Type — `str`](#-1-text-type--str)
- [🔢 Numeric Types](#-2-numeric-types)
  - [`int` — Integer](#-int--integer)
  - [`float` — Floating-Point Number](#-float--floating-point-number)
  - [`complex` — Complex Number](#-complex--complex-number)
- [📦 Sequence Types](#-3-sequence-types)
  - [`list`](#-list)
  - [`tuple`](#-tuple)
  - [`range`](#-range)
- [🗂️ Mapping Type — `dict`](#-4-mapping-type--dict)
- [🔵 Set Types](#-5-set-types)
  - [`set`](#-set)
  - [`frozenset`](#-frozenset)
- [✅ Boolean Type — `bool`](#-6-boolean-type--bool)
- [💾 Binary Types](#-7-binary-types)
  - [`bytes`](#-bytes)
  - [`bytearray`](#-bytearray)
  - [`memoryview`](#-memoryview)
- [🚫 None Type — `NoneType`](#-8-none-type--nonetype)
- [🧠 Quick Revision](#-quick-revision-table)
- [⭐ Important Types to Learn First](#-important-types-to-learn-first)

---

## 📊 Overview

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

# 📝 1. Text Type — `str`

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

[⬆️ Back to Top](#-python-data-types)

---

# 🔢 2. Numeric Types

Python has three main numeric data types:

- `int`
- `float`
- `complex`

---

## 🔹 `int` — Integer

Used for **whole numbers**.

```python
age = 18
marks = 95
```

There is no decimal point.

[⬆️ Back to Top](#-python-data-types)

---

## 🔹 `float` — Floating-Point Number

Used for numbers containing **decimal values**.

```python
height = 172.5
price = 99.99
```

[⬆️ Back to Top](#-python-data-types)

---

## 🔹 `complex` — Complex Number

Used for **complex mathematical numbers**.

```python
z = 3 + 4j
```

Here, `j` represents the **imaginary part**.

[⬆️ Back to Top](#-python-data-types)

---

# 📦 3. Sequence Types

Sequence types store **multiple values in an ordered way**.

Python has three common sequence types:

- `list`
- `tuple`
- `range`

---

## 🔹 `list`

A list is an **ordered and changeable** collection.

```python
fruits = ["apple", "banana", "mango"]
```

You can change
