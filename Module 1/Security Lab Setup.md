# 🧪🔐 Understand Security Lab Setup

> 🎯 **Goal:** Build a **safe, isolated, and controlled environment** for learning and practicing cybersecurity.

---

## 🖥️ a. Virtualization Concepts

### 💡 What is Virtualization?

**Virtualization** allows one physical computer to run multiple **virtual computers** using software called a **hypervisor**.

### 🔑 Key Components

| Component | Meaning |
|---|---|
| 🖥️ **Host Machine** | Your physical computer |
| 💻 **Guest Machine** | A virtual computer |
| ⚙️ **Hypervisor** | Software that manages VMs |
| 💾 **Virtual Storage** | Storage allocated to a VM |

### 🛠️ Examples

- 🟦 VirtualBox
- 🟪 VMware
- 🪟 Hyper-V

> 💡 **Example:** You can run Windows on your laptop while running a Linux VM for cybersecurity practice.

---

## 💻 b. Virtual Machines (VMs)

### 📌 What is a VM?

A **Virtual Machine (VM)** is a software-based computer that behaves similarly to a physical computer.

A VM can have its own:

- 🧠 CPU
- 🧮 RAM
- 💾 Storage
- 🌐 Network configuration
- 🐧 Operating System
- 🛠️ Security tools

### 🏗️ Example Lab Structure

```text
             🖥️ PHYSICAL COMPUTER
                     │
                     ▼
              ⚙️ HYPERVISOR
                     │
              ┌──────┴──────┐
              ▼             ▼
          🐧 LINUX VM   🪟 WINDOWS VM
          🔐 Security     🧪 Testing
             Tools         System
