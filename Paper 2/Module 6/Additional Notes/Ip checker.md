# 🐍 IP Address Classifier & Log Parser — Improved Version

## 📌 Project Overview

This Python security automation project reads IP addresses from a text file, validates them, classifies valid IP addresses into specific subnets, identifies duplicate and invalid addresses, and generates a structured JSON report.

## 🎯 Objectives

- ✅ Read IP addresses from `ips.txt`
- ✅ Validate IPv4 and IPv6 addresses
- ✅ Classify IP addresses based on subnet membership
- ✅ Identify invalid IP addresses
- ✅ Detect duplicate IP addresses
- ✅ Count unique valid IP addresses
- ✅ Generate a JSON report automatically

---

## 📁 Project Structure

Keep the following files in the same folder:

```text
IP Address Classifier/
├── ips.txt
├── parse_ips.py
└── ip_report.json
```

- `ips.txt` — Contains the input IP addresses.
- `parse_ips.py` — Contains the Python automation script.
- `ip_report.json` — Generated automatically after execution.

---

## 💻 Python Automation Script (`parse_ips.py`)

```python
import ipaddress
import json

input_file = "ips.txt"
output_file = "ip_report.json"

networks = {
    "TEST-NET-1": ipaddress.ip_network("192.0.2.0/24"),
    "TEST-NET-2": ipaddress.ip_network("198.51.100.0/24")
}

report = {
    "total_processed": 0,
    "networks": {
        "TEST-NET-1": [],
        "TEST-NET-2": [],
        "unknown_network": []
    },
    "invalid_ips": [],
    "duplicates": []
}

seen_ips = set()

try:
    with open(input_file, "r") as file:
        for line in file:
            ip = line.strip()

            if not ip:
                continue

            report["total_processed"] += 1

            try:
                address = ipaddress.ip_address(ip)
            except ValueError:
                report["invalid_ips"].append(ip)
                continue

            # Check duplicate IPs
            if ip in seen_ips:
                report["duplicates"].append(ip)
            else:
                seen_ips.add(ip)

            # Classify the IP address
            found = False

            for name, network in networks.items():
                if address.version == network.version and address in network:
                    report["networks"][name].append(ip)
                    found = True
                    break

            if not found:
                report["networks"]["unknown_network"].append(ip)

    report["unique_valid_ips"] = len(seen_ips)

    with open(output_file, "w") as file:
        json.dump(report, file, indent=4)

    print("✅ Report generated successfully!")
    print("Total processed:", report["total_processed"])
    print("Unique valid IPs:", len(seen_ips))
    print("Invalid IPs:", len(report["invalid_ips"]))

except FileNotFoundError:
    print("❌ ips.txt not found!")

except OSError as error:
    print("❌ File error:", error)
```

---

## 📄 Sample Input (`ips.txt`)

Create a file named `ips.txt` and add one IP address per line.

```text
192.0.2.10
192.0.2.20
198.51.100.5
8.8.8.8
192.0.2.999
192.0.2.10
```

### 🔍 Input Explanation

| IP Address | Result |
|---|---|
| `192.0.2.10` | Valid — TEST-NET-1 |
| `192.0.2.20` | Valid — TEST-NET-1 |
| `198.51.100.5` | Valid — TEST-NET-2 |
| `8.8.8.8` | Valid — Unknown network |
| `192.0.2.999` | Invalid IP address |
| `192.0.2.10` | Duplicate IP address |

---

## 📊 Expected JSON Report (`ip_report.json`)

With the sample input above, the generated report will look like this:

```json
{
    "total_processed": 6,
    "networks": {
        "TEST-NET-1": [
            "192.0.2.10",
            "192.0.2.20",
            "192.0.2.10"
        ],
        "TEST-NET-2": [
            "198.51.100.5"
        ],
        "unknown_network": [
            "8.8.8.8"
        ]
    },
    "invalid_ips": [
        "192.0.2.999"
    ],
    "duplicates": [
        "192.0.2.10"
    ],
    "unique_valid_ips": 4
}
```

---

## 🧠 Key Python Concepts Practiced

### 1. IP Address Validation

```python
address = ipaddress.ip_address(ip)
```

Validates whether the input is a correctly formatted IPv4 or IPv6 address. Invalid addresses raise a `ValueError`.

### 2. Subnet Classification

```python
if address.version == network.version and address in network:
```

Checks whether an IP address belongs to a specific network. The version check ensures IPv4 and IPv6 addresses are compared with compatible networks.

### 3. Duplicate Detection

```python
seen_ips = set()

if ip in seen_ips:
    report["duplicates"].append(ip)
else:
    seen_ips.add(ip)
```

A set stores unique IP addresses. If an address is already present, the script records it as a duplicate.

### 4. File Handling

```python
with open(input_file, "r") as file:
```

Opens the input file for reading. The `with` statement ensures that the file is closed automatically when the block finishes.

### 5. Removing Whitespace

```python
ip = line.strip()
```

Removes surrounding whitespace, including newline characters, from each line.

### 6. JSON Report Generation

```python
json.dump(report, file, indent=4)
```

Converts the Python dictionary into JSON format and writes it to a file. The `indent=4` argument makes the report easier to read.

### 7. Exception Handling

```python
except ValueError:
```

Handles invalid IP addresses.

```python
except FileNotFoundError:
```

Handles the situation where `ips.txt` does not exist.

```python
except OSError as error:
```

Handles other file-related errors.

---

## 🚀 How to Run the Project

1. Create a folder named `IP Address Classifier`.
2. Save the Python script as `parse_ips.py`.
3. Create `ips.txt` in the same folder.
4. Add your IP addresses to `ips.txt`, one per line.
5. Open the terminal in VS Code.
6. Run the following command:

```bash
python parse_ips.py
```

7. Open `ip_report.json` to view the generated report.

### ✅ Expected Terminal Output

```text
✅ Report generated successfully!
Total processed: 6
Unique valid IPs: 4
Invalid IPs: 1
```

---

## 📝 Important Notes

- `total_processed` counts non-empty entries, including invalid IP addresses.
- `unique_valid_ips` counts distinct valid IP addresses.
- The `duplicates` list records each repeated occurrence after the first.
- Duplicate addresses remain in their subnet lists.
- Valid IP addresses outside the specified networks are classified as `unknown_network`.
- The TEST-NET ranges used in this project are reserved for documentation and examples.

---

## 🎓 Conclusion

This project demonstrates practical Python security automation through file handling, IP address validation, subnet classification, duplicate detection, exception handling, set operations, and JSON report generation.

These concepts provide a foundation for developing cybersecurity utilities and automating repetitive tasks in security operations.
