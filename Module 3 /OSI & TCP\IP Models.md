# 🌐 2. Understand OSI & TCP/IP Models

> 📚 **OSI and TCP/IP models** help us understand how data is transmitted between devices across a network.
> They divide network communication into different **layers**, with each layer performing a specific function.

---

## 🧩 a. OSI Model

**OSI (Open Systems Interconnection)** is a **7-layer reference model** used to understand how network communication works.

### 🏗️ 7 Layers of the OSI Model

| 🔢 Layer | 📌 Name         | ⚙️ Main Responsibility                         |
| -------: | --------------- | ---------------------------------------------- |
|    **7** | 🖥️ Application | Provides network services to applications      |
|    **6** | 🎨 Presentation | Data formatting, encryption & compression      |
|    **5** | 🔗 Session      | Establishes & manages communication sessions   |
|    **4** | 🚚 Transport    | Reliable delivery, segmentation & flow control |
|    **3** | 🌐 Network      | IP addressing & routing                        |
|    **2** | 🔌 Data Link    | MAC addressing & frame delivery                |
|    **1** | ⚡ Physical      | Transmits raw bits through cables, radio, etc. |


### 🧠 Memory Trick

Remember the OSI layers using:

>Code: **P**lease **D**o **N**ot **T**ell **S**ecret **P**assword **A**nyone
## 🌐 OSI Model – Layer-by-Layer Data Flow

When data is sent over a network, it passes through the **7 layers of the OSI model**.

The data moves **down through the layers** on the sender's device and **up through the layers** on the receiver's device.

---

## 🔄 Data Flow Through OSI Layers

### **7️⃣ Application Layer**

The user requests a webpage or uses a network application.

**Example:** HTTP, HTTPS, DNS, SMTP

⬇️

### **6️⃣ Presentation Layer**

Data may be **translated, encoded, compressed, or encrypted**.

**Example:** Data encryption and encoding

⬇️

### **5️⃣ Session Layer**

Manages the **communication session between two applications/devices**.

**Example:** Establishing, maintaining, and ending a communication session.

⬇️

### **4️⃣ Transport Layer**

Provides **end-to-end communication** and may provide reliable delivery.

**Example:** TCP divides data into segments and handles reliable delivery. UDP provides faster, connectionless delivery.

⬇️

### **3️⃣ Network Layer**

Uses **IP addresses** to determine where data should go and routes packets between networks.

**Example:** IP, Routers

⬇️

### **2️⃣ Data Link Layer**

Handles communication on the **local network** using frames and MAC addresses.

**Example:** Ethernet, Wi-Fi, Switches

⬇️

### **1️⃣ Physical Layer**

Transmits data as **raw bits** using electrical, optical, or radio signals.

**Example:** Ethernet cables, fiber-optic cables, radio signals


---

> 💡 **Note:** The OSI model is mainly a conceptual model used to understand networking and troubleshoot network problems. Modern Internet communication is more directly based on the **TCP/IP model**.


---

## 🌐 b. TCP/IP Model

The **TCP/IP model** is the practical networking model used for communication over the **Internet**.

### 🏗️ TCP/IP Layers

| 🔢 Layer | 📌 Name           | ⚙️ Main Responsibility                 |
| -------: | ----------------- | -------------------------------------- |
|    **4** | 🖥️ Application   | Network applications & protocols       |
|    **3** | 🚚 Transport      | End-to-end communication               |
|    **2** | 🌐 Internet       | IP addressing & routing                |
|    **1** | 🔌 Network Access | Local network & physical communication |

---
## 🔄 TCP vs UDP

**TCP** is a reliable, connection-oriented protocol that ensures data is delivered in the correct order, while **UDP** is a faster, connectionless protocol that does not guarantee delivery or order.

### 🧠 Easy to Remember

**TCP → Reliable & Ordered 📦✅**

**UDP → Fast & Connectionless ⚡**

## 🔄 OSI vs TCP/IP

| 🧩 OSI Model | 🌐 TCP/IP Model   |
| ------------ | ----------------- |
| Application  | Application       |
| Presentation | ↗️ Application    |
| Session      | ↗️ Application    |
| Transport    | Transport         |
| Network      | Internet          |
| Data Link    | ↘️ Network Access |
| Physical     | ↘️ Network Access |

> 💡 **OSI has 7 layers**, while the commonly used **TCP/IP model has 4 layers**.

---

## ⚙️ c. Layer Responsibilities

Each layer has a specific responsibility in network communication.

### 🖥️ Application Layer

Provides network services directly to applications.

**Examples:** HTTP, HTTPS, DNS, FTP, SMTP

### 🎨 Presentation Layer

Responsible for:

* 🔐 Encryption & decryption
* 📦 Data formatting
* 🗜️ Data compression

### 🔗 Session Layer

Responsible for:

* Starting communication sessions
* Maintaining sessions
* Ending sessions
>“**communication session**” means the **connection between two devices or applications that are communicating with each other.**

### 🚚 Transport Layer

Responsible for:

* 📦 Data segmentation
* ✅ Reliable delivery
* 🔄 Flow control
* 🔢 Port numbers

**Examples:** TCP, UDP

### 🌐 Network Layer

Responsible for:

* 🏷️ IP addressing
* 🛣️ Routing
* 📦 Packet delivery

**Example:** IP

### 🔌 Data Link Layer

Responsible for:

* 🆔 MAC addresses
* 📦 Frames
* 🔄 Communication between devices on the local network

### ⚡ Physical Layer

Responsible for transmitting **raw bits** through:

* 🔌 Ethernet cables
* 📡 Wireless signals
* 💡 Fiber-optic cables

---

# 📦 d. Packet Flow

When data is sent from one device to another, it travels through the network layers.

### 📤 Sender Side

```text
        🖥️ Application
              ↓
        🚚 Transport
          Segment
              ↓
          🌐 Network
           Packet
              ↓
        🔌 Data Link
           Frame
              ↓
         ⚡ Physical
            Bits
              ↓
        🌐 NETWORK
```

### 📥 Receiver Side

```text
        🌐 NETWORK
              ↓
         ⚡ Physical
            Bits
              ↓
        🔌 Data Link
           Frame
              ↓
          🌐 Network
           Packet
              ↓
        🚚 Transport
          Segment
              ↓
        🖥️ Application
```

### 🔄 Data Transformation

```text
📄 Data
  ↓
📦 Segment
  ↓
📦 Packet
  ↓
🖼️ Frame
  ↓
0️⃣ 1️⃣ Bits
```

This process is called:

* 📤 **Encapsulation** → Adding information as data moves down the layers.
* 📥 **Decapsulation** → Removing that information as data moves up the layers.

---

# 🛠️ e. Troubleshooting Concepts

The OSI model can be used to troubleshoot network problems **layer by layer**.

| 🔢 Layer | ⚠️ Common Problem    | 💡 Example               |
| -------: | -------------------- | ------------------------ |
|    **1** | Physical problem     | 🔌 Damaged cable         |
|    **2** | Data Link problem    | 🔄 Incorrect VLAN        |
|    **3** | Network problem      | 🌐 Wrong IP address      |
|    **4** | Transport problem    | 🚫 Blocked port          |
|    **5** | Session problem      | 🔗 Connection terminated |
|    **6** | Presentation problem | 🔐 TLS/certificate issue |
|    **7** | Application problem  | 🌍 DNS/HTTP error        |

---

## 🔍 Simple Troubleshooting Flow

```text
🔌 Check Cable / Wi-Fi
          ↓
🌐 Check IP Address
          ↓
🚪 Check Default Gateway
          ↓
🔎 Check DNS
          ↓
🔢 Check Ports
          ↓
🖥️ Check Application
```

### 🧪 Useful Troubleshooting Commands

| 💻 Command               | 🎯 Purpose                             |
| ------------------------ | -------------------------------------- |
| `ping`                   | Tests network connectivity             |
| `ipconfig` / `ifconfig`  | Displays IP configuration              |
| `tracert` / `traceroute` | Shows the route to a destination       |
| `nslookup`               | Checks DNS resolution                  |
| `netstat`                | Displays network connections and ports |

---

# 🎯 Key Takeaways

> 🔹 **OSI Model** → A 7-layer conceptual/reference model.
>
> 🔹 **TCP/IP Model** → A practical model used for Internet networking.
>
> 🔹 **Encapsulation** → Data moves **down** the layers.
>
> 🔹 **Decapsulation** → Data moves **up** the layers.
>
> 🔹 **Troubleshooting** → Problems can be isolated by checking the layers one by one.

---

## 🧠 Quick Revision

```text
🌐 OSI → 7 Layers
🌐 TCP/IP → 4 Layers

📤 Sender:
Data → Segment → Packet → Frame → Bits

📥 Receiver:
Bits → Frame → Packet → Segment → Data

🛠️ Troubleshooting:
Physical → Data Link → Network → Transport → Application
```

> 🔐 **Understanding these models is essential for cybersecurity because many network attacks and security controls operate at specific layers.**
