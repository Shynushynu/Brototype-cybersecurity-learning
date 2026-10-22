# 📧 Python `smtplib` Module

## 🔗 Anchor
<a id="python-smtplib-module"></a>


## 📌 1. Overview

The `smtplib` module is a built-in Python library used to send emails through an SMTP (Simple Mail Transfer Protocol) server.

It allows Python programs to send automated emails, notifications, reports, and security alerts.

### 🎯 Uses of `smtplib`

- Sending automated emails
- Sending Gmail alerts
- Sending file integrity monitoring alerts
- Sending system monitoring notifications
- Sending log analysis reports
- Sending security event notifications

---

## 📚 2. Important Classes and Methods

| Class / Method | Definition |
|---|---|
| `smtplib.SMTP()` | Creates a connection to an SMTP server. |
| `smtplib.SMTP_SSL()` | Creates an SMTP connection using SSL/TLS encryption from the beginning. |
| `server.ehlo()` | Identifies the client to the SMTP server and obtains its supported features. |
| `server.starttls()` | Upgrades an SMTP connection to an encrypted TLS connection. |
| `server.login()` | Authenticates the sender with the SMTP server. |
| `server.sendmail()` | Sends an email using a sender address, recipient address, and message. |
| `server.send_message()` | Sends an email created using an `email.message.EmailMessage` object. |
| `server.quit()` | Ends the SMTP session and closes the connection. |
| `server.close()` | Closes the connection without the normal SMTP quit procedure. |
| `server.noop()` | Sends a NOOP command to check whether the server responds. |
| `server.docmd()` | Sends a low-level SMTP command to the server. |

**Note:** `server` is a variable representing an SMTP connection. The methods above are called on that connection object.

---

## 🔌 3. Connecting to an SMTP Server

### Using `SMTP()`

```python
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
```

**Explanation:**

- `smtp.gmail.com` is Gmail's SMTP server address.
- `587` is the standard port for SMTP submission with STARTTLS.
- `SMTP()` creates the connection.
- `starttls()` upgrades the connection to encrypted communication.

### Using `SMTP_SSL()`

```python
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
```

**Explanation:**

- `SMTP_SSL()` establishes an encrypted connection from the beginning.
- Port `465` is commonly used for SMTP over implicit TLS.

Use either the STARTTLS approach or the SMTP_SSL approach, not both on the same connection.

---

## 🔐 4. Authentication — `login()`

The `login()` method authenticates your email account with the SMTP server.

### Syntax

```python
server.login(user, password)
```

| Parameter | Definition |
|---|---|
| `user` | The email address used to authenticate. |
| `password` | The password or supported application-specific credential. |

### Example

```python
server.login("your_email@gmail.com", "your_app_password")
```

For Gmail, an App Password may be used when supported by your account configuration.

**Security note:** Never publish real passwords or App Passwords in GitHub repositories.

---

## 📤 5. Sending an Email — `sendmail()`

The `sendmail()` method sends a message through an SMTP connection.

### Syntax

```python
server.sendmail(from_addr, to_addrs, message)
```

| Parameter | Definition |
|---|---|
| `from_addr` | The sender's email address. |
| `to_addrs` | The recipient's email address or a list of addresses. |
| `message` | The email content as a string or bytes. |

### Example

```python
message = """Subject: Security Alert

A monitored file has changed.
"""

server.sendmail(
    "sender@gmail.com",
    "receiver@gmail.com",
    message
)
```

**Explanation:**

- `Subject:` specifies the email subject.
- The blank line separates the email headers from the message body.
- The remaining text is the email body.

---

## ✉️ 6. Sending an Email — `send_message()`

The `send_message()` method sends an email using an email message object.

It is useful when creating emails with subjects, sender addresses, recipients, and message bodies.

### Example

```python
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "Security Alert"
msg["From"] = "sender@gmail.com"
msg["To"] = "receiver@gmail.com"

msg.set_content("A monitored file has changed.")

server.send_message(msg)
```

### Difference Between `sendmail()` and `send_message()`

| `sendmail()` | `send_message()` |
|---|---|
| Accepts the message as a string or bytes. | Accepts an email message object. |
| You generally construct the message content yourself. | The message object manages email headers and content. |
| Useful for simple SMTP message sending. | Convenient for structured emails and attachments. |

---

## 🔒 7. Enabling Encryption — `starttls()`

The `starttls()` method upgrades an existing SMTP connection to use TLS encryption.

### Example

```python
import smtplib
import ssl

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
```

### Explanation

- `ssl.create_default_context()` creates a secure TLS configuration.
- The first `ehlo()` identifies the client and obtains the server's capabilities.
- `starttls()` upgrades the connection to TLS.
- The second `ehlo()` obtains the capabilities available after encryption.

TLS protects communication between your Python program and the SMTP server.

---

## 🔌 8. Closing the Connection — `quit()`

The `quit()` method ends the SMTP session.

### Example

```python
server.quit()
```

It sends the SMTP `QUIT` command and closes the session.

**Best practice:** Use a `with` statement for SMTP connections when possible. Python closes the connection automatically when the block exits.

---

## 🛡️ 9. Complete Example — Gmail Security Alert

```python
import smtplib
import ssl
from email.message import EmailMessage

sender_email = "your_email@gmail.com"
app_password = "your_app_password"
receiver_email = "receiver@gmail.com"

msg = EmailMessage()
msg["Subject"] = "File Integrity Alert"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content(
    "Security Alert: A monitored file has changed."
)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465,
    context=context
) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Security alert email sent.")
```

### How It Works

1. Import the required libraries.
2. Configure the sender and recipient email addresses.
3. Create the email subject and body.
4. Establish a secure connection to Gmail.
5. Authenticate the sender.
6. Send the email.
7. Close the SMTP connection automatically.

---

## ⚠️ 10. Common SMTP Exceptions

| Exception | Definition |
|---|---|
| `smtplib.SMTPAuthenticationError` | Authentication failed. |
| `smtplib.SMTPConnectError` | The connection attempt failed. |
| `smtplib.SMTPServerDisconnected` | The SMTP server disconnected unexpectedly. |
| `smtplib.SMTPRecipientsRefused` | All specified recipients were refused. |
| `smtplib.SMTPSenderRefused` | The SMTP server refused the sender address. |
| `smtplib.SMTPDataError` | The server rejected the message data. |
| `TimeoutError` | A network operation exceeded its timeout. |
| `OSError` | A network or operating-system-level error occurred. |

### Example: Handling SMTP Errors

```python
import smtplib

try:
    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        timeout=10
    ) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent successfully.")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed.")

except smtplib.SMTPServerDisconnected:
    print("SMTP server disconnected.")

except smtplib.SMTPException as error:
    print("SMTP error:", error)

except OSError as error:
    print("Network or operating system error:", error)
```

The variables `sender_email`, `app_password`, and `msg` must be defined before running this example.

---

## 🔐 11. Applications in Cybersecurity

### File Integrity Monitoring
Send an email when a monitored file's SHA-256 hash changes.

### System Monitoring
Notify an administrator when an important system resource exceeds a configured threshold.

### Service Monitoring
Send an alert when a required service becomes unavailable.

### Log Analysis
Notify an administrator when the program identifies a configured security event in log files.

### Automated Reporting
Send periodic reports containing monitoring results or security events.

---

## 📝 12. Important Points to Remember

- `smtplib` is part of Python's standard library.
- SMTP stands for Simple Mail Transfer Protocol.
- `SMTP()` can establish a connection that is upgraded using STARTTLS.
- `SMTP_SSL()` establishes an encrypted connection from the beginning.
- `login()` authenticates with the server.
- `sendmail()` and `send_message()` send email messages.
- `quit()` ends the SMTP session.
- Use environment variables or a secrets manager to protect credentials.
- Sending an email does not itself detect security events; your monitoring code must identify the event first.

---

## 🎯 13. Interview Answer

**What is the `smtplib` module in Python?**

The `smtplib` module is a built-in Python library used to send emails through SMTP servers. It supports connecting to mail servers, authenticating users, establishing encrypted connections, and sending email messages. In cybersecurity automation, it can be used to send alerts when file changes, system events, or suspicious activities are detected.
