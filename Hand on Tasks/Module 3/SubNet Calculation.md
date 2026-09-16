# 🌐 Subnet Calculation Using a Calculator

Subnet calculation can be done easily using a **normal calculator** if you know a few basic formulas.

---

## 🧮 Example: `192.168.1.0/26`

### 1️⃣ Find the Host Bits

An IPv4 address always contains **32 bits**.

```text
Host Bits = 32 - CIDR

32 - 26 = 6
```

So, there are **6 host bits**.

---

### 2️⃣ Calculate Total IP Addresses

Use the formula:

```text
Total Addresses = 2^(Host Bits)
```

In the calculator:

```text
2⁶ = 64
```

So, the subnet contains **64 total IP addresses**.

---

### 3️⃣ Calculate Usable Host Addresses

Usually, two addresses cannot be assigned to devices:

* **Network Address** → First address
* **Broadcast Address** → Last address

Therefore:

```text
Usable Hosts = Total Addresses - 2

64 - 2 = 62
```

So, there are **62 usable host addresses**.

---

### 4️⃣ Find the Subnet Size

The subnet size is **64**.

Start from `0` and count by 64:

```text
0
64
128
192
```

Therefore, the subnets are:

| Subnet | Network Address | Usable IP Range                 | Broadcast Address |
| ------ | --------------- | ------------------------------- | ----------------- |
| 1      | `192.168.1.0`   | `192.168.1.1 – 192.168.1.62`    | `192.168.1.63`    |
| 2      | `192.168.1.64`  | `192.168.1.65 – 192.168.1.126`  | `192.168.1.127`   |
| 3      | `192.168.1.128` | `192.168.1.129 – 192.168.1.190` | `192.168.1.191`   |
| 4      | `192.168.1.192` | `192.168.1.193 – 192.168.1.254` | `192.168.1.255`   |

---

# 🧠 Important Subnetting Formulas

| What You Want       | Formula             |
| ------------------- | ------------------- |
| **Host Bits**       | `32 - CIDR`         |
| **Total Addresses** | `2^(Host Bits)`     |
| **Usable Hosts**    | `2^(Host Bits) - 2` |

---

## 🔢 Another Example: `/28`

Let's calculate:

```text
192.168.1.0/28
```

### Step 1 — Host Bits

```text
32 - 28 = 4
```

### Step 2 — Total Addresses

```text
2⁴ = 16
```

### Step 3 — Usable Hosts

```text
16 - 2 = 14
```

Therefore:

```text
/28
↓
4 Host Bits
↓
16 Total Addresses
↓
14 Usable Host Addresses
```

---

## 📌 Quick Reference

| CIDR  | Host Bits | Total Addresses | Usable Hosts |
| ----- | --------: | --------------: | -----------: |
| `/24` |         8 |             256 |          254 |
| `/25` |         7 |             128 |              |
