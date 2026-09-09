# 🎯 Document Attack Techniques

## 1. Initial Access

Document how the malware initially reaches the victim system.

* Malicious email attachment
* Malicious link
* Drive-by download
* Exploitation of a vulnerable application
* Compromised software/package

**Evidence:**

* Source of the sample
* File name and type
* Delivery mechanism
* Relevant logs or observations

---

## 2. Execution

Document how the malware executes on the system.

* User execution
* Script/interpreter execution
* Command or scripting activity
* Exploitation for execution
* Malicious document execution

**Evidence:**

* Process tree
* Parent/child processes
* Command-line observations
* Suspicious executable or script activity

---

## 3. Persistence

Document how the malware attempts to remain active after reboot or logout.

* Startup mechanisms
* Scheduled tasks
* Services
* Registry-based persistence
* Modified configuration files

**Evidence:**

* Created files
* Registry modifications
* New services or tasks
* Startup entries

---

## 4. Privilege Escalation

Document attempts to obtain higher privileges.

* Exploitation of vulnerabilities
* Abuse of elevated privileges
* Permission-related manipulation
* Credential-based privilege escalation

**Evidence:**

* Process privileges
* Security events
* Suspicious system modifications

---

## 5. Defense Evasion

Document techniques used to avoid detection or analysis.

* Obfuscation
* Packing
* Process manipulation
* File hiding
* Log modification
* Virtualization/sandbox awareness

**Evidence:**

* Obfuscated strings
* Packed executable indicators
* Suspicious API usage
* Anti-analysis behavior

---

## 6. Credential Access

Document attempts to obtain authentication information.

* Credential theft
* Browser credential targeting
* Password database access
* Authentication token targeting

**Evidence:**

* Accessed files
* Suspicious processes
* Relevant API calls
* Security logs

---

## 7. Discovery

Document information the malware collects about the victim environment.

* System information
* Username and hostname
* Operating-system information
* Network configuration
* Running processes
* Installed applications
* Connected devices

**Evidence:**

* Commands executed
* API calls
* Files accessed
* Network/system queries

---

## 8. Command and Control (C2)

Document how the malware communicates with an external server.

* DNS communication
* HTTP/HTTPS communication
* Custom network protocols
* Periodic beaconing
* Remote command retrieval

**Evidence:**

* Destination domains
* IP addresses
* DNS requests
* Network traffic
* Connection frequency

---

## 9. Collection

Document information gathered by the malware.

* Files
* System information
* Application data
* Configuration information
* Other targeted data

**Evidence:**

* Files accessed
* Data staging locations
* Processes involved
* Network transfers

---

## 10. Exfiltration

Document how collected information may be transferred outside the system.

* Network transfer
* Web-based transfer
* C2 channel
* Staged data transfer

**Evidence:**

* Outbound connections
* Transferred data
* Destination infrastructure
* Network logs

---

## 11. Impact

Document the effects of the malware on the system.

* File modification
* Data destruction
* System disruption
* Resource consumption
* Encryption of files

**Evidence:**

* Modified/deleted files
* System changes
* Resource usage
* User-visible effects

---

# 📋 Attack Technique Summary

| Technique            | Observed? | Evidence | Risk |
| -------------------- | --------- | -------- | ---- |
| Initial Access       | ☐         | —        | —    |
| Execution            | ☐         | —        | —    |
| Persistence          | ☐         | —        | —    |
| Privilege Escalation | ☐         | —        | —    |
| Defense Evasion      | ☐         | —        | —    |
| Credential Access    | ☐         | —        | —    |
| Discovery            | ☐         | —        | —    |
| Command & Control    | ☐         | —        | —    |
| Collection           | ☐         | —        | —    |
| Exfiltration         | ☐         | —        | —    |
| Impact               | ☐         | —        | —    |

> **Note:** Mark a technique as observed only when there is supporting evidence from static or dynamic analysis. Avoid assuming a technique merely because a malware family is known to use it.
