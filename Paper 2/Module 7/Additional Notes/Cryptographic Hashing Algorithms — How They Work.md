# 🔐 Cryptographic Hashing Algorithms — How They Work

> **Beginner-friendly cybersecurity notes**  
> Learn how hashing algorithms calculate a hash and the techniques they use internally.

---

## 📌 Overview

A **cryptographic hash function** takes input data of almost any size and produces a fixed-length output called a **hash** or **digest**.

For example, SHA-256 always produces a 256-bit digest (32 bytes), usually displayed as 64 hexadecimal characters.

Hashing is designed to be a **one-way operation**. You cannot decrypt a hash to recover the original input.

### 🎯 Why Is Hashing Useful?

- 🔍 **Integrity:** Detect changes in files or data.
- ✍️ **Digital signatures:** Hash data as part of digital-signature processes.
- 🔐 **Security protocols:** Hashing is used in many cryptographic systems.

> **Important:** A plain hash does not prove who created the data. For security-sensitive integrity checks, the reference hash must be trusted.

---

## 📚 Table of Contents

1. [🔄 Basic Hashing Process](#1--basic-hashing-process)
2. [🧠 Techniques Used by Hashing Algorithms](#2--techniques-used-by-hashing-algorithms)
   - [SHA-256](#21-sha-256-sha-2-family)
   - [SHA-512](#22-sha-512-sha-2-family)
   - [SHA-3](#23-sha-3-keccak)
   - [MD5](#24-md5)
   - [BLAKE2 and BLAKE3](#25-blake2-and-blake3)
   - [Hashing Algorithm Comparison](#-hashing-algorithm-comparison)
3. [⚙️ Important Mathematical Operations](#3--important-mathematical-operations)
   - [XOR](#31-xor-exclusive-or)
   - [AND](#32-and)
   - [Bit Rotation](#33-bit-rotation)
   - [Modular Addition](#34-modular-addition)
   - [Choice and Majority Functions](#35-choice-and-majority-functions)
4. [🔍 SHA-256: A Closer Look](#4--sha-256-a-closer-look)
5. [🐍 Calculate SHA-256 Using Python](#5--calculate-sha-256-using-python)
6. [🔒 Hashing vs Encryption](#6--hashing-vs-encryption)
7. [🎤 Interview Questions](#7--interview-questions)
8. [⚡ Quick Revision](#8--quick-revision)

---

## 1. 🔄 Basic Hashing Process

A simplified view of a hash calculation is:

```text
Input Data
    |
    v
Message Preparation and Padding
    |
    v
Divide Data into Blocks (algorithm-dependent)
    |
    v
Perform Mathematical and Logical Operations
    |
    v
Generate the Final Hash
```

The exact process depends on the algorithm. Different algorithms use different block sizes, internal states, and mathematical techniques.

### 📝 Example

**Input:**

```text
Hello
```

**SHA-256 output:**

```text
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

Even a small input change, such as changing `Hello` to `hello`, produces a very different SHA-256 digest.

---

## 2. 🧠 Techniques Used by Hashing Algorithms

### 2.1 SHA-256 (SHA-2 Family)

**Digest size:** 256 bits (32 bytes)

SHA-256 uses a compression function in a construction known as **Merkle–Damgård**.

#### Calculation Process

1. Convert the message into a binary representation.
2. Add padding and the message length according to the SHA-256 specification.
3. Divide the prepared message into **512-bit blocks**.
4. Expand each block into a schedule of **64 words**, each 32 bits wide.
5. Perform **64 rounds** of mathematical and logical operations per block.
6. Update the internal state after processing each block.
7. Produce the final 256-bit digest.

#### Operations Used

- Bit rotations and shifts
- XOR and AND
- Choice and majority functions
- Modular addition

**Common use:** File-integrity checking and cryptographic systems.

### 2.2 SHA-512 (SHA-2 Family)

**Digest size:** 512 bits (64 bytes)

SHA-512 follows a similar overall design to SHA-256 but uses wider words.

- Processes **1024-bit blocks**.
- Uses **64-bit words**.
- Performs **80 rounds** per block.
- Uses modular addition modulo \(2^{64}\).

**Main difference:** SHA-512 uses a larger block size, wider words, more rounds per block, and a different digest size.

### 2.3 SHA-3 (Keccak)

SHA-3 uses a different design called a **sponge construction**.

#### Calculation Process

1. Start with an internal state.
2. Absorb the input into the state in portions.
3. Apply the Keccak permutation.
4. Extract the required output from the state.

The Keccak-f[1600] permutation uses a 1600-bit state and 24 rounds.

Its five round steps are:

- **Theta (θ)**
- **Rho (ρ)**
- **Pi (π)**
- **Chi (χ)**
- **Iota (ι)**

**Main difference:** SHA-3 uses a sponge construction instead of SHA-256's Merkle–Damgård construction.

### 2.4 MD5

**Digest size:** 128 bits (16 bytes)

MD5 is an older hashing algorithm.

- Processes 512-bit blocks.
- Maintains a 128-bit internal state.
- Performs 64 operations arranged into four rounds.
- Uses bitwise functions, rotations, and modular addition.

⚠️ **Security warning:** MD5 has practical collision attacks. Do not use it for security-sensitive integrity checks or digital-signature applications.

### 2.5 BLAKE2 and BLAKE3

BLAKE2 and BLAKE3 are modern, efficient hashing algorithms.

They use **ARX operations**:

- **A — Addition**
- **R — Rotation**
- **X — XOR**

BLAKE3 also uses a **tree structure**, allowing chunks of input to be processed efficiently and in parallel.

**Common use:** Fast general-purpose hashing and file-integrity workflows.

### 📊 Hashing Algorithm Comparison

| Algorithm | Digest Size | Main Technique |
|---|---|---|
| MD5 | 128 bits | Compression-based design |
| SHA-1 | 160 bits | Merkle–Damgård construction |
| SHA-256 | 256 bits | Merkle–Damgård construction |
| SHA-512 | 512 bits | Merkle–Damgård construction |
| SHA3-256 | 256 bits | Sponge construction |
| BLAKE2 | Configurable | ARX-based compression |
| BLAKE3 | 256 bits by default | ARX-based compression and tree hashing |

> ⚠️ MD5 and SHA-1 are unsuitable for security-sensitive collision-resistant applications.

---

## 3. ⚙️ Important Mathematical Operations

Hashing algorithms combine several mathematical and logical operations to transform data.

### 3.1 XOR (Exclusive OR)

XOR compares corresponding bits.

```text
  1010
⊕ 1100
------
  0110
```

**Rule:**
- Same bits → `0`
- Different bits → `1`

### 3.2 AND

AND returns `1` only when both corresponding bits are `1`.

```text
  1010
& 1100
------
  1000
```

### 3.3 Bit Rotation

A rotation moves bits around within a fixed-width word. Bits leaving one end re-enter at the other end.

Rotation is different from a normal shift, where bits shifted out are discarded.

### 3.4 Modular Addition

SHA-256 uses 32-bit words and performs addition modulo \(2^{32}\).

If an addition exceeds the maximum 32-bit value, the result wraps around modulo \(2^{32}\).

SHA-512 uses 64-bit words and addition modulo \(2^{64}\).

### 3.5 Choice and Majority Functions

SHA-256 also uses special bitwise functions.

- **Choice:** Each output bit selects a bit from one of two inputs based on a third input.
- **Majority:** Each output bit is the majority value among three input bits.

These operations are combined across multiple rounds to produce the final digest.

---

## 4. 🔍 SHA-256: A Closer Look

SHA-256 processes each 512-bit message block through a compression function.

### Steps

1. **Padding:** Prepare the message according to the SHA-256 specification.
2. **Block processing:** Divide the padded message into 512-bit blocks.
3. **Message schedule:** Create 64 words, each 32 bits wide, from each block.
4. **Initialization:** Set eight 32-bit working variables from the current internal state.
5. **Compression:** Perform 64 rounds using bitwise functions, constants, rotations, and modular addition.
6. **State update:** Combine the working variables with the previous internal state.
7. **Final output:** Produce eight 32-bit words, giving a total of 256 bits.

This is a simplified overview of the algorithm. The complete calculation involves many operations for each block.

---

## 5. 🐍 Calculate SHA-256 Using Python

Python provides the built-in `hashlib` module to calculate hashes.

### Example Code

```python
import hashlib

data = b"Hello"

hash_value = hashlib.sha256(data).hexdigest()

print(hash_value)
```

### Output

```text
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

### Code Explanation

| Code | Meaning |
|---|---|
| `import hashlib` | Imports Python's hashing library |
| `data = b"Hello"` | Stores the input as bytes |
| `hashlib.sha256(data)` | Calculates the SHA-256 digest |
| `.hexdigest()` | Converts the digest into hexadecimal text |
| `print(hash_value)` | Displays the hash |

**Important:** Python's `hashlib` performs the SHA-256 calculations internally. It does not display each compression round.

### 🔐 Example: Check File Integrity

```python
import hashlib

with open("example.txt", "rb") as file:
    data = file.read()

file_hash = hashlib.sha256(data).hexdigest()

print("SHA-256:", file_hash)
```

Run the program again after modifying the file. If the content changes, the hash will normally change too.

For large files, reading the file in chunks is more memory-efficient.

---

## 6. 🔒 Hashing vs Encryption

| Feature | Hashing | Encryption |
|---|---|---|
| Main goal | Often used to check integrity | Protect confidentiality |
| Output | Hash or digest | Ciphertext |
| Reversible? | Not designed to be reversed | Yes, with the correct decryption key |
| Example | SHA-256 | AES-GCM |
| Secret key required? | Not for ordinary SHA-256 | Yes |

### Which Technique Should You Use?

- **File integrity:** SHA-256 with a trusted reference hash.
- **Confidentiality:** Authenticated encryption such as AES-GCM.
- **Password storage:** Argon2id, scrypt, or appropriately configured bcrypt.
- **Message integrity and authenticity:** HMAC-SHA-256 when the communicating parties share a secret key.

> **Remember:** A plain SHA-256 hash does not authenticate the source of a file. An attacker who can replace both the file and its saved hash may evade a simple comparison.

---

## 7. 🎤 Interview Questions

### Q1. What is a hashing algorithm?

A hashing algorithm converts input data into a digest. A cryptographic hash function is designed to make it computationally infeasible to recover the original input or find two different inputs with the same digest, subject to the algorithm's security properties.

### Q2. Is SHA-256 an encryption algorithm?

No. SHA-256 is a cryptographic hashing algorithm. It generates a digest and is not designed to be decrypted.

### Q3. What technique does SHA-256 use?

SHA-256 uses a Merkle–Damgård construction with a compression function. It processes 512-bit blocks using a 64-word message schedule and 64 rounds of operations.

### Q4. What is the difference between SHA-256 and SHA-3?

SHA-256 uses a Merkle–Damgård construction, while SHA-3 uses the Keccak sponge construction.

### Q5. Why should we avoid MD5 for security?

MD5 has practical collision attacks, meaning different inputs can be created with the same hash. It is unsuitable for security-sensitive integrity checks and digital signatures.

### Q6. Does hashing guarantee file integrity?

Hash comparison can detect changes when the reference hash is trusted. If an attacker can replace both the file and the stored hash, a simple comparison alone may not protect the file.

### Q7. What is the difference between a hash and a digest?

The terms are commonly used interchangeably. A digest is the output produced by a hash function.

---

## 8. ⚡ Quick Revision

- 🔐 **Hashing:** Produces a digest and is not encryption.
- 🛡️ **SHA-256:** 256-bit digest, 512-bit blocks, 64 rounds per block.
- 🔢 **SHA-512:** 512-bit digest, 1024-bit blocks, 80 rounds per block.
- 🧽 **SHA-3:** Uses a sponge construction and Keccak permutation.
- ⚠️ **MD5 and SHA-1:** Unsuitable for security-sensitive collision-resistant applications.
- 🚀 **BLAKE2/BLAKE3:** Modern, efficient hash-function families.
- ⚙️ **XOR, AND, rotations, and modular addition:** Examples of operations used inside hashing algorithms.
- 🐍 **Python `hashlib`:** Provides SHA-256 and other hash functions.
- 🔍 **Integrity:** Compare with a trusted hash or use an appropriate authenticated mechanism.
- 🔒 **Confidentiality:** Use encryption, such as AES-GCM.

---

## 💡 Key Takeaway

Different hashing algorithms use different internal designs, but they all aim to produce a digest with useful security properties.

- **SHA-256:** Repeated compression rounds.
- **SHA-3:** Sponge construction.
- **BLAKE3:** ARX-based mixing and tree hashing.

Understanding these techniques helps you understand how cryptographic hashing supports file integrity, cybersecurity tools, and secure systems.
