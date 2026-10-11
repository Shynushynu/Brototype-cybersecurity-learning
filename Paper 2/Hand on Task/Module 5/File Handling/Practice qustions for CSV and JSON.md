# 🐍 Python File Handling — Practice Questions

## 📚 Table of Contents

- [Part 1: CSV Practice](#-part-1-csv-practice)
- [Part 2: JSON Practice](#-part-2-json-practice)
- [Part 3: Challenge Exercises](#-part-3-challenge-exercises)
- [Progress Tracker](#-progress-tracker)

---

# 📄 Part 1: CSV Practice

## 🟢 Q1. Create a CSV File

**Difficulty:** Beginner

Create a file named `students.csv` containing the following data.

| Name  | Age |
| ----- | --: |
| Alex  |  19 |
| Saju  |  32 |
| Jerry |  21 |

**Requirements:**

- Use the `csv` module.
- Use `with open()` to create the file.
- Write the header and student records using `writerows()`.
- Use `newline=""`.

## 🟢 Q2. Read a CSV File

**Difficulty:** Beginner

Read `students.csv` and print every row.

**Expected Output:**

```text
['Name', 'Age']
['Alex', '19']
['Saju', '32']
['Jerry', '21']
```

## 🟢 Q3. Count the Records

**Difficulty:** Beginner

Read `students.csv` and count how many student records are present, excluding the header.

**Expected Result:**

```text
3
```

## 🟡 Q4. Search for a Student

**Difficulty:** Beginner–Intermediate

Ask the user to enter a name, read the CSV file, and display the matching student's details.

**Example Input:**

```text
Enter name: Saju
```

**Expected Result:**

```text
Saju, 32
```

## 🟡 Q5. Filter Student Records

**Difficulty:** Intermediate

Read a file named `marks.csv` containing student names and marks. Display only students who scored 80 or above.

**Sample Data:**

| Name  | Marks |
| ----- | ----: |
| Alex  |    75 |
| Jerry |    92 |
| Saju  |    85 |
| Amal  |    60 |

**Expected Students:**

- Jerry — 92
- Saju — 85

---

# 🗂️ Part 2: JSON Practice

## 🟢 Q6. Write a Dictionary to a JSON File

**Difficulty:** Beginner

Create a Python dictionary containing a student's name, age, and course.

Save it to `student.json` using `json.dump()`.

## 🟢 Q7. Read a JSON File

**Difficulty:** Beginner

Read `student.json` using `json.load()` and print the student's name and course.

## 🟢 Q8. Convert a Dictionary into a JSON String

**Difficulty:** Beginner

Given this dictionary:

```python
student = {
    "name": "Shynu",
    "age": 18,
    "course": "CyberSecurity"
}
```

**Tasks:**

1. Convert the dictionary into a JSON string using `json.dumps()`.
2. Print the result.
3. Print its data type using `type()`.

## 🟢 Q9. Convert a JSON String into a Dictionary

**Difficulty:** Beginner–Intermediate

Given this string:

```python
data = '{"name": "Jerry", "course": "MEARN"}'
```

**Tasks:**

1. Use `json.loads()` to convert it into a Python object.
2. Print the name separately.
3. Print the course separately.

## 🟡 Q10. Manage Multiple Students

**Difficulty:** Intermediate

Create a list of dictionaries containing at least three students, each with a name, age, and course.

**Requirements:**

- Save the list to `students.json` using `json.dump()`.
- Read it back using `json.load()`.
- Display only students enrolled in `CyberSecurity`.

---

# 🔥 Part 3: Challenge Exercises

## 🔴 Q11. Convert CSV to JSON

Read student records from `students.csv` and convert them into a list of dictionaries.

Save the result to `students.json`.

## 🔴 Q12. Search JSON Records

Read `students.json`, ask the user for a name, and display that student's full details if found.

## 🔴 Q13. Update a JSON File

Read a JSON file containing student details, update one student's age, and save the updated data back to the same file.

## 🔴 Q14. Build a Student Database

Build a menu-driven program that lets the user:

1. Add a student.
2. View all students.
3. Search for a student.
4. Save records to a file.

Use CSV or JSON for storage.

---

# ✅ Progress Tracker

## CSV Practice

- [ ] Q1 — Create a CSV file
- [ ] Q2 — Read a CSV file
- [ ] Q3 — Count records
- [ ] Q4 — Search for a student
- [ ] Q5 — Filter records

## JSON Practice

- [ ] Q6 — Write using `dump()`
- [ ] Q7 — Read using `load()`
- [ ] Q8 — Convert using `dumps()`
- [ ] Q9 — Convert using `loads()`
- [ ] Q10 — Manage multiple students

## Challenge Exercises

- [ ] Q11 — CSV to JSON conversion
- [ ] Q12 — JSON record search
- [ ] Q13 — Update a JSON file
- [ ] Q14 — Student database project

---

## 💡 Important Revision

| Function       | Purpose                                |
| -------------- | -------------------------------------- |
| `csv.reader()` | Read CSV records                       |
| `csv.writer()` | Write CSV records                      |
| `writerow()`   | Write one row                          |
| `writerows()`  | Write multiple rows                    |
| `json.load()`  | Read JSON data from a file             |
| `json.loads()` | Convert a JSON string into Python data |
| `json.dump()`  | Write Python data to a JSON file       |
| `json.dumps()` | Convert Python data into a JSON string |

**🎯 Goal:** Complete the questions in order, test your code, and move to the challenge exercises once you're comfortable with the basics.
