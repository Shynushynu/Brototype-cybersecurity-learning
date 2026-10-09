# 🐍 Python File Handling Methods

## 📌 Overview

Python provides several file-handling methods to read, write, and manage files. These methods help us control where we read or write content and how we access information stored in files.

## 📚 Methods Covered

1. `seek()`
2. `read()`
3. `readline()`
4. `readlines()`
5. `write()`
6. `writelines()`
7. `tell()`

---

## 📍 1. `seek()` — Move the File Pointer

The `seek()` method moves the file pointer to a specific position in a file.

### Syntax

```python
file.seek(position)
```

### Example

```python
with open("data.txt", "r") as file:
    file.seek(2)
    print(file.read())
```

If `data.txt` contains `Python`, the output is:

```text
thon
```

**Explanation:**
- `seek(2)` moves the pointer to position 2.
- Python uses zero-based positions, so position 2 points to `t`.
- `read()` reads the remaining content.

---

## 📖 2. `read()` — Read File Content

The `read()` method reads content from the current file pointer position.

### Syntax

```python
file.read()
file.read(size)
```

### Example

```python
with open("data.txt", "r") as file:
    print(file.read(3))
```

If the file contains `Python`, the output is:

```text
Pyt
```

**Explanation:**
- `read()` reads all remaining content.
- `read(3)` reads up to 3 characters.

---

## 📄 3. `readline()` — Read One Line

The `readline()` method reads one line at a time from a file.

### Example

```python
with open("data.txt", "r") as file:
    print(file.readline())
```

If the file contains:

```text
Hello
World
```

The first call reads the first line, `Hello`.

**Remember:** Calling `readline()` again reads the next line, if one exists.

---

## 📋 4. `readlines()` — Read All Lines

The `readlines()` method reads the remaining lines and returns them as a list of strings.

### Example

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

If the file contains two lines, the output may be:

```python
['Hello\n', 'World']
```

**Remember:** The `\n` represents a newline character.

---

## ✍️ 5. `write()` — Write Content

The `write()` method writes a string to a file at the current file pointer position.

### Example

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

This writes `Hello` to the file.

**Important:** Opening an existing file in `"w"` mode erases its previous content.

---

## 📝 6. `writelines()` — Write Multiple Strings

The `writelines()` method writes multiple strings to a file.

### Example

```python
with open("data.txt", "w") as file:
    file.writelines(["Hello\n", "World\n"])
```

The file contains:

```text
Hello
World
```

**Important:** `writelines()` does not automatically add newline characters. Use `\n` when you want separate lines.

---

## 📍 7. `tell()` — Find the File Pointer Position

The `tell()` method returns the current file pointer position.

### Example

```python
with open("data.txt", "r") as file:
    print(file.tell())
    file.read(2)
    print(file.tell())
```

If the file contains `Python`, the output on a typical text file using UTF-8 is:

```text
0
2
```

**Explanation:**
- `tell()` initially reports position `0`.
- `read(2)` reads two characters.
- The next `tell()` reports the new position.

Note: In text mode, `tell()` returns a position marker suitable for restoring the file position; it is not always a simple character count.

---

## 🔄 `seek()` vs `tell()`

| Method | Purpose |
|---|---|
| `seek()` | Moves the file pointer |
| `tell()` | Reports the current file position |

### Example

```python
with open("data.txt", "r") as file:
    file.seek(3)
    print(file.tell())
```

Output:

```text
3
```

---

## 🧠 Quick Revision

| Method | Simple meaning |
|---|---|
| `seek()` | Move the pointer |
| `read()` | Read content |
| `readline()` | Read one line |
| `readlines()` | Read lines into a list |
| `write()` | Write a string |
| `writelines()` | Write multiple strings |
| `tell()` | Check the current position |

---

## 🎯 Practice Question

Suppose `data.txt` contains:

```text
Python
```

What will this program print?

```python
with open("data.txt", "r") as file:
    print(file.tell())
    file.read(2)
    print(file.tell())
```

**Options:**

- A. `0` then `2`
- B. `1` then `2`
- C. `0` then `3`
- D. An error occurs

Try answering before checking the result!

---

## ✅ Key Takeaway

Python file-handling methods help us control how data is read, written, and accessed. Understanding `seek()` and `tell()` is especially useful when you need to manage the file pointer.
