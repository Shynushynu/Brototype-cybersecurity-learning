# 🌐 1. UNDERSTAND WEB FUNDAMENTALS

> **PAPER 2 · MODULE 4 · WEB DEVELOPMENT**

> 💡 **Overview**
>
> Web fundamentals are the foundation of web development. They explain
> how websites work, how browsers communicate with servers, how frontend
> and backend systems interact, and how modern web applications are
> structured.

------------------------------------------------------------------------

## 📑 Table of Contents

1.  [🌍 How Websites Work](#1--how-websites-work)
2.  [🖥️ Client-Server Architecture](#2-️-client-server-architecture)
3.  [🎨 Frontend and Backend
    Concepts](#3--frontend-and-backend-concepts)
4.  [🔄 Web Application Workflows](#4--web-application-workflows)
5.  [🏗️ Modern Web Architecture](#5-️-modern-web-architecture)
6.  [🔐 Cybersecurity Perspective](#6--cybersecurity-perspective)
7.  [🎯 Key Takeaways](#7--key-takeaways)
8.  [🎤 Interview Questions](#8--interview-questions)

------------------------------------------------------------------------

## 1. 🌍 How Websites Work

A **website** is a collection of web pages that users can access through
a web browser using the internet.

Whenever we visit a website, several processes happen in the background.

### ⚙️ How a Website Loads

1.  **User Request:** The user enters a website URL in the browser.
2.  **DNS Resolution:** DNS converts the domain name into an IP address.
3.  **Connection Establishment:** The browser establishes a connection
    with the server, usually using TCP and TLS (for HTTPS).
4.  **HTTP Request:** The browser sends an HTTP request to the web
    server.
5.  **Server Processing:** The server processes the request and
    retrieves the required information.
6.  **HTTP Response:** The server sends the requested data back to the
    browser.
7.  **Rendering:** The browser processes HTML, CSS, and JavaScript to
    display the website.

### 🔍 Example

When you visit `https://www.google.com`:

-   Browser requests Google's website.
-   DNS resolves Google's domain name.
-   A secure connection is established.
-   Browser sends an HTTP request.
-   Google's server responds with website resources.
-   Browser renders the webpage.

### 🧰 Important Technologies

  Technology      Purpose
  --------------- --------------------------------------------------
  🌐 DNS          Converts domain names into IP addresses
  📡 HTTP         Communication protocol between client and server
  🔒 HTTPS        Secure HTTP communication
  🏗️ HTML         Defines webpage structure
  🎨 CSS          Controls webpage styling
  ⚡ JavaScript   Adds functionality and interactivity

------------------------------------------------------------------------

## 2. 🖥️ Client-Server Architecture

Client-server architecture is a computing model in which a client
requests services or resources from a server, and the server responds to
those requests.

### 👤 Client

A client is a device or application that requests information or
services from a server.

**Examples:** - Web browsers (Chrome, Firefox). - Mobile applications. -
Desktop applications.

### 🖥️ Server

A server is a computer or software that receives client requests,
processes them, and sends responses.

**Examples:** - Web servers. - Database servers. - Application servers.

### 🔄 How Client-Server Communication Works

1.  Client sends a request to the server.
2.  Server receives the request.
3.  Server processes the request.
4.  Server communicates with the database if necessary.
5.  Server sends a response to the client.
6.  Client displays the received information.

### 💡 Real-World Example

When you log in to Instagram:

-   You enter your username and password.
-   The browser sends login information to the server over HTTPS.
-   The server verifies your credentials.
-   The server responds with the login result.
-   The browser displays your account.

### ⭐ Advantages

-   Centralized data management.
-   Easier maintenance.
-   Better resource sharing.
-   Centralized security management.

------------------------------------------------------------------------

## 3. 🎨 Frontend and Backend Concepts

A web application is generally divided into two major parts: frontend
and backend.

### 🎨 Frontend (Client-Side)

Frontend is the part of a website that users can see and interact with.

**Main Technologies:**

  Technology   Purpose
  ------------ ------------------------------------
  HTML         Creates the structure
  CSS          Adds styling and layout
  JavaScript   Adds interactivity
  React        Builds interactive user interfaces

**Examples:** - Login forms. - Navigation bars. - Buttons. - Images and
animations. - Search boxes.

### ⚙️ Backend (Server-Side)

Backend is the part of a web application that works behind the scenes.

It handles application logic, processes requests, manages data, and
communicates with databases.

**Common Technologies:**

  Technology   Purpose
  ------------ -------------------------------------------------
  Python       Backend programming
  Node.js      JavaScript runtime for server-side applications
  PHP          Server-side programming
  Java         Backend application development
  Django       Python web framework
  Flask        Lightweight Python web framework

**Backend Responsibilities:** - 🔐 User authentication. - ⚙️ Processing
user requests. - 🗄️ Database operations. - 🧠 Business logic. - 🛡️
Access control. - 🍪 Session management.

### 🗄️ Database

A database stores and manages application data.

**Examples:** - MySQL - PostgreSQL - MongoDB - SQLite

### 🔄 Example: Login System

1.  User enters login credentials in the frontend.
2.  Frontend sends the credentials to the backend.
3.  Backend validates the submitted information.
4.  Backend checks the user details in the database.
5.  Backend sends a response.
6.  Frontend displays the result.

------------------------------------------------------------------------

## 4. 🔄 Web Application Workflows

A web application workflow describes how information moves between the
user, frontend, backend, and database.

### ⚙️ Basic Web Application Workflow

**Workflow:**

1.  User performs an action.
2.  Frontend captures the action.
3.  Frontend sends a request to the backend.
4.  Backend processes the request.
5.  Backend communicates with the database if needed.
6.  Database returns the requested information.
7.  Backend sends a response.
8.  Frontend updates the webpage.

### 🔗 What is an API?

API stands for **Application Programming Interface**.

An API allows different software applications or components to
communicate with each other.

💡 **Example:**

A weather application uses a weather API to request weather information
from a weather service.

### 📡 Common HTTP Methods

  Method      Purpose
  ----------- ------------------------------
  🟢 GET      Retrieve data
  🔵 POST     Submit or create data
  🟡 PUT      Replace existing data
  🟠 PATCH    Update part of existing data
  🔴 DELETE   Delete data

### 📋 Common HTTP Status Codes

  Status Code   Meaning
  ------------- --------------------------
  `200`         ✅ OK
  `201`         ✅ Created
  `301`         🔄 Moved Permanently
  `400`         ⚠️ Bad Request
  `401`         🔒 Unauthorized
  `403`         🚫 Forbidden
  `404`         ❌ Not Found
  `500`         🔥 Internal Server Error

------------------------------------------------------------------------

## 5. 🏗️ Modern Web Architecture

Modern web architecture describes how today's web applications are
designed using different components and technologies.

Instead of running everything in one place, modern applications often
separate frontend, backend, databases, and other services.

### 5.1 🧱 Monolithic Architecture

In monolithic architecture, most application components are developed
and deployed as one application.

**Characteristics:** - Application components are tightly connected. -
Usually deployed as one unit. - Easier to start developing. - Can become
difficult to maintain as the application grows.

### 5.2 🧩 Microservices Architecture

Microservices architecture divides an application into smaller
independent services.

**Example: E-commerce Application**

-   👤 User Service -- Manages user accounts.
-   📦 Product Service -- Manages products.
-   💳 Payment Service -- Handles payments.
-   🛒 Order Service -- Manages orders.

**Advantages:** - Independent development. - Easier scaling of
individual services. - Better separation of responsibilities.

### 5.3 ☁️ Cloud-Based Architecture

Cloud-based architecture uses cloud platforms to host and manage
application resources.

**Examples:** - AWS - Microsoft Azure - Google Cloud Platform

**Advantages:** - Flexible resource management. - Scalability. - High
availability options. - Remote accessibility.

### 5.4 ⚡ Serverless Architecture

Serverless architecture allows developers to run backend code without
directly managing the underlying servers.

The cloud provider manages the server infrastructure.

**Examples:** - AWS Lambda. - Azure Functions. - Google Cloud Functions.

### 📊 Architecture Comparison

  Architecture       Main Concept
  ------------------ ---------------------------------------------
  🧱 Monolithic      One integrated application
  🧩 Microservices   Multiple independent services
  ☁️ Cloud-Based     Applications hosted on cloud infrastructure
  ⚡ Serverless      Cloud-managed execution of backend code

------------------------------------------------------------------------

## 6. 🔐 Cybersecurity Perspective

Understanding web fundamentals is important in cybersecurity because web
applications can contain different security vulnerabilities.

### 🛡️ Security Risks in Web Components

  Component               Possible Security Risks
  ----------------------- ---------------------------------------------------
  🎨 Frontend             Client-side manipulation, DOM-based XSS
  ⚙️ Backend              SQL Injection, authentication flaws
  🗄️ Database             Unauthorized access, data exposure
  🔗 API                  Broken access control, API abuse
  🌐 Network              Man-in-the-Middle attacks, insecure communication
  🍪 Session Management   Session hijacking, session fixation

### 📚 Important Security Concepts to Learn

1.  🔒 HTTP vs HTTPS.
2.  🍪 Cookies and sessions.
3.  🔑 Authentication and authorization.
4.  🛡️ Same-Origin Policy (SOP).
5.  🔗 Cross-Origin Resource Sharing (CORS).
6.  💉 SQL Injection.
7.  ⚠️ Cross-Site Scripting (XSS).
8.  🔐 TLS and certificates.

------------------------------------------------------------------------

## 7. 🎯 Key Takeaways

-   🌐 Websites work through communication between browsers and servers.
-   🔍 DNS translates domain names into IP addresses.
-   🔒 HTTP/HTTPS enables communication between clients and servers.
-   🎨 Frontend handles the user interface.
-   ⚙️ Backend handles application logic and data processing.
-   🗄️ Databases store application information.
-   🔗 APIs allow different components to communicate.
-   🏗️ Modern applications use architectures such as monolithic and
    microservices.

------------------------------------------------------------------------

## 8. 🎤 Interview Questions

Test your understanding with these questions:

1.  How does a website work?
2.  What is DNS and why is it required?
3.  What is client-server architecture?
4.  What is the difference between frontend and backend?
5.  What is an API?
6.  What happens when you enter a URL in a browser?
7.  What is the difference between HTTP and HTTPS?
8.  What is the difference between monolithic and microservices
    architecture?
9.  What is the purpose of a database?
10. How does a login request travel from the browser to the server?

------------------------------------------------------------------------

## 💡 Learning Tip

Since you're learning cybersecurity, don't just memorize these concepts.
Try to understand what happens to an HTTP request when it travels from
your browser to a web server.

### 🛤️ Recommended Learning Path

1.  🌐 Web Fundamentals
2.  🏗️ HTML
3.  🎨 CSS
4.  ⚡ JavaScript
5.  📡 HTTP & APIs
6.  ⚙️ Backend Development
7.  🔐 Web Security

------------------------------------------------------------------------

```{=html}
<p align="center">
```
**📘 PAPER 2 · MODULE 4 · TOPIC 1**

*End of Notes*

```{=html}
</p>
```
