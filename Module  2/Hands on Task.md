# 🛡️ Cybersecurity Hands-on Tasks — Complete Documentation

## 📌 Overview

This document combines all the cybersecurity hands-on activities provided and organizes them into a single practical learning workflow.

The objective is to develop practical skills in:

- Safe malware analysis
- CVE and vulnerability research
- OSINT investigations
- Attack-technique documentation
- Vulnerability reporting

> **Safety Note:** All security testing and analysis must be performed only on systems, applications, malware samples, and environments for which you have explicit authorization. Malware analysis shou[...]

---

# 1. 🦠 Analyze Malware Samples Safely

## Objective

Learn how to examine suspicious or malicious files in a controlled environment without putting personal systems, networks, or data at risk.

## Key Activities

### a. Set Up a Safe Analysis Environment

- Use an isolated virtual machine.
- Keep malware samples away from the host operating system.
- Disable unnecessary shared folders, clipboard integration, and device passthrough.
- Use snapshots so the environment can be restored after analysis.
- Use a dedicated analysis network or controlled simulation environment.

### b. Collect File Information

Record:

- File name
- File type
- File size
- File hashes
- File creation/modification information when available
- Digital signature information
- Known indicators of compromise (IoCs)

Useful hashes include:

- MD5
- SHA-1
- SHA-256

### c. Perform Static Analysis

Static analysis examines a sample without executing it.

Possible areas of examination:

- File headers
- Strings
- Imported libraries/functions
- Embedded resources
- Metadata
- Packing or obfuscation indicators
- Suspicious URLs, domains, IP addresses, filenames, or registry references

### d. Perform Dynamic Analysis

Dynamic analysis observes behavior in a controlled environment.

Monitor:

- Process creation
- File-system activity
- Registry changes
- Network connections
- DNS requests
- Memory behavior
- Persistence-related changes
- Security-control interactions

### e. Document Indicators of Compromise

Examples include:

- File hashes
- Domains
- IP addresses
- URLs
- Suspicious filenames
- Registry locations
- Process names
- Mutexes or other behavioral indicators

## Expected Outcome

By completing this activity, you should be able to:

- Safely handle suspicious samples.
- Distinguish static and dynamic analysis.
- Identify useful IoCs.
- Record malware behavior systematically.
- Produce a basic malware-analysis report.

---

# 2. 🔎 Research Recent CVEs

## Objective

Learn how to research publicly disclosed vulnerabilities and understand their technical and business impact.

## Key Activities

### a. Identify a CVE

Record:

- CVE identifier
- Product
- Vendor
- Affected component
- Affected versions
- Publication date
- Last modification date

### b. Understand the Vulnerability

Determine:

- Vulnerability type
- Root cause
- Attack requirements
- Affected security boundary
- Potential impact

Common vulnerability categories include:

- Improper input validation
- Authentication issues
- Authorization problems
- Injection
- Memory corruption
- Path traversal
- Information disclosure
- Improper privilege management

### c. Analyze Severity

Review available severity information such as:

- CVSS score
- CVSS vector
- Severity rating
- Attack vector
- Attack complexity
- Privileges required
- User interaction
- Confidentiality impact
- Integrity impact
- Availability impact

### d. Validate Technical Information

Cross-check information using reliable sources such as:

- NVD
- CVE records
- Vendor advisories
- CISA resources
- Security advisories
- Reputable security research

Do not rely on a single source when important technical claims need verification.

### e. Document Remediation

Record:

- Fixed versions
- Available patches
- Vendor recommendations
- Temporary mitigations
- Configuration changes
- Detection recommendations

## Example CVE Research Record

```text
CVE ID:
Vendor:
Product:
Affected Version:
Vulnerability Type:
CVSS:
Attack Vector:
Privileges Required:
User Interaction:
Impact:
Affected Component:
Remediation:
References:
Confidence:
```

## Expected Outcome

You should be able to:

- Find recent CVEs.
- Understand vulnerability descriptions.
- Interpret CVSS information.
- Verify technical claims.
- Explain security impact.
- Recommend appropriate remediation.

---

# 3. 🌐 Perform OSINT Investigations

## Objective

Develop the ability to collect, correlate, validate, and document publicly available information using legal and ethical OSINT methods.

## OSINT Principles

OSINT means gathering intelligence from publicly available information.

Important principles:

- Use only legal and publicly accessible sources.
- Respect privacy.
- Avoid unauthorized access.
- Do not bypass authentication or access controls.
- Validate important findings.
- Record sources and dates.
- Separate facts from assumptions.

## Investigation Workflow

```text
Define Objective
      ↓
Identify Target
      ↓
Collect Public Information
      ↓
Organize Findings
      ↓
Correlate Information
      ↓
Validate Sources
      ↓
Assess Risk
      ↓
Document Results
```

## Information Categories

### Organization Information

Collect, where publicly available:

- Company name
- Legal entity
- Founding information
- Headquarters
- Public offices
- Leadership information
- Business registrations
- Public contact information

### Digital Footprint

Investigate passively:

- Official domains
- Public subdomains
- Publicly indexed services
- DNS information
- Certificate information
- Technology references
- Public social-media profiles
- Public repositories

### Security-Relevant Information

Look for:

- Publicly disclosed vulnerabilities
- Security advisories
- Exposed information
- Publicly documented technologies
- Historical incidents
- Security-related claims

### Reputation

Compare:

- Customer reviews
- Public discussions
- News reports
- Professional profiles
- Official claims
- Independent sources

Always distinguish between:

**Verified fact → Reported claim → Opinion → Unverified information**

## OSINT Documentation Template

```text
Target:
Investigation Objective:
Date:
Sources:
Key Findings:
Digital Footprint:
Security Findings:
Reputation Findings:
Potential Risks:
Evidence:
Confidence:
Recommendations:
```

## Example: Brototype OSINT Investigation

The investigation of Brototype used publicly available and legal sources.

### Organization

- Brototype is associated with **Packapeer Academy Private Limited**.
- Public corporate information identified CIN **U72200KL2019PTC057898**.
- The company was incorporated on **7 May 2019**.
- Kochi is identified as the headquarters/location associated with the organization.

### Public Digital Footprint

Publicly indexed information identified:

- `brototype.com`
- `learn.brototype.com`
- `study.brototype.com`
- `refer.brototype.com`

Public third-party technology information also referenced infrastructure and services associated with providers such as DigitalOcean and common web/CDN/analytics services.

### Leadership

Public information identifies **Nikhil Kilivayil** as Founder & CEO. Public corporate records also list directors associated with the legal entity.

Leadership and founder claims should be cross-checked against authoritative corporate records when used in formal reporting.

### Cybersecurity Training

Public course information describes cybersecurity topics including:

- Network defense
- Penetration testing
- Cloud security
- DevSecOps
- TCP/IP
- VPNs
- Secure design
- Python and shell scripting
- Security labs
- SOC concepts
- GRC
- Cyber threat intelligence

### Placement Claims

Public Brototype pages contain placement-related claims, including:

- Thousands of students placed
- Average salary figures
- Highest salary figures
- Individual alumni examples

These figures should be treated as **company-published claims** unless independently audited or verified.

### Reputation

Public review platforms and online discussions contain both positive and negative opinions.

Reported concerns include topics such as:

- Program cost
- Refund experiences
- Placement expectations
- Program rules

These are user reports or opinions and should not automatically be treated as verified allegations.

### Privacy

The organization's public privacy information indicates collection of categories such as:

- Name
- Email
- Phone number
- Address
- Education information
- Profile information
- IP/device/browser information
- Usage information
- OTP/device-related information
- Communications

### OSINT Assessment

**Overall assessment: 🟡 Needs Verification**

The organization has a visible public business and digital presence. However, claims relating to placements, outcomes, reputation, infrastructure, and privacy should be independently verified whe[...]

No reliable public evidence of a confirmed major Brototype data breach was established during the reviewed research. This does **not** prove that no incident has ever occurred.

> The investigation was passive/public-source research and did not include unauthorized scanning, exploitation, credential testing, or attempts to access restricted systems.

## Expected Outcome

You should be able to:

- Build an organization profile.
- Map a public digital footprint.
- Correlate information from multiple sources.
- Identify security-relevant public information.
- Evaluate source reliability.
- Produce an evidence-based OSINT report.

---

# 4. 🎯 Document Attack Techniques

## Objective

Learn how attacks are structured and document them using a standardized cybersecurity framework such as **MITRE ATT&CK**, while keeping the work focused on defensive understanding.

## Attack Lifecycle

A high-level attack lifecycle can be represented as:

```text
Reconnaissance
      ↓
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Defense Evasion
      ↓
Credential Access
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Command & Control
      ↓
Exfiltration
      ↓
Impact
```

Not every real-world attack uses every stage.

## MITRE ATT&CK Concepts

### Tactics

Tactics describe the **adversary's objective or why** an activity is performed.

### Techniques

Techniques describe **how** an objective may be achieved.

### Sub-techniques

Sub-techniques provide more specific classifications.

## Common Attack Techniques to Study

### Phishing

Understand:

- Social-engineering concepts
- Malicious attachment risks
- Link-based threats
- Credential-harvesting risks
- Detection opportunities

### Exploitation of Public-Facing Applications

Study:

- Vulnerable web applications
- Unpatched software
- Security monitoring
- Patch management
- Web-application defenses

### Valid Accounts

Understand how compromised credentials can be abused and how organizations can detect unusual account activity.

### Command and Scripting Interpreter

Study how legitimate scripting environments can be abused and how defenders can monitor suspicious script execution.

### Credential Access

Study:

- Credential theft concepts
- Password attacks at a defensive level
- Authentication monitoring
- MFA
- Credential protection

### Privilege Escalation

Understand how attackers may attempt to obtain higher privileges and how least privilege and monitoring reduce risk.

### Persistence

Study common persistence concepts and corresponding defensive controls.

### Defense Evasion

Understand how malicious activity may attempt to avoid detection and how endpoint, network, and logging controls can detect suspicious behavior.

### Discovery

Study techniques used to learn about:

- Systems
- Users
- Network configuration
- Installed software
- Security controls

### Lateral Movement

Understand how attackers may move between systems after obtaining access, and how segmentation, authentication controls, and monitoring can limit movement.

### Command and Control

Study:

- Beaconing concepts
- Suspicious outbound connections
- DNS-based indicators
- Network monitoring

### Exfiltration

Understand unauthorized data-transfer concepts and defensive controls such as:

- DLP
- Network monitoring
- Access control
- Data classification

### Impact

Study potential consequences such as:

- Service disruption
- Data destruction
- Data encryption
- Operational downtime
- Financial loss

## Attack Technique Documentation Template

```text
Technique Name:
MITRE ATT&CK ID:
Tactic:
Description:
Security Objective:
High-Level Attack Scenario:
Potential IoCs:
Detection Methods:
Mitigation:
Evidence/Source:
Date:
Confidence:
Risk:
```

## Expected Outcome

You should be able to:

- Explain major attack techniques.
- Map techniques to MITRE ATT&CK.
- Identify defensive detection opportunities.
- Document IoCs.
- Recommend mitigations.
- Explain attacks without performing unauthorized exploitation.

---

# 5. 🛡️ Create Vulnerability Reports

## Objective

Learn how to convert technical vulnerability findings into professional security reports.

## Vulnerability Report Structure

### 1. Title

Create a short and descriptive title.

Example:

```text
Improper Authorization in Example Application
```

### 2. Identification

Include:

- Vulnerability ID
- CVE, if applicable
- CWE, if applicable
- Product
- Vendor
- Version
- Affected component
- Severity
- CVSS score

### 3. Description

Explain:

- What the vulnerability is
- Where it exists
- What causes it
- Why it matters

### 4. Technical Details

Document the technical root cause at an appropriate level.

Include authorized evidence such as:

- Error messages
- Logs
- Screenshots
- Safe test results
- Relevant configuration
- Affected component information

Do not include sensitive credentials or unnecessary secrets.

### 5. Impact

Explain the effect on:

- Confidentiality
- Integrity
- Availability

Also consider:

- Business impact
- Operational impact
- Privacy impact
- Compliance impact

### 6. Severity

Use an appropriate severity methodology.

Example:

```text
Severity: High
CVSS: 8.8
```

The score should be based on the actual vulnerability characteristics rather than guessed.

### 7. Affected Versions

Clearly identify:

```text
Affected:
- Version X
- Version Y

Fixed:
- Version Z
```

### 8. Remediation

Recommend:

- Applying vendor patches
- Upgrading to supported versions
- Correcting insecure configurations
- Improving access control
- Adding monitoring
- Applying temporary mitigations where appropriate

### 9. References

Use reliable sources such as:

- Vendor advisories
- CVE records
- NVD
- CISA
- MITRE
- Official documentation
- Reputable security research

### 10. Risk Assessment

Summarize:

- Likelihood
- Impact
- Exposure
- Existing controls
- Recommended priority

## Professional Vulnerability Report Template

```markdown
# Vulnerability Report

## Title
[Short vulnerability title]

## Identification

- Vulnerability ID:
- CVE:
- CWE:
- Product:
- Vendor:
- Version:
- Affected Component:
- Severity:
- CVSS:

## Description

[Explain the vulnerability.]

## Technical Details

[Explain the root cause and authorized evidence.]

## Impact

### Confidentiality
[Impact]

### Integrity
[Impact]

### Availability
[Impact]

## Affected Versions

[List affected versions.]

## Remediation

[Provide recommended fixes.]

## Detection

[Explain defensive detection opportunities.]

## Risk Assessment

- Likelihood:
- Impact:
- Risk:
- Priority:

## References

[List reliable sources.]

## Evidence

[List safe and authorized evidence.]

## Date

[Date]

## Confidence

[High / Medium / Low]
```

## Expected Outcome

You should be able to:

- Write structured vulnerability reports.
- Explain technical findings clearly.
- Assign evidence-based severity.
- Describe business impact.
- Recommend remediation.
- Produce professional security documentation.

---

# 🔗 Integrated Cybersecurity Investigation Workflow

The five activities can be combined into one practical security workflow:

```text
┌───────────────────────────────┐
│ 1. Analyze Malware Safely     │
│    Identify behavior & IoCs   │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ 2. Research Recent CVEs       │
│    Understand vulnerabilities │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ 3. Perform OSINT Investigations│
│    Gather public intelligence │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ 4. Document Attack Techniques │
│    Map threats & behaviors    │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ 5. Create Vulnerability       │
│    Reports                    │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ Professional Security Report  │
│ Evidence + Risk + Mitigation  │
└───────────────────────────────┘
```

# 📊 Skills Developed

| Area | Skills Developed |
|---|---|
| Malware Analysis | Static analysis, dynamic analysis, IoC identification |
| Vulnerability Research | CVE research, CVSS analysis, remediation |
| OSINT | Public-source research, correlation, validation |
| Threat Analysis | MITRE ATT&CK, attack lifecycle, detection |
| Reporting | Risk assessment, evidence handling, remediation |
| Documentation | Professional cybersecurity reporting |

# 🎓 Overall Learning Outcome

After completing all five activities, you should be able to:

- Safely analyze suspicious malware samples in an isolated environment.
- Research and validate publicly disclosed vulnerabilities.
- Conduct legal and ethical OSINT investigations.
- Understand and document common attack techniques.
- Map attack behavior to recognized frameworks.
- Identify indicators of compromise.
- Evaluate security risks.
- Recommend defensive mitigations.
- Create structured vulnerability reports.
- Present technical findings in a clear and professional format.

# 🏁 Final Goal

The overall goal is to develop a practical cybersecurity investigation workflow:

**Collect → Analyze → Validate → Correlate → Assess → Document → Mitigate**

This workflow builds the foundation for real-world activities such as:

- Security analysis
- Threat intelligence
- SOC operations
- Vulnerability management
- Incident response
- Security research
- Cybersecurity reporting

> **Ethical Requirement:** Perform all practical security testing only in authorized environments. The purpose of these activities is to understand, detect, document, and reduce cybersecurity ris[...]
