# 🐍 Bitwise Operators in Python

Bitwise operators work directly with the **binary bits (0s and 1s)** of integers.

## 📚 Topics Covered

- [1. Understanding Binary](#1-understanding-binary)
- [2. Bitwise AND (`&`)](#2-bitwise-and-)
- [3. Bitwise OR (`|`)](#3-bitwise-or-)
- [4. Bitwise XOR (`^`)](#4-bitwise-xor-)
- [5. Bitwise NOT (`~`)](#5-bitwise-not-)
- [6. Left Shift (`<<`)](#6-left-shift-)
- [7. Right Shift (`>>`)](#7-right-shift-)
- [8. Quick Revision](#8-quick-revision)
- [9. Practice Questions](#9-practice-questions)

---

## 1. Understanding Binary

Binary is a number system that uses only two digits: `0` and `1`.

Computers use binary to represent data.

| Decimal | Binary |
|---:|---|
| 1 | `001` |
| 2 | `010` |
| 3 | `011` |
| 4 | `100` |
| 5 | `101` |
| 6 | `110` |
| 7 | `111` |

For our examples:

- `5` = `101`
- `3` = `011`

---

## 2. Bitwise AND (`&`)

### Rule

The result is `1` only when **both bits are `1`**.

### Example

```python
a = 5
b = 3

print(a & b)
```

### Calculation

```text
  101   (5)
& 011   (3)
-----
  001   (1)
```

### Output

```text
1
```

### Explanation

- `1 & 0` = `0`
- `0 & 1` = `0`
- `1 & 1` = `1`

**Remember:** AND requires both bits to be `1`.

---

## 3. Bitwise OR (`|`)

### Rule

The result is `1` when **at least one bit is `1`**.

### Example

```python
a = 5
b = 3

print(a | b)
```

### Calculation

```text
  101   (5)
| 011   (3)
-----
  111   (7)
```

### Output

```text
7
```

### Explanation

- `1 | 0` = `1`
- `0 | 1` = `1`
- `1 | 1` = `1`

**Remember:** OR requires at least one bit to be `1`.

---

## 4. Bitwise XOR (`^`)

### Rule

The result is `1` when **the two bits are different**.

### Example

```python
a = 5
b = 3

print(a ^ b)
```

### Calculation

```text
  101   (5)
^ 011   (3)
-----
  110   (6)
```

### Output

```text
6
```

### Explanation

- `1 ^ 0` = `1`
- `0 ^ 1` = `1`
- `1 ^ 1` = `0`
- `0 ^ 0` = `0`

**Remember:** XOR gives `1` when bits are different.

---

## 5. Bitwise NOT (`~`)

### Rule

Flips the bits: `1` becomes `0`, and `0` becomes `1`.

### Example

```python
a = 5

print(~a)
```

### Output

```text
-6
```

### Explanation

Python's bitwise NOT follows this relationship:

```python
~n == -(n + 1)
```

Therefore:

```text
~5 = -(5 + 1)
~5 = -6
```

**Remember:** In Python, `~5` is `-6`, not `2`.

---

## 6. Left Shift (`<<`)

### Rule

Shifts the bits to the left by a specified number of positions.

### Example

```python
a = 5

print(a << 1)
```

### Calculation

```text
Original:  00000101  (5)
Shift left by 1
Result:    00001010  (10)
```

### Output

```text
10
```

### More Examples

```python
print(5 << 1)  # 10
print(5 << 2)  # 20
print(5 << 3)  # 40
```

For non-negative integers, shifting left by one position is equivalent to multiplying by `2`.

**Remember:** Left shift moves bits to the left.

---

## 7. Right Shift (`>>`)

### Rule

Shifts the bits to the right by a specified number of positions.

### Example

```python
a = 5

print(a >> 1)
```

### Calculation

```text
Original:  00000101  (5)
Shift right by 1
Result:    00000010  (2)
```

### Output

```text
2
```

### More Examples

```python
print(5 >> 1)  # 2
print(5 >> 2)  # 1
print(8 >> 1)  # 4
```

For non-negative integers, shifting right by one position is equivalent to floor-dividing by `2`.

**Remember:** Right shift moves bits to the right.

---

## 8. Quick Revision

| Operator | Name | Rule | Example | Result |
|---|---|---|---|---:|
| `&` | AND | Both bits are `1` | `5 & 3` | `1` |
| `|` | OR | At least one bit is `1` | `5 \| 3` | `7` |
| `^` | XOR | Bits are different | `5 ^ 3` | `6` |
| `~` | NOT | Flips the bits | `~5` | `-6` |
| `<<` | Left shift | Shifts bits left | `5 << 1` | `10` |
| `>>` | Right shift | Shifts bits right | `5 >> 1` | `2` |

### Bitwise Operators in Cybersecurity 🔐

Bitwise operators are useful for:

- Understanding binary data.
- Working with permission flags and bit masks.
- Manipulating individual bits.
- Learning how some cryptographic algorithms operate.
- Understanding low-level data processing.

---

## 9. Practice Questions

Try solving these questions before checking the answers.

### Questions

1. What is the result of `6 & 3`?
2. What is the result of `5 | 2`?
3. What is the result of `5 ^ 5`?
4. What is the result of `~7`?
5. What is the result of `4 << 2`?
6. What is the result of `16 >> 2`?
7. What is the difference between `&` and `and`?
8. What is the difference between `|` and `or`?

### Answers

<details>
<summary>Click to reveal answers</summary>

1. `6 & 3` = `2`
2. `5 | 2` = `7`
3. `5 ^ 5` = `0`
4. `~7` = `-8`
5. `4 << 2` = `16`
6. `16 >> 2` = `4`
7. `&` performs bitwise AND on integers, while `and` evaluates logical conditions.
8. `|` performs bitwise OR on integers, while `or` evaluates logical conditions.

</details>

---

## 🎯 Final Summary

- `&` → AND: both bits must be `1`.
- `|` → OR: at least one bit must be `1`.
- `^` → XOR: bits must be different.
- `~` → NOT: flips the bits.
- `<<` → Left shift: moves bits to the left.
- `>>` → Right shift: moves bits to the right.

**Tip:** Practice converting small decimal numbers into binary to understand bitwise operations more easily.
