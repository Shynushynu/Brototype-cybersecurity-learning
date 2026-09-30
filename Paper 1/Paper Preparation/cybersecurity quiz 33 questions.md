# 🔐 Cybersecurity Interview Quiz — 33 Questions

> **Format:** Question → My Answer → Corrected / Interview Answer  
> **Topics:** Cybersecurity Fundamentals, Linux, Bash, Networking, Security Teams, Logs, and Security Controls

---

## 1. What is Linux, and why is Linux commonly used in cybersecurity?

### 🧑‍💻 My Answer
> Linux is free to use and modify and to use automation.

### ✅ Corrected / Interview Answer
> Linux is an open-source operating system that is free to use and modify. It is commonly used in cybersecurity because it provides powerful command-line tools, automation through scripting, and good control over system resources and permissions.

---

## 2. What is the CIA Triad in cybersecurity?

### 🧑‍💻 My Answer
> It is a rule that everyone follows about data. In CIA Triad, C refers to Confidentiality, I refers to Integrity, and A refers to Availability.
>
> **Confidentiality:** The data must be confidential; only authorized people should access it.  
> **Integrity:** The data should be correct and unchanged.  
> **Availability:** The data can be accessed any time the user wants.

### ✅ Corrected / Interview Answer
> The CIA Triad is a fundamental security model consisting of Confidentiality, Integrity, and Availability. Confidentiality ensures that only authorized people can access data. Integrity ensures that data remains accurate and is not improperly changed. Availability ensures that authorized users can access data and systems when they need them.

---

## 3. What is the difference between a threat, vulnerability, and risk?

### 🧑‍💻 My Answer
> Threat is something that can harm a system using unauthorized access.  
> Vulnerability is a weakness of a security system that can be exploited using a threat.  
> Risk is a possibility of a threat exploiting a vulnerability.

### ✅ Corrected / Interview Answer
> A threat is something that has the potential to cause harm to a system. A vulnerability is a weakness that can be exploited. Risk is the potential for loss or damage when a threat exploits a vulnerability.

**Easy relationship:**  
**Threat → exploits Vulnerability → creates Risk**

---

## 4. What is an exploit in cybersecurity?

### 🧑‍💻 My Answer
> It is a piece of code or a technique that can take advantage of a vulnerability.

### ✅ Corrected / Interview Answer
> An exploit is a piece of code, technique, or method that takes advantage of a vulnerability to perform an unintended or unauthorized action on a system.

---

## 5. What is an attack vector in cybersecurity?

### 🧑‍💻 My Answer
> Attack vector is a path or an endpoint where an attacker compromises a target.

### ✅ Corrected / Interview Answer
> An attack vector is a path, method, or entry point that an attacker uses to gain unauthorized access to or compromise a target system.

**Examples:** Phishing, vulnerable software, weak passwords, and malicious websites.

---

## 6. What is the difference between a vulnerability and an exploit?

### 🧑‍💻 My Answer
> Vulnerability is a weak point of a security system and exploit takes advantage of vulnerability.

### ✅ Corrected / Interview Answer
> A vulnerability is a weakness in a system, while an exploit is the code, technique, or method used to take advantage of that weakness.

---

## 7. What are the main types of attackers in cybersecurity?

### 🧑‍💻 My Answer
> Script kiddies  
> Cyber criminals

### ✅ Corrected / Interview Answer
Common attacker types include:

- Script Kiddies
- Cybercriminals
- Insider Threats
- Hacktivists
- Nation-State Actors
- Black Hat Hackers

---

## 8. What is the difference between a Black Hat, White Hat, and Grey Hat hacker?

### 🧑‍💻 My Answer
> Black Hat hackers exploit a system or server without permission.
>
> White Hat hackers take permission and then find vulnerabilities and inform the authorized people, sometimes for a reward.
>
> Grey Hat hackers find vulnerabilities without taking permission and then inform authorized people, sometimes for a reward.

### ✅ Corrected / Interview Answer
> **Black Hat hackers** access or attack systems without authorization, usually for malicious purposes.
>
> **White Hat hackers** have authorization to test systems and identify vulnerabilities so they can be fixed.
>
> **Grey Hat hackers** may discover vulnerabilities without authorization but may disclose them to the owner rather than using them maliciously. A reward may be requested, but it does not define a Grey Hat hacker.

---

## 9. What is a SOC, and what is its main purpose?

### 🧑‍💻 My Answer
> SOC will monitor the server continuously to find malicious activity and take relevant action to stop it.

### ✅ Corrected / Interview Answer
> A Security Operations Center (SOC) is a team or facility that continuously monitors an organization's IT environment to detect, investigate, and respond to security threats and suspicious activities.

**Important:** A SOC monitors more than just servers. It can monitor systems, networks, endpoints, logs, and security alerts.

---

## 10. What is the difference between a Blue Team and a Red Team?

### 🧑‍💻 My Answer
> Blue Team is the defense team. They detect and stop malicious activity.

### ✅ Corrected / Interview Answer
> **Blue Team** defends systems by monitoring, detecting, investigating, and responding to threats.
>
> **Red Team** simulates attackers by conducting authorized security testing to find weaknesses in an organization's defenses.

---

## 11. What is a Purple Team, and how does it relate to the Red and Blue Teams?

### 🧑‍💻 My Answer
> Purple Team is the collaboration of Red and Blue Teams. They share the vulnerabilities that need to be protected.

### ✅ Corrected / Interview Answer
> A Purple Team is a collaborative approach where the Red Team and Blue Team work together to improve security. The Red Team shares attack techniques and findings, while the Blue Team uses them to improve detection and defense.

---

## 12. What is a Virtual Machine (VM), and why is it useful in cybersecurity labs?

### 🧑‍💻 My Answer
> VM works as a virtual platform for an OS. In cybersecurity they can test malware or use something that can possibly harm our computer.

### ✅ Corrected / Interview Answer
> A Virtual Machine is a software-based computer that runs an operating system in an isolated environment. In cybersecurity, VMs are useful for safely testing malware, security tools, configurations, and attacks without directly affecting the host system.

---

## 13. What is a snapshot in a Virtual Machine, and why is it useful?

### 📝 Note
This question was asked but the quiz moved forward before an answer was given.

---

## 14. A user enters `https://example.com` in a browser. Explain the major steps that happen from entering the URL until the webpage is displayed.

### 🧑‍💻 My Answer
> The user's interface is at the application layer. There the user sends a request and encapsulates it and encrypts it for protection, then schedules sessions between server and makes the data into a packet.
>
> In the transport layer the packet converts to frames and does the transportation, and in the internet layer they route the destination. Then in the network access layer the data transmits through physical cable.

### ✅ Corrected / Interview Answer
> First, DNS resolves the domain name to an IP address. The browser then establishes a TCP connection with the server and, for HTTPS, performs a TLS handshake to create a secure connection. The browser sends an HTTP request. TCP handles reliable transport, IP handles addressing and routing, and the Network Access layer sends frames through Ethernet or Wi-Fi. The server processes the request and sends the response back, which the browser uses to display the webpage.

### 🔑 Important Corrections
- DNS resolves the domain name to an IP address.
- TCP uses **segments**, not frames.
- IP handles addressing and routing using **packets**.
- Ethernet/Wi-Fi handles **frames**.
- HTTPS uses TLS to secure the communication.

---

## 15. Explain `chmod 750 script.sh`. What permissions do the owner, group, and others receive?

### 🧑‍💻 My Answer
> Owner: `rwx`  
> Group: `rx`  
> User: `rx`

### ✅ Corrected / Interview Answer
For `750`:

- **Owner → `rwx`** → read, write, execute
- **Group → `r-x`** → read, execute
- **Others → `---`** → no permissions

```text
750
│││
││└── Others = 0 = ---
│└─── Group  = 5 = r-x
└──── Owner  = 7 = rwx
```

`755` differs because **others receive `r-x`** instead of `---`.

---

## 16. What is the difference between a primary group and a secondary group in Linux?

### 🧑‍💻 My Answer
> Primary group is the default group of a user and secondary groups are the created ones that we add the user in.
>
> If a user is in the Red Team, the user is a member of the Red Team group and also has a default group by their name, then they will be a member of Purple Team too.

### ✅ Corrected / Interview Answer
> A **primary group** is the user's default group. Files created by the user generally get this group as their group ownership.
>
> **Secondary groups** are additional groups the user belongs to and can provide extra access or permissions.
>
> A user does not automatically become a member of another group. They must be explicitly added.

Example:

```bash
sudo usermod -aG redteam shynu
sudo usermod -aG blueteam shynu
```

A Linux user can have **one primary group and multiple secondary groups**.

Check groups with:

```bash
id shynu
groups shynu
```

---

## 17. A sensitive file has this permission: `-rwxrwxrwx`. What does it mean, and why is it a security risk?

### 🧑‍💻 My Answer
> It means owner, group, and others have permission to read, write, and execute this file. If it's a sensitive file, there is a possibility of misusing it.

### ✅ Corrected / Interview Answer
> `-rwxrwxrwx` means:
>
> - Owner: `rwx`
> - Group: `rwx`
> - Others: `rwx`
>
> The security risk is that **any user on the system can modify or execute the file**. If it is a sensitive script or program, an unauthorized user could potentially alter it and cause unintended or malicious behavior.

---

## 18. What is the difference between `sudo`, `su`, and `chmod`?

### 🧑‍💻 My Answer
> `sudo` is used to get administrative privilege.  
> `su` is used to change between users.  
> `chmod` is used to give permissions like read and write.

### ✅ Corrected / Interview Answer
- **`sudo`** → runs a command with another user's privileges, commonly root privileges.
- **`su`** → switches to another user account and starts a shell/session as that user.
- **`chmod`** → changes the permissions of files and directories.

Examples:

```bash
sudo apt update
su username
chmod 755 script.sh
```

---

## 19. What does `ps aux` show, and what do `a`, `u`, and `x` mean?

### 🧑‍💻 My Answer
> It shows the processes done by the terminal.

### ✅ Corrected / Interview Answer
> `ps aux` displays a detailed list of running processes from all users, including processes that do not have a terminal attached.

- `a` → show processes for all users that have a terminal
- `u` → display processes in a user-oriented format
- `x` → include processes without a controlling terminal

It can show information such as **PID, CPU usage, memory usage, user, and command**.

---

## 20. What is the difference between a process and a service in Linux?

### 🧑‍💻 My Answer
> Process is the program running in the background.

### ✅ Corrected / Interview Answer
> A **process** is a running instance of a program. It can run in the foreground or background.
>
> A **service** is a program or process managed by the system to provide a specific function, often running in the background.

Example:

```bash
systemctl status ssh
```

Here, SSH is a service.

---

## 21. What is a PID, and how would you find the PID of a running process?

### 🧑‍💻 My Answer
> Using the `top` command.

### ✅ Corrected / Interview Answer
> PID (Process ID) is a unique number assigned to each running process by the Linux kernel.

You can find PIDs using:

```bash
top
ps aux
pgrep firefox
pidof firefox
```

---

## 22. What is the difference between `/var/log/auth.log` and `/var/log/syslog`?

### 🧑‍💻 My Answer
> In `auth.log` we find authentication information.

### ✅ Corrected / Interview Answer
> **`/var/log/auth.log`** contains authentication and authorization-related events such as login attempts, `sudo` usage, and SSH authentication.
>
> **`/var/log/syslog`** contains more general system activity, including services, system processes, and various system events. It can also contain useful security indicators.

> **Note:** Log locations differ between Linux distributions. Systems using `systemd` may rely heavily on `journalctl`.

---

## 23. What is the difference between `$variable` and `variable` in Bash?

### 🧑‍💻 My Answer
> With `$` use the value in the variable, and without it it just uses the variable only.

### ✅ Corrected / Interview Answer
> `variable` refers to the variable's name, while `$variable` expands to the value stored in that variable.

Example:

```bash
name="Shynu"

echo name
echo $name
```

Output:

```text
name
Shynu
```

---

## 24. Why do we use `-gt` instead of `>` for numeric comparison in Bash?

### 🧑‍💻 My Answer
> In Bash scripting it does not accept `>` symbol; it only uses `-gt`.

### ✅ Corrected / Interview Answer
> `-gt` is used for numeric comparison inside `[ ]`.
>
> `>` does exist in Bash, but it normally means **output redirection**, not numeric comparison.

Examples:

```bash
[ "$x" -gt 10 ]
```

means **x is greater than 10**.

Common numeric operators:

| Operator | Meaning |
|---|---|
| `-gt` | Greater than |
| `-lt` | Less than |
| `-eq` | Equal to |
| `-ge` | Greater than or equal |
| `-le` | Less than or equal |
| `-ne` | Not equal |

Output redirection:

```bash
echo "hello" > file.txt
```

---

## 25. What does `"$user"` mean, and why is the variable inside double quotes?

### 🧑‍💻 My Answer
> It refers to the variable's value.

### ✅ Corrected / Interview Answer
> `"$user"` means the value stored in the `user` variable. Double quotes help prevent problems caused by spaces or special characters in the value.

Example:

```bash
user="Shynu T"
```

`"$user"` becomes:

```text
Shynu T
```

---

## 26. What is the difference between `=` and `==` in Bash?

### 🧑‍💻 My Answer
> I don't know.

### ✅ Corrected / Interview Answer
In Bash:

- `=` → can be used for string comparison inside `[ ]`
- `==` → can also be used for string comparison, especially inside Bash `[[ ]]`

Examples:

```bash
if [ "$user" = "admin" ]; then
```

```bash
if [[ "$user" == "admin" ]]; then
```

Assignment uses `=`:

```bash
name="Shynu"
```

---

## 27. What is the difference between TCP and UDP?

### 🧑‍💻 My Answer
> TCP is a slow and reliable protocol. It sends data and takes the confirmation request. If the confirmation request does not arrive then it sends it again. UDP only sends and does not confirm, but it is fast. TCP is used for email and UDP is used for streaming.

### ✅ Corrected / Interview Answer
> **TCP** is connection-oriented and reliable. It uses acknowledgments, sequencing, and retransmission when needed. It is not necessarily “slow,” but it generally has more overhead than UDP.
>
> **UDP** is connectionless and has less overhead. It does not provide TCP-style delivery confirmation or retransmission.

Examples:

- **TCP:** Email, web browsing, file transfer
- **UDP:** Live streaming, online gaming, DNS queries

---

## 28. What is DNS, and why is it needed?

### 🧑‍💻 My Answer
> DNS converts it to an IP address to locate.

### ✅ Corrected / Interview Answer
> DNS (Domain Name System) translates human-readable domain names such as `google.com` into IP addresses, allowing a device to locate and communicate with the correct server.

```text
google.com → DNS → IP address → Server
```

---

## 29. What is the difference between a router, switch, and firewall?

### 🧑‍💻 My Answer
> Router routes between the same local network.  
> Switch acts as a center/core.  
> Firewall monitors system requests and if there are too many of them from the same device it will block it.

### ✅ Corrected / Interview Answer
- **Router** → connects different networks and forwards packets using IP addresses.
- **Switch** → connects devices within a LAN and forwards Ethernet frames mainly using MAC addresses.
- **Firewall** → filters network traffic according to configured security rules and can allow or block traffic.

A firewall does not necessarily block traffic just because there are many requests from one device. That depends on its configured rules and features.

---

## 30. What is the difference between a Firewall, IDS, and IPS?

### 🧑‍💻 My Answer
> Firewall will monitor the system and accept or reject the requests based on the rules.
>
> IDS will monitor the system and alert when unauthorized access happens.
>
> IPS will detect, alert, and defend against malicious activity.

### ✅ Corrected / Interview Answer
> A **firewall** filters incoming and outgoing network traffic according to configured security rules and can allow or block traffic.
>
> An **IDS (Intrusion Detection System)** monitors network or system activity, detects suspicious behavior, and generates alerts.
>
> An **IPS (Intrusion Prevention System)** detects suspicious or malicious activity and can automatically take action to block or prevent it.

### 🔥 Example Firewall Rule

```text
Source IP:        192.168.1.50
Destination:      Web Server
Protocol:         TCP
Destination Port: 443
Action:           ALLOW
```

Meaning:

> Allow the device `192.168.1.50` to connect to the web server using TCP port `443` (HTTPS).

Firewall rules can use:

**Source IP + Destination IP + Port + Protocol + Direction → Allow/Block**

---

## 31. What is NAT, and why is it commonly used in home networks?

### 🧑‍💻 My Answer
> I don't know.

### ✅ Corrected / Interview Answer
> NAT (Network Address Translation) translates private IP addresses to a public IP address, allowing multiple devices in a private network to share a public IP when accessing the internet.

Example:

```text
PC       → 192.168.1.10
Phone    → 192.168.1.11
Laptop   → 192.168.1.12
              ↓
          Home Router
              ↓
       Public IP → Internet
```

---

## 32. What is the difference between `chmod 755 script.sh` and `chmod +x script.sh`?

### 🧑‍💻 My Answer
> It's only add x.

### ✅ Corrected / Interview Answer
> `chmod +x script.sh` adds execute permission according to the command's default permission-class handling, while `chmod 755 script.sh` sets a specific complete permission set.

### `755`

- Owner → `rwx`
- Group → `r-x`
- Others → `r-x`

### Explicit execute permissions

```bash
chmod u+x script.sh   # Owner gets execute
chmod g+x script.sh   # Group gets execute
chmod o+x script.sh   # Others get execute
chmod a+x script.sh   # Owner + group + others get execute
```

### Interview-safe answer

> **“`chmod +x` adds execute permission, while `chmod a+x` explicitly adds execute permission for the owner, group, and others. `chmod 755` sets the exact permissions to `rwxr-xr-x`.”**

---

## 33. Write a Bash script that takes `n` numbers and finds the largest number.

### 🧑‍💻 My Answer — Attempt 1

```bash
read -p "enter the no.of input" n
for((i=0;i<n;i++))
do 
    read "a[i]"
```

### 🧑‍💻 My Answer — Attempt 2

```bash
large="$a[0]"
for((i=0;i<n;i++))
do
   if[ large -lt "$a[i]"
done 
echo "largest is $large"
```

### 🔧 Corrections

1. Use `read a[i]`, not `read "a[i]"`.
2. Use `large=${a[0]}` to initialize the largest value.
3. `[ ... ]` needs spaces around it.
4. Add `then`.
5. Compare the current array value with `large`.
6. Update `large` when a bigger number is found.
7. Add `fi`.

### ✅ Correct Script

```bash
read -p "Enter the number of inputs: " n

for ((i=0; i<n; i++))
do
    read a[i]
done

large=${a[0]}

for ((i=1; i<n; i++))
do
    if [ "${a[i]}" -gt "$large" ]; then
        large=${a[i]}
    fi
done

echo "Largest is $large"
```

### 🧠 Logic to Remember

1. Read the number of inputs.
2. Store the numbers in an array.
3. Assume the first number is the largest.
4. Compare each remaining number with the current largest.
5. Replace `large` when a bigger number is found.
6. Print the largest number.

---

# 📌 Quick Interview Revision

## Cybersecurity Fundamentals
- CIA Triad
- Threat
- Vulnerability
- Risk
- Exploit
- Attack Vector
- Attacker Types

## Security Teams
- SOC
- Red Team
- Blue Team
- Purple Team
- White Hat
- Black Hat
- Grey Hat

## Linux
- Permissions
- `chmod`
- Primary/Secondary Groups
- `sudo`
- `su`
- Processes
- Services
- PID
- `ps`
- Logs

## Bash
- Variables
- `$variable`
- `if`
- `-gt`, `-lt`, `-eq`
- Arrays
- Loops
- Functions/conditions
- Finding largest values

## Networking
- OSI Model
- TCP/IP
- DNS
- TCP vs UDP
- Router
- Switch
- Firewall
- IDS
- IPS
- NAT
- HTTPS/TLS
- IP addressing

---

# 🎯 Key Weak Areas to Revise

Based on the quiz, pay extra attention to:

1. **OSI vs TCP/IP and packet flow**
2. **DNS → TCP → TLS → HTTP/HTTPS flow**
3. **TCP segments vs IP packets vs Ethernet frames**
4. **Primary vs secondary Linux groups**
5. **`ps aux` options**
6. **Linux processes vs services**
7. **Bash comparison operators**
8. **Bash array syntax**
9. **NAT**
10. **Firewall rules**
11. **IDS vs IPS vs Firewall**

---

# 🏁 Quiz Result Summary

You showed a good understanding of the basic cybersecurity concepts and were able to explain many topics in your own words.

The main improvement area is **technical precision and command syntax**, especially in Linux, Bash, and networking.

> **Interview tip:** Don't worry about using complicated words. Give a simple definition first, then add one technical detail or example. This makes your answer clear and professional.
