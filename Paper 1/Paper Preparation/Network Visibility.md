# 🌐 Network Visibility

## 🔍 What is Network Visibility?

**Network visibility** means being able to **see and understand what is happening on a network**.

It can include:

* 💻 Devices connected to the network
* 🔗 Network connections
* 📦 Network traffic
* 🌐 Protocols being used
* 🚨 Suspicious or malicious activity
* 📜 Logs and network events

---

## 🛠️ Is Wireshark the Only Way?

**No.** Wireshark is only **one tool** used for network visibility.

Different tools provide different types of visibility.

| Tool / Method                   | What You Can See                                 |
| ------------------------------- | ------------------------------------------------ |
| 🦈 **Wireshark**                | Detailed packets and protocols                   |
| 🛡️ **IDS/IPS**                 | Suspicious or malicious network activity         |
| 🔥 **Firewall Logs**            | Allowed and blocked connections                  |
| 📊 **Network Monitoring Tools** | Traffic, bandwidth, devices, and availability    |
| 📜 **Server Logs**              | Connections and activities on servers            |
| 🌐 **DNS Logs**                 | Domain-name requests made by devices             |
| 📡 **Router/Switch Logs**       | Network connections and device activity          |
| 🏢 **SIEM**                     | Collects and analyzes logs from multiple systems |

---

## 🦈 Wireshark

**Wireshark** provides **packet-level network visibility**.

It allows you to inspect network packets and information such as:

* Source IP
* Destination IP
* Protocol
* Port
* Packet details
* TCP connections
* DNS requests

### 🔄 Simple Flow

```text id="j2h1qe"
💻 Computer
     ↓
🌐 Network Traffic
     ↓
🦈 Wireshark
     ↓
📦 Packets
     ↓
HTTP / DNS / TCP / UDP / etc.
```

---

## 🔥 Firewall

A firewall can provide visibility through its logs.

It can show:

* Allowed connections
* Blocked connections
* Source IP addresses
* Destination IP addresses
* Ports
* Protocols

```text id="5fr9z2"
Network Traffic
      ↓
🔥 Firewall
      ↓
Allow / Block
      ↓
📜 Firewall Logs
```

---

## 🛡️ IDS/IPS

**IDS (Intrusion Detection System)** monitors network traffic and detects suspicious activity.

**IPS (Intrusion Prevention System)** can detect and also block certain malicious traffic.

```text id="c5i0cp"
Network Traffic
      ↓
🛡️ IDS / IPS
      ↓
Analyze Traffic
      ↓
🚨 Suspicious Activity?
```

---

## 📊 SIEM

A **SIEM (Security Information and Event Management)** system collects security logs and events from multiple sources.

For example:

```text id="q1y3cu"
🔥 Firewall Logs
       ↓
🛡️ IDS/IPS Logs
       ↓
🌐 DNS Logs
       ↓
💻 Server Logs
       ↓
       SIEM
       ↓
📊 Analysis & Alerts
```

---

## 🧠 Easy Way to Remember

> 🦈 **Wireshark** → See the packets
>
> 🔥 **Firewall** → See and control connections
>
> 🛡️ **IDS/IPS** → Detect suspicious traffic
>
> 📊 **SIEM** → Collect and analyze security events

---

## 🗣️ Interview Answer

> **"Network visibility means being able to monitor and understand what is happening on a network. Wireshark is one tool that provides packet-level visibility, but firewalls, IDS/IPS, network monitoring tools, DNS logs, and SIEM systems can also provide network visibility."**
