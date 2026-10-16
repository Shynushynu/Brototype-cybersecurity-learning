# 🔍 Service Availability Check Using Python

## 📌 Overview

Service availability checking is the process of automatically verifying whether a network service is reachable through a specific IP address and port number.

In Python, we can use the `socket` library to create a TCP server and a client that checks the service's availability.

### 🎯 Objectives

- Understand TCP client-server communication.
- Create a local TCP server.
- Check whether a service is reachable.
- Send and receive data using sockets.
- Handle connection errors using exception handling.

---

## 🖥️ 1. Create a TCP Server

**File name:** `server.py`

The server listens for incoming TCP connections on `127.0.0.1`, port `8080`. When a client connects, it sends a response message.

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8080))
server.listen(5)

print("Server is running on port 8080...")

try:
    while True:
        client, address = server.accept()

        print("Client connected:", address)
        client.sendall(b"Service is available!")

        client.close()

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server.close()
```

### 🔎 Explanation

| Method | Purpose |
|---|---|
| `socket()` | Creates a TCP socket. |
| `bind()` | Assigns an IP address and port to the server. |
| `listen(5)` | Allows the server to queue incoming connection requests. |
| `accept()` | Waits for a client and accepts its connection. |
| `sendall()` | Sends the complete message to the client or raises an error. |
| `close()` | Closes the socket and releases its resources. |

---

## 🔌 2. Create a Service Availability Checker

**File name:** `checker.py`

The client attempts to connect to the local server. If the connection succeeds, it receives the server's response.

```python
import socket

ip_address = "127.0.0.1"
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)

try:
    client.connect((ip_address, port))
    print("Service is reachable!")

    response = client.recv(1024)
    print("Server response:", response.decode())

except OSError as error:
    print("Service is unavailable:", error)

finally:
    client.close()
```

### 🔎 Explanation

| Method | Purpose |
|---|---|
| `socket()` | Creates a TCP client socket. |
| `settimeout(5)` | Sets a five-second timeout for socket operations. |
| `connect()` | Attempts to connect to the server. |
| `recv(1024)` | Receives up to 1024 bytes of data. |
| `decode()` | Converts received bytes into a string. |
| `except OSError` | Handles socket and connection errors. |
| `finally` | Ensures the client socket is closed. |

---

## ▶️ 3. How to Run Both Programs

### Step 1: Start the server

Open the first terminal and run:

```bash
python server.py
```

Expected output:

```text
Server is running on port 8080...
```

Keep this terminal running.

### Step 2: Run the checker

Open a second terminal in the same directory and run:

```bash
python checker.py
```

Expected output:

```text
Service is reachable!
Server response: Service is available!
```

### Step 3: Check the server terminal

The server displays a message when a client connects.

```text
Server is running on port 8080...
Client connected: ('127.0.0.1', <client_port>)
```

`<client_port>` represents the client's dynamically assigned local port.

---

## 🔄 4. How the Program Works

1. The server creates a TCP socket.
2. The server binds to `127.0.0.1:8080`.
3. The server starts listening for incoming connections.
4. The checker creates a client socket.
5. The checker connects to the server.
6. The server accepts the connection and sends a message.
7. The checker receives and displays the message.
8. Both sides close their respective client sockets.

---

## 🧠 5. Important Concepts

| Concept | Meaning |
|---|---|
| IP address | Identifies the network interface used to reach the destination. |
| Port number | Identifies the destination service or application endpoint. |
| TCP | A connection-oriented transport protocol. |
| Client | Initiates a connection to a server. |
| Server | Listens for and accepts client connections. |
| Timeout | Limits how long a socket operation waits. |
| Exception handling | Handles errors without abruptly terminating the program. |
| Service availability | Whether a service can be reached and, when tested, responds as expected. |

### ⚠️ Important Note

A successful TCP connection confirms that a connection was established, but it does not necessarily prove that the application is functioning correctly. Checking the server's response provides an additional basic application-level check.

This example runs on the local computer using the loopback address `127.0.0.1`. Test network services only on systems you own or have permission to assess.

---

## 🎯 Interview Answer

Service availability checking is the process of verifying whether a network service is reachable through a particular IP address and port number. In Python, I can use the `socket` library to create a TCP client that connects to a server, checks the connection, receives a response, and handles errors using exception handling. This helps automate basic service monitoring and troubleshooting.
