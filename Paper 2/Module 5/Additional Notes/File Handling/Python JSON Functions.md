# 🐍 Python JSON Functions

JSON (JavaScript Object Notation) is a format used to store and exchange data between applications.

## 📑 Table of Contents

- [📦 Import the JSON Module](#-import-the-json-module)
- [📚 Main JSON Functions](#-main-json-functions)
- [`json.dumps()` — Convert to a JSON String](#1-jsondumps--convert-to-a-json-string)
- [`json.dump()` — Write to a JSON File](#2-jsondump--write-to-a-json-file)
- [`json.loads()` — Convert a JSON String into Python Data](#3-jsonloads--convert-a-json-string-into-python-data)
- [`json.load()` — Read a JSON File](#4-jsonload--read-a-json-file)
- [🧠 Easy Way to Remember](#-easy-way-to-remember)
- [🎯 Interview Tip](#-interview-tip)

---

## 📦 Import the JSON Module

```python
import json
```

## 📚 Main JSON Functions

| Function | Use | Simple Explanation |
|---|---|---|
| `json.dumps()` | Python data → JSON string | Converts Python data into a JSON-formatted string |
| `json.dump()` | Python data → JSON file | Writes Python data into a JSON file |
| `json.loads()` | JSON string → Python data | Converts a JSON string into Python data |
| `json.load()` | JSON file → Python data | Reads JSON data from a file |
| `json.JSONEncoder()` | Custom encoding | Helps customize how Python objects are converted to JSON |
| `json.JSONDecoder()` | Custom decoding | Helps customize how JSON strings are decoded |

---

## 1. `json.dumps()` — Convert to a JSON String

```python
import json

student = {"name": "Shynu", "age": 18}

result = json.dumps(student)

print(result)
print(type(result))
```

**Output:**

```text
{"name": "Shynu", "age": 18}
<class 'str'>
```

**Explanation:** `json.dumps()` converts Python data into a JSON-formatted string.

## 2. `json.dump()` — Write to a JSON File

```python
import json

student = {"name": "Shynu", "age": 18}

with open("student.json", "w") as file:
    json.dump(student, file)
```

**Explanation:** This writes the data into `student.json`.

## 3. `json.loads()` — Convert a JSON String into Python Data

```python
import json

data = '{"name": "Shynu", "age": 18}'

result = json.loads(data)

print(result["name"])
```

**Output:**

```text
Shynu
```

**Explanation:** `json.loads()` converts a JSON string into Python data. Here, `result` becomes a Python dictionary.

## 4. `json.load()` — Read a JSON File

Suppose `student.json` contains:

```json
{
    "name": "Shynu",
    "age": 18
}
```

**Python code:**

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
```

**Output:**

```text
Shynu
```

**Explanation:** `json.load()` reads the JSON file and converts its contents into Python data.

---

## 🧠 Easy Way to Remember

| Function | Remember It As |
|---|---|
| `dump()` | Write data to a file |
| `load()` | Read data from a file |
| `dumps()` | Convert data to a JSON string |
| `loads()` | Convert a JSON string into Python data |

### 🔑 Quick Rule

- `dump()` and `load()` work with file objects.
- `dumps()` and `loads()` work with strings.

## 🎯 Interview Tip

The four main JSON functions to learn first are:

1. `json.dump()`
2. `json.dumps()`
3. `json.load()`
4. `json.loads()`

Remember: **`dump` = file writing, `load` = file reading, `dumps` = string conversion, and `loads` = string parsing.**
