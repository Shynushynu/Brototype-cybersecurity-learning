# 🐍 Python CSV Module

## 📌 Overview

Python's built-in `csv` module helps us read, write, and manage CSV (Comma-Separated Values) files.

CSV files store data in rows and columns, similar to a spreadsheet.

## 📚 Table of Contents

- [📌 Overview](#-overview)
- [1. `csv.reader()` — Read CSV Data](#1-csvreader--read-csv-data)
- [2. `csv.writer()` — Write CSV Data](#2-csvwriter--write-csv-data)
- [3. `writerow()` — Write One Row](#3-writerow--write-one-row)
- [4. `writerows()` — Write Multiple Rows](#4-writerows--write-multiple-rows)
- [5. `csv.DictReader()` — Read Rows as Dictionaries](#5-csvdictreader--read-rows-as-dictionaries)
- [6. `csv.DictWriter()` — Write Dictionaries to CSV](#6-csvdictwriter--write-dictionaries-to-csv)
- [7. `writeheader()` — Write Column Names](#7-writeheader--write-column-names)
- [8. Handling Commas Inside Values](#8-handling-commas-inside-values)
- [9. Understanding `newline=""`](#9-understanding-newline)
- [10. Quick Revision](#10-quick-revision)
- [11. Practice Question](#11-practice-question)
- [12. Key Takeaway](#12-key-takeaway)

---

## 1. `csv.reader()` — Read CSV Data

The `csv.reader()` function reads CSV data row by row and returns each row as a list of strings.

### Example

Suppose `users.csv` contains:

```csv
name,age
Alex,20
Sam,22
```

Python code:

```python
import csv

with open("users.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['name', 'age']
['Alex', '20']
['Sam', '22']
```

**Explanation:**
- `import csv` makes the CSV module available.
- `csv.reader(file)` reads CSV rows.
- `for row in reader` processes one row at a time.
- Values returned by `csv.reader()` are normally strings.

---

## 2. `csv.writer()` — Write CSV Data

The `csv.writer()` function creates a writer object that writes correctly formatted CSV data.

### Example

```python
import csv

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Alex", 20])
    writer.writerow(["Sam", 22])
```

The resulting file contains:

```csv
name,age
Alex,20
Sam,22
```

**Important:** Opening a file with `"w"` erases its previous content.

---

## 3. `writerow()` — Write One Row

The `writerow()` method writes one row of data to a CSV file.

### Example

```python
import csv

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Alex", 20])
```

Result:

```csv
Alex,20
```

**Remember:** `writerow()` writes one row at a time.

---

## 4. `writerows()` — Write Multiple Rows

The `writerows()` method writes multiple rows from an iterable, such as a list of lists.

### Example

```python
import csv

users = [
    ["name", "age"],
    ["Alex", 20],
    ["Sam", 22]
]

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)
```

Result:

```csv
name,age
Alex,20
Sam,22
```

**Difference:**
- `writerow()` writes one row.
- `writerows()` writes multiple rows.

---

## 5. `csv.DictReader()` — Read Rows as Dictionaries

The `csv.DictReader()` function reads each row as a dictionary, using the column names as keys.

### Example

Suppose `users.csv` contains:

```csv
name,age
Alex,20
Sam,22
```

Python code:

```python
import csv

with open("users.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["age"])
```

Output:

```text
Alex 20
Sam 22
```

Each row behaves like a dictionary:

```python
{"name": "Alex", "age": "20"}
```

**Remember:** Use `row["name"]` to access a value by its column name.

---

## 6. `csv.DictWriter()` — Write Dictionaries to CSV

The `csv.DictWriter()` function writes dictionary data into a CSV file.

### Example

```python
import csv

users = [
    {"name": "Alex", "age": 20},
    {"name": "Sam", "age": 22}
]

with open("users.csv", "w", newline="") as file:
    fieldnames = ["name", "age"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(users)
```

Result:

```csv
name,age
Alex,20
Sam,22
```

**Explanation:**
- `fieldnames` defines the column names and their order.
- `writeheader()` writes the column names.
- `writerows(users)` writes all the dictionary records.

---

## 7. `writeheader()` — Write Column Names

The `writeheader()` method writes the column names defined by `fieldnames` when using `csv.DictWriter()`.

### Example

```python
import csv

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age"]
    )

    writer.writeheader()
```

Result:

```csv
name,age
```

**Note:** `writeheader()` belongs to the `DictWriter` object, not the regular `csv.writer()` object.

---

## 8. Handling Commas Inside Values

CSV values can contain commas. When a comma belongs inside a value, the CSV format can enclose that value in quotation marks.

### Example CSV

```csv
name,city
Alex,"Kochi, Kerala"
```

Python code:

```python
import csv

with open("users.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['name', 'city']
['Alex', 'Kochi, Kerala']
```

The CSV reader understands that the comma inside `"Kochi, Kerala"` belongs to the city value rather than separating two columns.

---

## 9. Understanding `newline=""`

When opening a CSV file, Python's documentation recommends using `newline=""`.

### Example

```python
import csv

with open("users.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

**Why use it?**

- It lets the `csv` module handle newline characters.
- It helps prevent extra blank rows when writing CSV files on some platforms.
- It helps correctly handle quoted fields containing newline characters.

**Remember:** `newline=""` does not delete newlines. It controls how Python handles them when opening the file.

---

## 10. Quick Revision

| Function or method | Purpose |
|---|---|
| `csv.reader()` | Read CSV rows as lists |
| `csv.writer()` | Create a CSV writer |
| `writerow()` | Write one row |
| `writerows()` | Write multiple rows |
| `csv.DictReader()` | Read rows as dictionaries |
| `csv.DictWriter()` | Write dictionaries to CSV |
| `writeheader()` | Write column names |
| `newline=""` | Let the CSV module handle newlines |

---

## 11. Practice Question

Suppose you want to read a CSV file and access a person's name using `row["name"]`.

Which one should you use?

**Options:**

- A. `csv.reader()`
- B. `csv.DictReader()`
- C. `csv.writer()`
- D. `open.csv()`

Try answering before checking the result!

---

## 12. Key Takeaway

The `csv` module makes it easier to work with structured data stored in CSV files.

- Use `csv.reader()` to read rows as lists.
- Use `csv.DictReader()` to read rows using column names.
- Use `csv.writer()` to write rows from lists.
- Use `csv.DictWriter()` to write rows from dictionaries.
- Use `newline=""` when opening CSV files for reading or writing.
