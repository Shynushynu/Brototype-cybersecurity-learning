# ╔══════════════════════════════════════╗

# 🔐 PAPER 2 — MODULE 3

# 🛡️ CRYPTOGRAPHY FUNDAMENTALS

# ╚══════════════════════════════════════╝

> 🔎 **Module Focus:** Understanding how cryptography protects information and supports confidentiality, integrity, and authentication.

---

## 📑 Table of Contents

- [🔑 1. Introduction to Cryptography](#1-introduction-to-cryptography)
- [🎯 2. Security Goals](#2-security-goals)
- [🔒 3. Confidentiality](#3-confidentiality)
- [🛡️ 4. Integrity](#4-integrity)
- [🪪 5. Authentication](#5-authentication)
- [🌐 6. Cryptography in Cybersecurity](#6-cryptography-examples-in-cybersecurity)
- [⚖️ 7. Important Differences](#7-important-differences)
- [💡 8. Interview Questions and Answers](#8-interview-questions-and-answers)
- [📝 9. Module Summary](#9-module-summary)

---

## 🔑 1. Introduction to Cryptography

### 📌 What is Cryptography?

**Cryptography** is the technique of protecting information by converting it into a form that unauthorized people cannot easily understand.

It uses mathematical algorithms and keys to protect data during storage and communication.

### 💬 Example

Suppose Alice wants to send a secret message to Bob.

📄 **Original message (Plaintext)**

```text
Hello Bob
```

🔐 **After encryption (Ciphertext)**

```text
Encrypted, unreadable data
```

Bob uses the appropriate decryption key to recover the original message.

### 📚 Important Terms

| 🔹 Term                 | 📖 Meaning                                      |
| ----------------------- | ----------------------------------------------- |
| Plaintext               | Original, readable information                  |
| Ciphertext              | Information transformed by encryption           |
| Encryption              | Converting plaintext into ciphertext            |
| Decryption              | Recovering plaintext from ciphertext            |
| Cryptographic algorithm | Mathematical procedure used to protect data     |
| Cryptographic key       | Information used by a cryptographic algorithm   |
| Cipher                  | An algorithm used for encryption and decryption |

### 🔄 How Cryptography Works

```text
       📄 Original Message
                |
                v
       🔐 Encryption + Key
                |
                v
          🔒 Ciphertext
                |
                v
       🔑 Decryption + Key
                |
                v
       📄 Original Message
```

### 🧩 Types of Cryptography

#### 1. 🔑 Symmetric-Key Cryptography

The same secret key is used for encryption and decryption.

**Example:** AES (Advanced Encryption Standard).

**Uses:**

- Encrypting files
- Protecting stored data
- Securing large amounts of information

#### 2. 🔐 Asymmetric-Key Cryptography

Uses a mathematically related public key and private key.

**Example:** RSA.

**Uses:**

- Digital signatures
- Key establishment and exchange
- Public-key encryption in supported systems

#### 3. #️⃣ Hashing

Hashing converts data into a fixed-length digest using a hash function. It is designed to be one-way.

**Examples:** SHA-256 and SHA-3.

**Uses:**

- Checking file integrity
- Supporting digital signatures
- Storing password verifiers using suitable password-hashing methods

> ⚠️ **Remember:** Hashing is not encryption. Encryption is designed to be reversible with the appropriate key, while secure hashing is designed to be one-way.

---

## 🎯 2. Security Goals

Cryptography helps achieve several security goals. Three fundamental goals form the **CIA Triad**.

\<box border radius="xl" padding={3} gap={3}>
&#x20; \<row align="center" gap={3}>
&#x20;   \<box background="#DCEAFE" radius="lg" size="44px" align="center" justify="center">
&#x20;     \<icon name="lock-keyhole" color="#174EA6" size="xl"/>
&#x20;   \</box>
&#x20;   \<box flex="1" gap={1}>
&#x20;     \*\*🔒 Confidentiality\*\*

```
  <text size="sm">Protects information from unauthorized disclosure.</text>
</box>
```

&#x20; \</row>
&#x20; \<divider color="subtle"/>
&#x20; \<row align="center" gap={3}>
&#x20;   \<box background="#DDF5E5" radius="lg" size="44px" align="center" justify="center">
&#x20;     \<icon name="shield-check" color="#176B3A" size="xl"/>
&#x20;   \</box>
&#x20;   \<box flex="1" gap={1}>
&#x20;     \*\*🛡️ Integrity\*\*

```
  <text size="sm">Helps detect unauthorized changes to information.</text>
</box>
```

&#x20; \</row>
&#x20; \<divider color="subtle"/>
&#x20; \<row align="center" gap={3}>
&#x20;   \<box background="#FCE8D5" radius="lg" size="44px" align="center" justify="center">
&#x20;     \<icon name="server" color="#984B0C" size="xl"/>
&#x20;   \</box>
&#x20;   \<box flex="1" gap={1}>
&#x20;     \*\*⚡ Availability\*\*

```
  <text size="sm">Keeps systems and information accessible to authorized users.</text>
</box>
```

&#x20; \</row>
\</box>

### 🪪 Authentication

Authentication is another important security property that verifies the identity of a user, device, or system.

### 📊 Quick Reference

| Security goal      | Main purpose                     |
| ------------------ | -------------------------------- |
| 🔒 Confidentiality | Prevent unauthorized disclosure  |
| 🛡️ Integrity      | Detect unauthorized modification |
| ⚡ Availability     | Keep resources accessible        |
| 🪪 Authentication  | Verify identity                  |

> 💡 **Example:** Encryption can protect a confidential file, integrity checks can detect changes, and backups can help maintain availability.

---

## 🔒 3. Confidentiality

### 📌 What is Confidentiality?

**Confidentiality** means protecting sensitive information from being accessed or disclosed to unauthorized people.

Encryption is one of the main techniques used to achieve confidentiality.

### 💬 Example

Imagine you send your friend a private message over a network.

- Without suitable protection, an attacker who obtains the message might be able to read it.
- With encryption, the message is transformed into ciphertext.
- Without the necessary key or a successful attack, the attacker should not be able to recover the original message.

### 🛠️ Techniques Used to Achieve Confidentiality

1. **Encryption:** Protects data by transforming it into ciphertext.
2. **Access control:** Restricts who can access information.
3. **Authentication:** Helps verify users before granting access.
4. **Secure communication protocols:** HTTPS helps protect data exchanged with websites.

### 🌍 Real-World Examples

- 🔐 Encrypting files on a laptop.
- 🌐 Using HTTPS while accessing a website.
- 💬 Encrypting messages in a messaging application.
- 📁 Restricting access to confidential company documents.

### 🎤 Interview Question

**Q: How does encryption provide confidentiality?**

**Answer:** Encryption transforms readable data into ciphertext using a cryptographic algorithm and key. Without the required key, an unauthorized person should not be able to recover the original information in a practical attack.

---

## 🛡️ 4. Integrity

### 📌 What is Integrity?

**Integrity** means ensuring that data remains accurate and complete and that unauthorized modifications can be detected.

Integrity is important because attackers or errors may change information during storage or transmission.

### 💬 Example: Checking File Integrity

Suppose you download a software file from an official website.

The publisher provides the file's SHA-256 hash. You calculate the hash of your downloaded file and compare the two values.

- ✅ **Matching hashes:** Supports the conclusion that your file matches the published version.
- ⚠️ **Different hashes:** The file may have been modified, corrupted, or replaced.

A matching hash alone does not prove that the publisher is trustworthy. You must also trust the source of the expected hash.

### 🛠️ Techniques Used to Protect Integrity

#### 1. #️⃣ Cryptographic Hashing

Produces a digest from data.

Examples: SHA-256 and SHA-3.

#### 2. 🔑 Message Authentication Code (MAC)

Uses a secret key to produce a value that helps verify message integrity and authenticity.

Example: HMAC-SHA-256.

#### 3. ✍️ Digital Signatures

Use asymmetric cryptography to support verification of a message's origin and integrity.

#### 4. 📂 File Integrity Monitoring

Calculates file hashes periodically and alerts when unexpected changes are detected.

### 💻 Hashing Example in Python

```python
import hashlib

message = b"Hello Bob"

result = hashlib.sha256(message).hexdigest()

print(result)
```

### 🔍 Code Explanation

| Code               | Purpose                                    |
| ------------------ | ------------------------------------------ |
| `import hashlib`   | Imports Python's hashing library           |
| `b"Hello Bob"`     | Represents the message as bytes            |
| `hashlib.sha256()` | Calculates the SHA-256 hash                |
| `.hexdigest()`     | Returns the digest as a hexadecimal string |
| `print(result)`    | Displays the resulting hash                |

💡 If the input changes, the resulting SHA-256 digest will almost certainly change.

### 🎤 Interview Question

**Q: How can we detect whether a file has been modified?**

**Answer:** We can calculate the file's cryptographic hash and compare it with a trusted, previously recorded hash. If the values differ, the file's contents may have changed.

---

## 🪪 5. Authentication

### 📌 What is Authentication?

**Authentication** is the process of verifying the identity of a user, device, or system.

It answers the question:

> 🗣️ **"Who are you?"**

### 💬 Example

When you log in to your email account, the service checks your credentials to determine whether you are an authorized user.

### 🔑 Common Authentication Factors

#### 1. 🧠 Something You Know

- Password
- PIN
- Passphrase

#### 2. 📱 Something You Have

- Security key
- Authenticator device
- One-time password (OTP) delivered through an available channel

#### 3. 👤 Something You Are

- Fingerprint
- Facial biometric verification

### 🔐 Multi-Factor Authentication (MFA)

Using two or more different types of authentication factors is called **multi-factor authentication (MFA)**.

**Example:** Entering a password and using a security key.

This combines something you know with something you have.

### ⚖️ Authentication vs Authorization

| 🪪 Authentication      | 🔓 Authorization                      |
| ---------------------- | ------------------------------------- |
| Verifies identity      | Determines permitted actions          |
| Answers "Who are you?" | Answers "What are you allowed to do?" |
| Example: Logging in    | Example: Checking file permissions    |

### 🔏 Cryptography and Authentication

Cryptographic techniques can help authenticate users and systems.

- **Digital signatures:** Help verify the origin and integrity of signed data.
- **MACs:** Help verify messages created by someone who possesses the shared secret key.
- **Certificates:** Help bind public keys to identities under a trusted certificate system.
- **Challenge-response protocols:** Can verify possession of a secret without directly transmitting that secret.

> ⚠️ **Important:** Encryption alone does not necessarily authenticate the sender. Authenticated encryption, such as AES-GCM when correctly implemented, provides confidentiality and integrity protections.

### 🎤 Interview Question

**Q: What is the difference between authentication and authorization?**

**Answer:** Authentication verifies who a user is, while authorization determines what that user is allowed to access or do.

---

## 🌐 6. Cryptography Examples in Cybersecurity

| 💻 Scenario                         | 🔧 Technique                                        | 🎯 Security purpose                                   |
| ----------------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| Protecting a private file           | Encryption                                          | Confidentiality                                       |
| Checking whether a file changed     | Cryptographic hash comparison                       | Integrity checking                                    |
| Verifying a signed software package | Digital signature                                   | Origin and integrity verification                     |
| Protecting an API request           | MAC or digital signature, depending on the protocol | Integrity and authentication                          |
| Securing a website connection       | TLS                                                 | Confidentiality, integrity, and server authentication |
| Verifying a user's login            | Password authentication and/or MFA                  | Authentication                                        |

### 🏢 Real-World Scenario

Imagine a company sends a confidential report to another company.

1. 🔒 **Encryption:** Helps prevent unauthorized people from reading the report.
2. \#️⃣ **Hashing:** Helps identify changes when compared with a trusted digest.
3. ✍️ **Digital signature:** Helps verify the report's origin and integrity.
4. 🪪 **Authentication:** Verifies the identity of people accessing the report.
5. 🔓 **Authorization:** Determines whether those people are permitted to access it.

Together, these techniques help protect information.

---

## ⚖️ 7. Important Differences

### 🔒 Encryption vs Hashing

| Encryption                                         | Hashing                                                          |
| -------------------------------------------------- | ---------------------------------------------------------------- |
| Designed to be reversible with the appropriate key | Designed to be one-way                                           |
| Uses a key for encryption and decryption           | A standard cryptographic hash function does not use a secret key |
| Primarily supports confidentiality                 | Commonly supports integrity checking                             |
| Example: AES                                       | Example: SHA-256                                                 |

### 🔑 Symmetric vs Asymmetric Cryptography

| Symmetric                                              | Asymmetric                                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Uses the same secret key for encryption and decryption | Uses a public/private key pair                                                 |
| Generally fast for bulk data encryption                | Often used for signatures and key establishment                                |
| Requires secure secret-key distribution                | Public keys can be distributed openly but must be authenticated when necessary |
| Example: AES                                           | Example: RSA                                                                   |

### 🎯 Confidentiality vs Integrity vs Authentication

| Property           | Main question                                    |
| ------------------ | ------------------------------------------------ |
| 🔒 Confidentiality | Can unauthorized people read the data?           |
| 🛡️ Integrity      | Has the data been changed without authorization? |
| 🪪 Authentication  | Is the identity or claimed origin verified?      |

---

## 💡 8. Interview Questions and Answers

\<box border radius="lg" padding={3} gap={3}>
&#x20; \<text weight="medium">🔹 Q1. What is cryptography?\</text>
&#x20; Cryptography uses mathematical techniques and algorithms to protect information and support security properties such as confidentiality, integrity, and authentication.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q2. What is plaintext?\</text>
&#x20; Plaintext is the original information in a readable or usable form before encryption.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q3. What is ciphertext?\</text>
&#x20; Ciphertext is the transformed output produced by encryption.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q4. What is encryption?\</text>
&#x20; Encryption transforms plaintext into ciphertext using an algorithm and a key.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q5. What is decryption?\</text>
&#x20; Decryption recovers plaintext from ciphertext using the appropriate key and algorithm.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q6. What is the CIA triad?\</text>
&#x20; The CIA triad consists of confidentiality, integrity, and availability.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q7. What is confidentiality?\</text>
&#x20; Confidentiality prevents unauthorized disclosure of information.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q8. What is integrity?\</text>
&#x20; Integrity helps ensure that data remains accurate and that unauthorized modifications can be detected.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q9. What is authentication?\</text>
&#x20; Authentication verifies the identity of a user, device, or system.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q10. What is hashing?\</text>
&#x20; Hashing transforms input data into a fixed-length digest. Secure cryptographic hashes are designed to resist recovering the original input and finding collisions.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q11. Is hashing the same as encryption?\</text>
&#x20; No. Encryption is designed to be reversible with the appropriate key, while hashing is designed to be one-way.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q12. What is a digital signature?\</text>
&#x20; A digital signature is a cryptographic mechanism that helps verify the origin and integrity of data.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q13. What is a cryptographic key?\</text>
&#x20; A cryptographic key is information used by a cryptographic algorithm to perform operations such as encryption, decryption, signing, or verification.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q14. What is multi-factor authentication?\</text>
&#x20; MFA requires two or more authentication factors from different categories, such as something you know and something you have.
&#x20; \<divider color="subtle"/>
&#x20; \<text weight="medium">🔹 Q15. Does encryption guarantee complete security?\</text>
&#x20; No. Security also depends on correct implementation, key management, authentication, access controls, and system security.
\</box>

---

## 📝 9. Module Summary

| 📌 Concept            | 📝 Key takeaway                                                 |
| --------------------- | --------------------------------------------------------------- |
| 🔐 Cryptography       | Techniques used to protect information                          |
| 🔒 Encryption         | Converts plaintext into ciphertext                              |
| 🔑 Decryption         | Recovers plaintext from ciphertext                              |
| 🛡️ Confidentiality   | Prevents unauthorized disclosure                                |
| ✅ Integrity           | Helps detect unauthorized modification                          |
| 🪪 Authentication     | Verifies identity or claimed origin                             |
| ⚡ Availability        | Keeps resources accessible                                      |
| #️⃣ Hashing           | Produces a digest for integrity checking and other applications |
| ✍️ Digital signatures | Help verify origin and integrity                                |
| 🎯 CIA triad          | Confidentiality, Integrity, and Availability                    |

### ⭐ Remember This!

- 🔒 **Confidentiality** = Keep data secret.
- 🛡️ **Integrity** = Keep data accurate and detect unauthorized changes.
- 🪪 **Authentication** = Verify identity.
- 🔓 **Authorization** = Control access.
- ⚡ **Availability** = Keep services accessible.

---

**📚 End of Paper 2 — Module 3, Topic 1: Understand Cryptography Fundamentals.**
