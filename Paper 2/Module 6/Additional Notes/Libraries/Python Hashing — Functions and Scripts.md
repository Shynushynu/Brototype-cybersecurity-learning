# 🔐 Python Hashing — Functions and Scripts

Python provides the `hashlib` module for hashing text, files, and other data.

In cybersecurity, hashing is commonly used for:

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [📚 1. Important Functions in `hashlib`](#-1-important-functions-in-hashlib)
- [🧪 2. Script 1 — Hash Text Using SHA-256](#-2-script-1--hash-text-using-sha-256)
- [📁 3. Script 2 — Calculate a File Hash](#-3-script-2--calculate-a-file-hash)
- [🛡️ 4. Script 3 — Detect File Changes](#️-4-script-3--detect-file-changes)
- [🔄 5. Script 4 — Compare Two Files](#-5-script-4--compare-two-files)
- [⚙️ 6. Script 5 — Use `hashlib.new()`](#️-6-script-5--use-hashlibnew)
- [🧠 7. Quick Revision](#-7-quick-revision)
- [🔐 8. Hashing in Cybersecurity](#-8-hashing-in-cybersecurity)
- [🚀 9. Practical Project Idea](#-9-practical-project-idea)
- [✅ Conclusion](#-conclusion)

---

## 📚 1. Important Functions in `hashlib`

| Function / Method | Purpose |
|---|---|
| `hashlib.sha256()` | Creates a SHA-256 hash object |
| `hashlib.sha1()` | Creates a SHA-1 hash object; avoid for security-sensitive integrity uses |
| `hashlib.md5()` | Creates an MD5 hash object; not suitable for security-sensitive integrity uses |
| `hashlib.sha512()` | Creates a SHA-512 hash object |
| `hashlib.blake2b()` | Creates a BLAKE2b hash object |
| `hashlib.new()` | Creates a hash object using a supported algorithm name |
| `.update(data)` | Adds bytes to the data being hashed |
| `.hexdigest()` | Returns the hash as hexadecimal text |
| `.digest()` | Returns the raw hash bytes |
| `.copy()` | Copies the current hash object's state |
| `hashlib.file_digest()` | Hashes a file using a supported digest algorithm (Python 3.11+) |
| `hashlib.algorithms_available` | Lists algorithms available in the current Python environment |
| `hashlib.pbkdf2_hmac()` | Derives a key from a password using PBKDF2 |

### Other Useful Function

- `hmac.compare_digest(a, b)` — Compares values safely when comparing security-sensitive digests.

---

## 🧪 2. Script 1 — Hash Text Using SHA-256

### 💻 Code

```python
import hashlib

text = "Hello World"

hash_object = hashlib.sha256(text.encode())
hash_value = hash_object.hexdigest()

print("Original Text:", text)
print("SHA-256 Hash:", hash_value)
```

### 🔍 Explanation

1. `text.encode()` converts the string into bytes.
2. `hashlib.sha256()` creates a SHA-256 hash object.
3. `.hexdigest()` returns the hash as hexadecimal text.
4. `print()` displays the text and its hash.

### 🎯 Use Case

Generate a hash to help verify whether data has changed.

---

## 📁 3. Script 2 — Calculate a File Hash

This script calculates the SHA-256 hash of a file such as `test.txt`.

### 💻 Code

```python
import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


file_path = "test.txt"

result = calculate_hash(file_path)

print("File:", file_path)
print("SHA-256:", result)
```

### 🔍 Explanation

| Function / Statement | Purpose |
|---|---|
| `open(file_path, "rb")` | Opens the file in binary mode |
| `file.read(4096)` | Reads up to 4096 bytes at a time |
| `sha256.update(data)` | Processes each chunk of data |
| `sha256.hexdigest()` | Returns the final hash |
| `return` | Sends the calculated hash back to the caller |

### 🎯 Use Case

Calculate a file's hash without loading the entire file into memory.

---

## 🛡️ 4. Script 3 — Detect File Changes

This example introduces file change detection using hashes.

### 💻 Code

```python
import hashlib
import time

def CalculateHash(file_path):
    sha256=hashlib.sha256()
    with open(file_path,"rb")as file:
        while True:
            data=file.read(4096)
            if not data:
                break
            sha256.update(data)
    hashVal=sha256.hexdigest()
    return hashVal
try:
    file_path="test.py"
    OrginalHash=CalculateHash(file_path)
    print("Orginal hash obtaied")
    print("Monitoring:",file_path)
    while True:
        time.sleep(5)
        hashVal=CalculateHash(file_path)
        if hashVal!=OrginalHash:
            print("Alert!! File content changed......")
            OrginalHash=hashVal
        else:
            print("File unchanged")
except FileNotFoundError:
    print(f"File:{file_path} is not found")
except KeyboardInterrupt:
    print("Monitoring stoped...")
```

### 🔍 Explanation

1. Calculate the original file hash.
2. Calculate the file hash again.
3. Compare both hash values.
4. If the values differ, the file contents have changed.

> ⚠️ **Important:** Both hashes in this example are calculated consecutively. To detect changes made later, save the original hash and compare it during a subsequent check.

### 🎯 Use Case

- File integrity monitoring
- Detecting unexpected file modifications
- Security monitoring automation

---

## 🔄 5. Script 4 — Compare Two Files

This script compares two files using their SHA-256 hashes.

### 💻 Code

```python
import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for data in iter(lambda: file.read(4096), b""):
            sha256.update(data)

    return sha256.hexdigest()


file1 = calculate_hash("file1.txt")
file2 = calculate_hash("file2.txt")

if file1 == file2:
    print("Both files have identical contents.")
else:
    print("The files have different contents.")
```

### 🔍 Explanation

- `calculate_hash()` calculates the hash of each file.
- `==` compares the resulting hash strings.
- Matching hashes indicate that the file contents are almost certainly identical.
- Different hashes indicate that the file contents differ.

### 🎯 Use Case

Verify whether a downloaded file matches a trusted copy by comparing their hashes.

---

## ⚙️ 6. Script 5 — Use `hashlib.new()`

The `hashlib.new()` function creates a hash object using an algorithm name.

### 💻 Code

```python
import hashlib

text = b"Cybersecurity"

hash_object = hashlib.new("sha256")
hash_object.update(text)

print(hash_object.hexdigest())
```

### 🔍 Explanation

1. `hashlib.new("sha256")` creates a SHA-256 hash object.
2. `.update(text)` processes the supplied bytes.
3. `.hexdigest()` returns the final hash as hexadecimal text.

You can use other supported algorithms, such as `"sha512"`.

### 🎯 Use Case

Select a supported hashing algorithm dynamically in a Python program.

---

## 🧠 7. Quick Revision

| Task | Function / Method |
|---|---|
| Create a SHA-256 hash | `hashlib.sha256()` |
| Create a hash by name | `hashlib.new()` |
| Process data | `.update()` |
| Get a hexadecimal hash | `.hexdigest()` |
| Get raw digest bytes | `.digest()` |
| Copy hash state | `.copy()` |
| List supported algorithms | `hashlib.algorithms_available` |
| Hash a file using a helper | `hashlib.file_digest()` |
| Compare sensitive digest values | `hmac.compare_digest()` |

---

## 🔐 8. Hashing in Cybersecurity

### Common Applications

1. **File Integrity Monitoring:** Detect unexpected changes to files.
2. **File Verification:** Compare a file's hash with a trusted hash value.
3. **Security Automation:** Trigger alerts when monitored files change.
4. **Incident Investigation:** Help verify whether collected files have changed.
5. **Password Storage:** Use dedicated password-hashing algorithms rather than plain SHA-256.

### ⚠️ Security Note

Never store passwords using plain SHA-256, MD5, or SHA-1.

Password storage should use a dedicated password-hashing algorithm such as:

- Argon2id
- scrypt
- PBKDF2 with an appropriate configuration and a unique salt

Hashing is designed to be one-way, unlike encryption, which is designed to be reversible using the appropriate key.

---

## 🚀 9. Practical Project Idea

### Python File Integrity Monitor

Build a program that:

1. Calculates the original SHA-256 hash of a file.
2. Saves the hash for future comparison.
3. Recalculates the hash during a later check.
4. Compares the saved hash with the current hash.
5. Detects changes in the file contents.
6. Sends a Gmail alert when an unexpected change is detected.

### 🛠️ Concepts Covered

- Python functions
- File handling
- The `hashlib` module
- Binary file reading
- Hash comparison
- Change detection
- Security automation
- Email alerting

---

## ✅ Conclusion

Hashing is an important cybersecurity technique for checking data integrity and verifying files.

Python's `hashlib` module makes it possible to calculate hashes, compare files, and build automated file integrity monitoring tools.
