# 🔹 Task a – Analyze Packet Captures

## 📖 Objective

The objective of this task was to understand how network communication can be analyzed by examining captured network packets.

## 🧰 Tool Used

* **Wireshark** – Used to capture and analyze network packets.

## 🔍 Information Analyzed

During packet analysis, the following information was examined:

* **Source IP Address** – The system sending the packet.
* **Destination IP Address** – The system receiving the packet.
* **Protocol** – The protocol used for communication, such as TCP, UDP, DNS, or HTTP.
* **Source Port** – The port used by the sending application.
* **Destination Port** – The port used by the receiving service.
* **Packet Length** – The size of the packet.
* **Packet Details** – Information contained within different protocol layers.

## 🧪 Practical Procedure

1. Open **Wireshark**.
2. Select the appropriate network interface.
3. Start capturing network traffic.
4. Generate some normal network activity, such as accessing a website or performing a DNS lookup.
5. Stop the packet capture.
6. Examine individual packets.
7. Identify the source and destination addresses.
8. Identify the protocols and ports being used.
9. Review the packet details and communication flow.
10. Document the observations.

## 📊 Sample Observation

| Source | Destination | Protocol |    Port | Observation                  |
| ------ | ----------- | -------- | ------: | ---------------------------- |
| Client | DNS Server  | DNS      |      53 | Domain name resolution       |
| Client | Web Server  | TCP      |     443 | HTTPS connection             |
| Client | Web Server  | TCP      |      80 | HTTP communication           |
| Client | Remote Host | UDP      | Various | Connectionless communication |

> **Note:** The actual IP addresses, ports, and protocols observed will depend on the network traffic captured during the practical exercise.

## 🎯 Result

I learned how to examine packet captures and identify important network information such as IP addresses, protocols, ports, and packet details. This helped me understand how network traffic can be analyzed for troubleshooting and cybersecurity investigations.

---
