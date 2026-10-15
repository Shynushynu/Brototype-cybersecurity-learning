# 🐍 Python Socket Library — Complete Notes

## 📌 1. What Is a Socket?

A **socket** is an endpoint used for communication between two programs over a network. It allows programs to establish connections and send or receive data.

For example, when you open a website, your browser communicates with a web server using network connections.

### 🔄 How Does a Socket Work?

```text
+----------------------+
|        Client        |
|  Sends a Request     |
+----------------------+
           |
           v
+----------------------+
|   Socket Connection  |
| IP Address + Port    |
|      + Protocol      |
+----------------------+
           |
           v
+----------------------+
|        Server        |
| Receives and Responds|
+----------------------+
```

### 🔑 Important Terms

- **Client:** The program that initiates communication.
- **Server:** The program that waits for or accepts connections.
- **IP Address:** Identifies a network interface or destination.
- **Port:** Identifies a service or application endpoint.
- **Protocol:** Defines how data is communicated, such as TCP or UDP.

---

## 📚 2. What Is the Python Socket Library?

Python's built-in `socket` module provides functions and methods for network communication.

### Importing the Socket Library

```python
import socket
```

You do not need to install an external package to use the standard `socket` module.

---

## 📋 3. List of Important Socket Functions and Methods

| Function / Method | Purpose |
|---|---|
| [`socket.socket()`](#1-socketsocket) | Creates a socket. |
| [`socket.gethostname()`](#2-socketgethostname) | Gets the local computer's hostname. |
| [`socket.gethostbyname()`](#3-socketgethostbyname) | Resolves a hostname to an IPv4 address. |
| [`socket.gethostbyname_ex()`](#4-socketgethostbyname_ex) | Returns extended hostname and IPv4 address information. |
| [`socket.getaddrinfo()`](#5-socketgetaddrinfo) | Resolves a hostname or address into connection-ready address information. |
| [`socket.getfqdn()`](#6-socketgetfqdn) | Gets a fully qualified domain name where available. |
| [`socket.getservbyname()`](#7-socketgetservbyname) | Finds a port number associated with a service name. |
| [`socket.getservbyport()`](#8-socketgetservbyport) | Finds a service name associated with a port number. |
| [`connect()`](#9-connect) | Connects a client socket to a remote endpoint. |
| [`bind()`](#10-bind) | Associates a socket with a local address and port. |
| [`listen()`](#11-listen) | Makes a TCP socket listen for incoming connections. |
| [`accept()`](#12-accept) | Accepts an incoming connection. |
| [`send()`](#13-send) | Sends data through a connected socket. |
| [`sendall()`](#14-sendall) | Sends all supplied data or raises an error. |
| [`recv()`](#15-recv) | Receives data from a socket. |
| [`sendto()`](#16-sendto) | Sends data to a specified destination, commonly with UDP. |
| [`recvfrom()`](#17-recvfrom) | Receives data and the sender's address, commonly with UDP. |
| [`close()`](#18-close) | Closes the socket. |
| [`shutdown()`](#19-shutdown) | Disables sending, receiving, or both. |
| [`settimeout()`](#20-settimeout) | Sets a timeout for socket operations. |
| [`gettimeout()`](#21-gettimeout) | Gets the current timeout setting. |
| [`getsockname()`](#22-getsockname) | Gets the socket's local address. |
| [`getpeername()`](#23-getpeername) | Gets the address of the connected remote endpoint. |
| [`setsockopt()`](#24-setsockopt) | Sets a socket option. |
| [`getsockopt()`](#25-getsockopt) | Gets a socket option. |
| [`makefile()`](#26-makefile) | Creates a file-like interface for a socket. |
| [`setblocking()`](#27-setblocking) | Enables or disables blocking mode. |
| [`getblocking()`](#28-getblocking) | Checks whether the socket is in blocking mode. |
| [`detach()`](#29-detach) | Detaches and returns the underlying socket descriptor. |
| [`fileno()`](#30-fileno) | Returns the socket's file descriptor or handle. |
---

# 🔍 4. Explanation of Each Function and Method

## 1. `socket.socket()`

**Purpose:** Creates a new socket object.

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

client.close()
```

### Explanation

- `socket.socket()` creates a socket object.
- `socket.AF_INET` specifies IPv4 addressing.
- `socket.SOCK_STREAM` specifies a stream socket, commonly used with TCP.
- `client.close()` closes the socket.

**Use:** Creating a TCP or UDP socket for network communication.

---

## 2. `socket.gethostname()`

**Purpose:** Returns the hostname of the local computer.

```python
import socket

hostname = socket.gethostname()

print(hostname)
```

Example output:

```text
DESKTOP-ABC123
```

The output depends on your computer.

**Use:** Identifying your machine's hostname in a network utility.

---

## 3. `socket.gethostbyname()`

**Purpose:** Resolves a hostname to an IPv4 address.

```python
import socket

ip_address = socket.gethostbyname("example.com")

print(ip_address)
```

The actual IP address may vary.

**Use:** Finding an IPv4 address associated with a domain name.

**Note:** This function returns an IPv4 address. For IPv4 and IPv6 resolution, use `getaddrinfo()`.

---

## 4. `socket.gethostbyname_ex()`

**Purpose:** Returns extended hostname information, including aliases and IPv4 addresses.

```python
import socket

result = socket.gethostbyname_ex("example.com")

print(result)
```

The result is a tuple containing:

1. The official hostname returned by the resolver.
2. A list of aliases.
3. A list of IPv4 addresses.

**Use:** Collecting additional hostname-resolution information.

---

## 5. `socket.getaddrinfo()`

**Purpose:** Resolves a hostname and service into address information suitable for creating a connection.

```python
import socket

results = socket.getaddrinfo(
    "example.com",
    443,
    type=socket.SOCK_STREAM
)

print(results)
```

It can return IPv4 and IPv6 results, depending on the system and DNS response.

**Use:** Building network applications that need to support different address families.

---

## 6. `socket.getfqdn()`

**Purpose:** Attempts to return the fully qualified domain name (FQDN) for a host.

```python
import socket

name = socket.getfqdn()

print(name)
```

An FQDN is a complete domain name, such as `server.example.com`.

**Use:** Getting a machine's fully qualified name when supported by its name-resolution configuration.

---

## 7. `socket.getservbyname()`

**Purpose:** Looks up the port associated with a service name in the system's service database.

```python
import socket

port = socket.getservbyname("https", "tcp")

print(port)
```

Example output on a typical system:

```text
443
```

**Use:** Translating a service name into a port number.

**Note:** The result depends on the system's service database.

---

## 8. `socket.getservbyport()`

**Purpose:** Looks up the service name associated with a port and protocol.

```python
import socket

service = socket.getservbyport(443, "tcp")

print(service)
```

Typical output:

```text
https
```

**Use:** Understanding service names associated with known port numbers.

---

## 9. `connect()`

**Purpose:** Connects a client socket to a remote endpoint.

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)

try:
    client.connect(("example.com", 443))
    print("Connection successful")

except OSError as error:
    print("Connection failed:", error)

finally:
    client.close()
```

### Explanation

- `client.settimeout(5)` sets a five-second timeout.
- `connect(("example.com", 443))` attempts to establish a TCP connection.
- `except OSError` handles connection-related errors.
- `finally` ensures that the socket is closed.

**Use:** Establishing TCP connections to servers you are authorized to access.

---

## 10. `bind()`

**Purpose:** Associates a socket with a local IP address and port.

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))

print("Socket bound to port 5000")

server.close()
```

### Explanation

- `127.0.0.1` is the IPv4 loopback address, which refers to your own computer.
- `5000` is the selected local port.
- `bind()` associates the socket with that local endpoint.

**Use:** Setting up a server to receive connections on a local address and port.

---

## 11. `listen()`

**Purpose:** Marks a TCP socket as ready to accept incoming connections.

```python
server.listen(5)
```

The number `5` is the requested backlog for pending connections. It is not a limit of five total clients.

**Use:** Preparing a bound TCP socket to act as a listening server.

---

## 12. `accept()`

**Purpose:** Accepts an incoming connection on a listening socket.

```python
connection, address = server.accept()
```

It returns:

- `connection`: A new socket for communicating with the connected client.
- `address`: The remote client's address.

**Use:** Handling client connections in a TCP server.

---

## 13. `send()`

**Purpose:** Sends bytes through a connected socket.

```python
client.send(b"Hello")
```

The `b` before the string creates a bytes object.

**Important:** `send()` may send fewer bytes than requested. Applications must handle any unsent bytes.

**Use:** Sending data through a connected socket.

---

## 14. `sendall()`

**Purpose:** Sends all supplied bytes unless an error occurs.

```python
client.sendall(b"Hello from Python")
```

Unlike `send()`, it continues sending until all the data has been sent or an exception occurs.

**Use:** Sending a complete byte sequence over a connected socket.

**Note:** Applications still need a protocol for determining where each message ends.

---

## 15. `recv()`

**Purpose:** Receives bytes from a connected socket.

```python
data = client.recv(1024)

print(data)
```

### Explanation

- `1024` is the maximum number of bytes to receive in this call.
- The returned value is bytes.
- An empty bytes object (`b""`) on a TCP connection usually indicates that the peer has closed its sending side.

**Use:** Receiving data from a server or client.

---

## 16. `sendto()`

**Purpose:** Sends data to a specified destination address, commonly using UDP.

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Hello", ("127.0.0.1", 5000))

client.close()
```

The destination includes an IP address and port.

**Use:** Sending UDP datagrams without first establishing a TCP-style connection.

---

## 17. `recvfrom()`

**Purpose:** Receives a datagram and returns the sender's address.

```python
data, address = server.recvfrom(1024)

print(data)
print(address)
```

**Use:** Receiving UDP datagrams and identifying their source endpoint.

---

## 18. `close()`

**Purpose:** Closes the socket and releases its resources.

```python
client.close()
```

**Use:** Cleaning up network connections when they are no longer required.

---

## 19. `shutdown()`

**Purpose:** Disables sending, receiving, or both directions of communication.

```python
client.shutdown(socket.SHUT_RDWR)
client.close()
```

### Common Options

| Option | Meaning |
|---|---|
| `socket.SHUT_RD` | Disables receiving. |
| `socket.SHUT_WR` | Disables sending. |
| `socket.SHUT_RDWR` | Disables both sending and receiving. |

**Use:** Controlling how a connection is closed. The socket should still be closed when no longer needed.

---

## 20. `settimeout()`

**Purpose:** Sets how long certain socket operations can wait before timing out.

```python
client.settimeout(5)
```

This sets a timeout of five seconds.

**Use:** Preventing a network program from waiting indefinitely for an operation.

---

## 21. `gettimeout()`

**Purpose:** Returns the socket's current timeout setting.

```python
print(client.gettimeout())
```

Possible results include:

- `5.0` — a five-second timeout.
- `None` — no timeout is configured.

**Use:** Checking the current timeout configuration.

---

## 22. `getsockname()`

**Purpose:** Returns the local address associated with the socket.

```python
print(client.getsockname())
```

Depending on the socket state, this may return a local IP address and port.

**Use:** Finding the local endpoint used by a connection.

---

## 23. `getpeername()`

**Purpose:** Returns the address of the remote endpoint connected to the socket.

```python
print(client.getpeername())
```

**Use:** Checking which remote endpoint a connected socket is communicating with.

---

## 24. `setsockopt()`

**Purpose:** Sets a socket option that controls socket behavior.

```python
client.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_KEEPALIVE,
    1
)
```

This enables the operating system's TCP keepalive option for that socket.

**Use:** Configuring supported networking behavior. Exact options depend on the operating system.

---

## 25. `getsockopt()`

**Purpose:** Reads a socket option.

```python
value = client.getsockopt(
    socket.SOL_SOCKET,
    socket.SO_KEEPALIVE
)

print(value)
```

**Use:** Checking the current value of a supported socket option.

---

## 26. `makefile()`

**Purpose:** Creates a file-like object associated with a socket.

```python
file_object = client.makefile("rb")
```

The returned object can use file-like methods such as `read()`.

**Use:** Reading or writing socket data using file-style interfaces.

**Note:** The file object and socket have related lifecycles, so resource management is important.

---

## 27. `setblocking()`

**Purpose:** Enables or disables blocking mode.

```python
client.setblocking(False)
```

- `True`: Operations may wait until they can proceed.
- `False`: Operations return without waiting when they cannot proceed immediately.

**Use:** Building responsive network programs and event-driven applications.

---

## 28. `getblocking()`

**Purpose:** Checks whether the socket is in blocking mode.

```python
print(client.getblocking())
```

It returns `True` or `False`.

**Use:** Checking the socket's current blocking configuration.

---

## 29. `detach()`

**Purpose:** Detaches the underlying socket descriptor or handle from the Python socket object.

```python
descriptor = client.detach()
```

After detaching, the original socket object no longer owns the descriptor.

**Use:** Advanced applications that transfer socket ownership to another component.

**Note:** The descriptor must be managed correctly to avoid resource leaks.

---

## 30. `fileno()`

**Purpose:** Returns the socket's underlying file descriptor or handle.

```python
descriptor = client.fileno()

print(descriptor)
```

**Use:** Integrating sockets with lower-level operating-system APIs and I/O multiplexing.

---

# 📌 5. Common Socket Constants

These are constants rather than functions.

| Constant | Meaning |
|---|---|
| `socket.AF_INET` | IPv4 address family. |
| `socket.AF_INET6` | IPv6 address family. |
| `socket.SOCK_STREAM` | Stream socket, commonly used for TCP. |
| `socket.SOCK_DGRAM` | Datagram socket, commonly used for UDP. |
| `socket.SHUT_RD` | Disable further receiving. |
| `socket.SHUT_WR` | Disable further sending. |
| `socket.SHUT_RDWR` | Disable sending and receiving. |
| `socket.SOL_SOCKET` | Socket-level options. |
| `socket.SO_KEEPALIVE` | TCP keepalive option. |

---

# 🔄 6. Typical TCP Server Workflow

A TCP server generally uses these methods in the following order:

```text
1. socket()
   |
   v
2. bind()
   |
   v
3. listen()
   |
   v
4. accept()
   |
   v
5. recv() / sendall()
   |
   v
6. close()
```

### Explanation

1. **`socket()`** — Creates the socket.
2. **`bind()`** — Selects the local address and port.
3. **`listen()`** — Waits for incoming connections.
4. **`accept()`** — Accepts a client connection.
5. **`recv()` / `sendall()`** — Exchanges data.
6. **`close()`** — Releases resources.

A client typically creates a socket, calls `connect()`, exchanges data, and closes the connection.

---

# 🛡️ 7. Uses of the Socket Library in Cybersecurity

- **Network automation:** Automate basic connectivity checks.
- **Troubleshooting:** Check whether a service accepts TCP connections.
- **Security monitoring:** Build tools that communicate with network services.
- **Client-server programming:** Understand how network applications exchange data.
- **Security labs:** Learn networking concepts in an authorized environment.

**Important:** A socket connection test is not a complete vulnerability scan. It only tests a particular aspect of network connectivity.

---

# 🎯 8. Interview Question and Answer

### Question: What is the Python socket library?

**Answer:**

The Python socket library is a built-in module used for network communication between programs. It supports socket-based communication using protocols such as TCP and UDP. It provides functions and methods for creating sockets, resolving hostnames, connecting to servers, sending and receiving data, and managing network connections. In cybersecurity, it is useful for network automation, connectivity testing, and learning client-server communication.

---

# 🧠 9. Quick Revision

| Question | Answer |
|---|---|
| What is a socket? | An endpoint for network communication. |
| Which module is used for socket programming? | `socket` |
| How do you import the module? | `import socket` |
| Which constant specifies IPv4? | `socket.AF_INET` |
| Which constant is commonly used for TCP? | `socket.SOCK_STREAM` |
| Which constant is commonly used for UDP? | `socket.SOCK_DGRAM` |
| Which method establishes a client connection? | `connect()` |
| Which method associates a local address with a socket? | `bind()` |
| Which method prepares a TCP socket to accept connections? | `listen()` |
| Which method accepts a connection? | `accept()` |
| Which method receives bytes? | `recv()` |
| Which method sends all supplied bytes? | `sendall()` |
| Which method closes a socket? | `close()` |
| Which method resolves a hostname to IPv4? | `gethostbyname()` |
| Which method sets a timeout? | `settimeout()` |

---

## ✅ Conclusion

The Python `socket` library is an important part of network programming. Understanding sockets, IP addresses, ports, TCP, UDP, and client-server communication provides a strong foundation for learning **network automation and cybersecurity**.
