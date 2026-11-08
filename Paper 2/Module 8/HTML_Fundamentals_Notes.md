# 🌐✨ 2. Understand HTML Fundamentals

> 📚 **PAPER 2 • MODULE 4 • THEORY NOTES**

💡 **Introduction:** HTML (HyperText Markup Language) is the standard
markup language used to create and structure web pages. It defines the
content and layout of a website using different elements and tags.

------------------------------------------------------------------------

## 📑 Table of Contents

1.  🏗️ [HTML Structure](#1-html-structure)
2.  📝 [Forms](#2-forms)
3.  ⌨️ [User Inputs](#3-user-inputs)
4.  📂 [Document Structure](#4-document-structure)
5.  🧩 [Web Page Components](#5-web-page-components)
6.  🎯 [Quick Revision](#quick-revision)

------------------------------------------------------------------------

## 🏗️ 1. HTML Structure

HTML structure refers to the basic arrangement of elements required to
create an HTML document.

Every HTML document follows a standard structure.

### 💻 Basic HTML Structure

``` html
<!DOCTYPE html>
<html>
    <head>
        <title>My Website</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <p>This is my website.</p>
    </body>
</html>
```

### 🔍 Important Elements

  Element             Purpose
  ------------------- ----------------------------------------
  `<!DOCTYPE html>`   Declares the HTML version
  `<html>`            Root element of the document
  `<head>`            Contains page information and metadata
  `<title>`           Sets the browser tab title
  `<body>`            Contains visible webpage content

------------------------------------------------------------------------

## 📝 2. Forms

HTML forms are used to collect information from users and send it to a
server for processing.

### 🔍 Common Form Elements

  Element        Purpose
  -------------- --------------------------------
  `<form>`       Creates a form
  `<label>`      Provides a label for an input
  `<input>`      Accepts user information
  `<textarea>`   Accepts multiple lines of text
  `<select>`     Creates a dropdown list
  `<button>`     Creates a clickable button

### 💻 Example

``` html
<form>
    <label>Name:</label>
    <input type="text">

    <label>Email:</label>
    <input type="email">

    <button type="submit">Submit</button>
</form>
```

------------------------------------------------------------------------

## ⌨️ 3. User Inputs

User inputs are HTML elements that allow users to enter or select
information on a webpage.

### 🔍 Common Input Types

  Input Type   Purpose
  ------------ --------------------------------
  `text`       Enter text
  `password`   Enter a password
  `email`      Enter an email address
  `number`     Enter a number
  `radio`      Select one option from a group
  `checkbox`   Select multiple options
  `date`       Select a date
  `file`       Upload a file
  `submit`     Submit a form

### 💻 Example

``` html
<form>
    Username:
    <input type="text">

    Password:
    <input type="password">

    Gender:
    <input type="radio" name="gender"> Male
    <input type="radio" name="gender"> Female

    <input type="checkbox"> Remember Me

    <input type="submit" value="Login">
</form>
```

------------------------------------------------------------------------

## 📂 4. Document Structure

HTML document structure refers to how webpage content is organized using
different HTML elements.

### 🔍 Important Structural Elements

  Element       Purpose
  ------------- ---------------------------------
  `<header>`    Defines the header section
  `<nav>`       Contains navigation links
  `<main>`      Contains the main content
  `<section>`   Groups related content
  `<article>`   Defines independent content
  `<aside>`     Contains additional information
  `<footer>`    Defines the footer section

### 💻 Example

``` html
<body>

    <header>
        <h1>My Website</h1>
    </header>

    <nav>
        <a href="home.html">Home</a>
        <a href="about.html">About</a>
    </nav>

    <main>
        <section>
            <h2>About Us</h2>
            <p>Welcome to our website.</p>
        </section>
    </main>

    <footer>
        <p>Copyright 2026</p>
    </footer>

</body>
```

------------------------------------------------------------------------

## 🧩 5. Web Page Components

Web page components are the individual elements used to build and
display the content of a webpage.

### 🔍 Common Components

  Component   HTML Element       Purpose
  ----------- ------------------ -----------------------
  Heading     `<h1>` to `<h6>`   Displays headings
  Paragraph   `<p>`              Displays text
  Image       `<img>`            Displays images
  Link        `<a>`              Creates hyperlinks
  List        `<ul>`, `<ol>`     Displays lists
  Table       `<table>`          Displays tabular data
  Button      `<button>`         Creates buttons
  Division    `<div>`            Groups elements
  Span        `<span>`           Groups inline content
  Video       `<video>`          Embeds videos

------------------------------------------------------------------------

## 🎯 Quick Revision

  -----------------------------------------------------------------------
  Topic                               Key Point
  ----------------------------------- -----------------------------------
  🏗️ HTML Structure                   Basic arrangement of an HTML
                                      document

  📝 Forms                            Used to collect information from
                                      users

  ⌨️ User Inputs                      Allow users to enter or select data

  📂 Document Structure               Organizes webpage content into
                                      meaningful sections

  🧩 Web Page Components              Individual elements used to build a
                                      webpage
  -----------------------------------------------------------------------

------------------------------------------------------------------------

> 🚀 **Remember:** HTML provides the structure of a webpage, CSS
> controls its appearance, and JavaScript adds interactivity.

**✅ Paper 2 -- Module 4 \| HTML Fundamentals**
