# 🏢 IT Company Network Architecture — 50 Employees

## 📌 Overview

If we start an **IT company with 50 employees**, we can use network architecture to organize employees, departments, devices, servers, and security controls.

Instead of putting everyone into one network, we can divide employees into different **departments and VLANs**.

---

## 👥 Employee Distribution

| Department         | Employees | Example Roles           |
| ------------------ | --------: | ----------------------- |
| 👨‍💻 Development  |        20 | Developers              |
| 🧪 QA/Testing      |         8 | Testers                 |
| 🛡️ Cybersecurity  |         5 | Security Team           |
| 💰 HR & Finance    |         5 | HR, Accounts            |
| 📞 Sales & Support |         7 | Sales, Customer Support |
| 👔 Management      |         5 | Managers                |
| **Total**          |    **50** |                         |

---

## 🌐 Network Architecture

We can separate different departments using **VLANs**.

```text
                         🌐 Internet
                              |
                         [ Firewall ]
                              |
                         [ Core Switch ]
                              |
          ┌───────────────┬──────────────┬───────────────┐
          ↓               ↓              ↓               ↓
      VLAN 10          VLAN 20        VLAN 30         VLAN 40
    Development          QA          Cybersecurity    HR/Finance
      20 PCs             8 PCs          5 PCs           5 PCs

                         ┌──────────────┐
                         ↓
                      VLAN 50
                   Sales & Support
                       7 PCs

                         ┌──────────────┐
                         ↓
                      VLAN 60
                     Management
                       5 PCs
```

---

## 🔐 Why Separate Departments?

If all 50 employees are on the same network and one computer gets compromised, an attacker may have an easier time moving toward other systems.

Using **VLANs and firewall rules**, we can control communication between departments.

### Example

```text
Development → Internet       ✅ Allowed
Development → QA             ✅ Allowed
Development → HR/Finance     ❌ Restricted
Sales → Finance              ❌ Restricted
Cybersecurity → Other VLANs  🔍 Controlled as needed
```

---

## 🧩 What Is VLAN?

**VLAN** stands for **Virtual Local Area Network**.

A VLAN is a **logical network created within a physical network**.

For example:

```text
🏢 IT Company Network

       Core Switch
           |
   ┌───────┼────────┐
   ↓       ↓        ↓
VLAN 10  VLAN 20  VLAN 30
  👨‍💻      🧪       🛡️
  Dev      QA      Security
```

### VLAN IDs

The numbers **10, 20, 30, 40, 50, and 60** are simply **VLAN IDs**.

The numbers themselves don't have a special meaning. The network administrator decides what each VLAN represents.

| VLAN ID | Department    | Employees |
| ------: | ------------- | --------: |
| VLAN 10 | Development   |        20 |
| VLAN 20 | QA/Testing    |         8 |
| VLAN 30 | Cybersecurity |         5 |
| VLAN 40 | HR/Finance    |         5 |
| VLAN 50 | Sales/Support |         7 |
| VLAN 60 | Management    |         5 |

---

## 🛡️ Blue Team and SOC

### 🔵 Blue Team

The **Blue Team** is responsible for defending the organization against cyber threats.

They may:

* 🔍 Perform threat hunting
* 🚨 Respond to incidents
* 🛡️ Improve security defenses
* 🔎 Manage vulnerabilities
* 🔧 Harden systems
* 🔐 Improve security controls

### 🛡️ SOC

**SOC** stands for **Security Operations Center**.

The SOC continuously monitors and analyzes security events.

They may:

* 📊 Monitor security alerts
* 📝 Analyze logs
* 🚨 Detect suspicious activity
* 🔎 Investigate incidents
* 🛡️ Respond to threats
* 📢 Escalate serious incidents

---

## 🔄 Example Security Flow

```text
Employee PC
     ↓
Switch
     ↓
Firewall ─────→ 🌐 Internet
     ↓
Network / Security Logs
     ↓
🛡️ SOC
     ↓
Detects Suspicious Activity
     ↓
🔵 Blue Team
     ↓
Investigates + Responds + Improves Defense
```

---

## 🎯 Interview Answer

> **"If I build an IT company with 50 employees, I would divide the network based on departments using VLANs and control communication between them using firewalls and access rules. The SOC would monitor the network and security events, while the Blue Team would defend the environment and respond to threats."**

---

## 🧠 Key Points to Remember

* 🏢 **Network Architecture** → Organizes the company's network.
* 🧩 **VLAN** → Separates departments logically.
* 🔢 **VLAN ID** → Number used to identify a VLAN.
* 🔥 **Firewall** → Controls network traffic using rules.
* 🛡️ **SOC** → Monitors and investigates security events.
* 🔵 **Blue Team** → Defends the organization against cyber threats.
