# 🛡️ Understand Denial of Service (DoS) Attacks

## a. DoS Attacks

**DoS (Denial of Service)** is an attack that tries to make a website, server, or network **unavailable to normal users**.

The attacker sends a large number of requests or otherwise consumes the target's resources, such as:

* 🖥️ CPU
* 🧠 Memory
* 🌐 Network bandwidth
* 🔗 Server connections

### Example

A server can normally handle **1,000 requests** at once. If it receives far more requests than it can handle, legitimate users may not be able to access the website.

---

## b. DDoS Attacks

**DDoS (Distributed Denial of Service)** is similar to DoS, but the traffic comes from **many different devices** at the same time.

### DoS vs DDoS

| DoS                                | DDoS                         |
| ---------------------------------- | ---------------------------- |
| Usually comes from one main source | Comes from many sources      |
| Easier to identify and block       | More difficult to filter     |
| Usually smaller in scale           | Can reach a very large scale |
| Single-source attack               | Distributed attack           |

---

## c. Botnets 🤖

A **botnet** is a network of computers or other internet-connected devices that have been compromised and can be controlled by an attacker.

Attackers may use botnets to send large amounts of traffic toward a target.

### Simple Example

```text
        Attacker
           ↓
        Botnet
       ↙   ↓   ↘
     PC    PC   IoT Devices
       \   |   /
          ↓
     Target Server
```

---

## d. Attack Impact 💥

DoS/DDoS attacks can cause:

* 🌐 Website downtime
* 🐌 Slow network or application performance
* 💰 Financial losses
* 👥 Loss of customers or users
* 📉 Damage to reputation
* 🖥️ Increased server and network costs
* 🔒 Reduced availability of important services

### CIA Triad Impact

The main security goal affected by DoS/DDoS attacks is:

> **Availability**

Availability means that authorized users should be able to access systems and services when they need them.

---

## e. Mitigation Approaches 🛡️

Organizations can reduce the impact of DoS/DDoS attacks using:

### 1. 🔥 Firewalls

Filter unwanted or suspicious network traffic.

### 2. 🚦 Rate Limiting

Limit how many requests a client can make within a certain period.

### 3. ⚖️ Load Balancing

Distribute traffic across multiple servers to prevent one server from becoming overloaded.

### 4. 🛡️ DDoS Protection Services

Use specialized services to detect and filter malicious traffic.

### 5. 📊 Traffic Monitoring

Monitor network traffic to identify unusual or sudden increases in requests.

### 6. 🌐 Content Delivery Networks (CDNs)

CDNs can distribute traffic across multiple locations and help absorb large traffic spikes.

### 7. 🏢 Redundant Infrastructure

Use multiple servers and network paths so that one failure does not take down the entire service.

### 8. 🚨 Incident Response Plans

Prepare procedures for detecting, responding to, and recovering from DoS/DDoS attacks.

---

## 🔑 Key Points

* **DoS** → Attack from a single main source.
* **DDoS** → Attack from many sources.
* **Botnet** → A group of compromised devices controlled by an attacker.
* **Main Impact** → Loss of **availability**.
* **Mitigation** → Firewalls, rate limiting, load balancing, monitoring, CDNs, and DDoS protection.

> 🛡️ **Goal of DoS/DDoS attacks:** Make a service unavailable or difficult for legitimate users to access.
