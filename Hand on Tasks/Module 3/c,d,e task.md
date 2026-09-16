# 🛡️ Hands-on Network Security Tasks – Practical Report

# 🔹 C. Task 1 – Identify Network Protocols

## 📖 Objective

The objective was to identify different network protocols by examining network communication and understanding their purpose.

### 🔍 Protocols Identified

| Protocol | Purpose                                     | Common Port |
| -------- | ------------------------------------------- | ----------: |
| HTTP     | Transfers web pages and web resources       |          80 |
| HTTPS    | Secure web communication                    |         443 |
| DNS      | Converts domain names into IP addresses     |          53 |
| SSH      | Secure remote administration                |          22 |
| FTP      | Transfers files between systems             |          21 |
| TCP      | Provides reliable data transmission         |           — |
| UDP      | Provides fast connectionless transmission   |           — |
| DHCP     | Automatically assigns network configuration |       67/68 |

### 🧪 Practical Approach

Network traffic can be captured and analyzed using tools such as **Wireshark**.

The following information can be examined:

* Source IP address
* Destination IP address
* Protocol
* Source port
* Destination port
* Packet information
* Communication patterns

### 📌 Observation

By examining network packets, different protocols can be identified based on their packet structure, port numbers, and communication behavior.

### ✅ Result

I learned how to identify commonly used network protocols and understand their role in network communication.

---

# 🔹 D. Task 2 – Build a Network Diagram

## 📖 Objective

The objective was to create a visual representation of a basic network and understand how different devices communicate with each other.

### 🖥️ Basic Network Structure

```text
                    🌐 Internet
                         │
                         ▼
                    ┌─────────┐
                    │ Router  │
                    └────┬────┘
                         │
                         ▼
                    ┌─────────┐
                    │ Switch  │
                    └────┬────┘
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
           💻 PC      🖥️ Server   📱 Mobile
```

### 🔍 Devices Identified

* **Router** – Connects different networks and forwards packets.
* **Switch** – Connects devices within a local network.
* **Server** – Provides services or resources to other systems.
* **PC/Endpoint** – A device used by a network user.
* **Mobile Device** – Connects to the network through wireless communication.

### 📌 Practical Approach

The network diagram was created by:

1. Identifying the devices.
2. Determining how the devices are connected.
3. Representing the connections visually.
4. Identifying the communication path between devices.
5. Adding relevant network information where required.

### ✅ Result

I gained a better understanding of network topology and how different devices communicate within a network.

---

# 🔹 E. Task 3 – Investigate Network Incidents

## 📖 Objective

The objective was to understand how network traffic and logs can be analyzed to identify potentially suspicious activity.

### 🔎 Investigation Process

```text
Network Traffic / Logs
          │
          ▼
    Collect Evidence
          │
          ▼
    Analyze Traffic
          │
          ▼
 Identify Anomalies
          │
          ▼
 Investigate Indicators
          │
          ▼
   Document Findings
          │
          ▼
 Recommend Response
```

### 🔍 Indicators Examined

During an investigation, the following indicators can be reviewed:

* Unusual IP addresses
* Unexpected open ports
* Suspicious domains
* Unusual protocols
* Large or unexpected traffic volumes
* Repeated connection attempts
* Unusual communication patterns
* Unexpected connections between systems

### 🧪 Example Investigation

Suppose a workstation repeatedly communicates with an unfamiliar external IP address.

The investigation can include:

1. Identifying the source system.
2. Identifying the destination IP address.
3. Checking the destination port.
4. Identifying the protocol being used.
5. Reviewing the timing and frequency of connections.
6. Examining related network logs.
7. Determining whether the activity is expected or suspicious.
8. Documenting the findings.

> ⚠️ A suspicious indicator does not automatically mean that an attack has occurred. Additional evidence should be reviewed before reaching a conclusion.

### 📌 Result

I learned how network traffic and logs can be used as evidence during a network security investigation.

---
