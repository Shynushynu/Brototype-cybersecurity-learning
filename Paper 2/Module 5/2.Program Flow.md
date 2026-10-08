# 🔄 2. Understand Program Flow

> **Program flow** means the order in which a Python program executes instructions.  
> It helps us control **what happens, when it happens, and how many times it happens**.

---

## 📌 Table of Contents

- [1. Conditional Statements](#1-conditional-statements)
- [2. Loops](#2-loops)
- [3. Nested Conditions](#3-nested-conditions)
- [4. Control Statements](#4-control-statements)
- [5. Problem-Solving Workflows](#5-problem-solving-workflows)
- [6. Quick Revision](#6-quick-revision)

---

# 1. 🔀 Conditional Statements

Conditional statements allow a program to **make decisions**.

They execute different blocks of code depending on whether a condition is `True` or `False`.

### Basic Structure

```python
if condition:
    # code to execute
```

## `if`

The `if` statement executes its block **only when the condition is true**.

```python
age = 20

if age >= 18:
    print("Adult")
```

### Flow

```text
Condition
   ↓
True? ── Yes ──> Execute if block
   │
   No
   ↓
Skip if block
```

---

## `if-else`

`else` provides an alternative when the `if` condition is false.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Flow

```text
        Condition
        /       \
     True       False
      ↓           ↓
    if block   else block
```

---

## `if-elif-else`

Use `elif` when there are **multiple conditions** to check.

```python
marks = 75

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 50:
    print("B")
else:
    print("Fail")
```

Python checks the conditions **from top to bottom** and executes the first matching block.

### ⚠️ Important

Once Python finds a true condition in an `if-elif-else` chain, it skips the remaining conditions.

---

# 2. 🔁 Loops

Loops are used to **repeat a block of code**.

Python mainly provides:

- `for` loop
- `while` loop

---

## `for` Loop

A `for` loop is commonly used when we want to repeat something for each item in a sequence or a known range.

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

### How it works

```text
range(5)
   ↓
0 → execute
1 → execute
2 → execute
3 → execute
4 → execute
   ↓
Stop
```

---

## `while` Loop

A `while` loop repeats as long as its condition remains `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```text
1
2
3
4
5
```

### ⚠️ Important

Make sure something inside the loop eventually makes the condition `False`.

Otherwise, you may create an **infinite loop**.

Example:

```python
count = 1

while count <= 5:
    print(count)
```

Here, `count` never changes, so the condition remains true.

---

## `range()`

`range()` generates a sequence of numbers, commonly used with `for` loops.

### `range(stop)`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
```

Output:

```text
2
3
4
5
```

> The `stop` value is **not included**.

### `range(start, stop, step)`

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

Here:

- `10` → starting value
- `0` → stopping point (not included)
- `-1` → move backward by 1

---

# 3. 🪆 Nested Conditions

A **nested condition** means placing one condition inside another condition.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")
```

### How it works

First Python checks:

```python
age >= 18
```

If it is true, Python checks:

```python
has_id
```

So the second `if` depends on the first `if`.

### Real-world example

```text
Is the person 18 or older?
        ↓
      Yes
        ↓
Do they have an ID?
   ↓            ↓
 Yes           No
  ↓             ↓
Allow entry   Ask for ID
```

---

# 4. 🎮 Control Statements

Control statements change the normal flow of loops.

The main control statements are:

| Statement | Purpose |
|---|---|
| `break` | Stop the loop completely |
| `continue` | Skip the current iteration |
| `pass` | Do nothing; act as a placeholder |

---

## `break`

`break` immediately **stops the loop**.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output:

```text
1
2
3
4
```

When `i` becomes `5`, the loop stops.

### Simple idea

```text
Loop
 ↓
Condition true?
 ↓
break → STOP LOOP
```

---

## `continue`

`continue` skips the **current iteration** and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

The number `3` is skipped, but the loop continues.

### Simple idea

```text
Loop
 ↓
Condition true?
 ↓
continue → Skip this iteration
 ↓
Next iteration
```

---

## `pass`

`pass` does nothing.

It is useful when Python requires a statement but you do not want to write the actual code yet.

```python
if age >= 18:
    pass
```

Another example:

```python
def my_function():
    pass
```

The function exists, but currently does nothing.

### Remember

```text
break    → Stop
continue → Skip
pass     → Do nothing
```

---

# 5. 🧠 Problem-Solving Workflows

Problem-solving workflow means following a **step-by-step process** to solve a programming problem.

## Step 1 — Understand the Problem

Read the problem carefully.

Ask:

- What do I need to find?
- What information is given?
- What should the program produce?

---

## Step 2 — Identify Input and Output

Determine what the program receives and what it should display.

Example:

> Take two numbers and print the larger number.

### Input

```text
Two numbers
```

### Output

```text
The larger number
```

---

## Step 3 — Break the Problem into Steps

For the example above:

```text
1. Get the first number
2. Get the second number
3. Compare them
4. Print the larger number
```

---

## Step 4 — Create the Logic

```python
if num1 > num2:
    print(num1)
else:
    print(num2)
```

---

## Step 5 — Write the Python Code

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Larger:", num1)
else:
    print("Larger:", num2)
```

---

## Step 6 — Test the Program

Try different inputs.

### Test 1

```text
Input:
10
5

Output:
Larger: 10
```

### Test 2

```text
Input:
3
8

Output:
Larger: 8
```

Testing helps find mistakes and unexpected cases.

---

## 🔄 Complete Problem-Solving Flow

```text
Understand the problem
        ↓
Identify inputs & outputs
        ↓
Break into smaller steps
        ↓
Create the logic
        ↓
Write the code
        ↓
Test the code
        ↓
Find and fix errors
        ↓
Final solution
```

---

# 6. ⚡ Quick Revision

| Topic | Main Purpose |
|---|---|
| `if` | Execute code when a condition is true |
| `elif` | Check another condition |
| `else` | Execute when previous conditions are false |
| `for` | Repeat code over a sequence/range |
| `while` | Repeat while a condition is true |
| `range()` | Generate a sequence of numbers |
| Nested condition | Put one condition inside another |
| `break` | Stop a loop |
| `continue` | Skip the current iteration |
| `pass` | Do nothing / placeholder |
| Problem-solving workflow | Solve problems step by step |

---

## 🧩 Key Points to Remember

- 🔀 **Conditions** make decisions.
- 🔁 **Loops** repeat code.
- 🪆 **Nested conditions** put conditions inside other conditions.
- 🛑 **`break`** stops a loop.
- ⏭️ **`continue`** skips one iteration.
- ⏸️ **`pass`** does nothing.
- 🧠 A good workflow helps turn a problem into a working program.
- 📌 In `range()`, the **stop value is excluded**.
- ⚠️ A `while` loop must eventually become `False` to avoid an infinite loop.
