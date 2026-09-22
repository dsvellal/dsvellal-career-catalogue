# Web-In-and-around

> Converted from presentation 

Internet 

How does it work?? 

An introduction to the technologies behind internet

By, 

Dattatreya S Vellal

dsvellal@gmail.com

Senior Technical Lead - Exeter Group

So... here's a billion dollar question

How does the internet work??

Today's Agenda

Client Side Programming

Server Side Programming

Scripting lanuages

UNIX – Basics

Let's start!!

Client Server Architecture

The Gyan!

What is SGML ?

What is HTML ?

What is XML ?

SGML is a language for describing markup languages, particularly those used in electronic document exchange, document management, and document publishing. 

HTML is a Standard Generalized Markup Language application conforming to International Standard ISO 8879. HTML is widely regarded as the standard publishing language of the World Wide Web.

XML is the shorthand name for Extensible Markup Language. XML is a markup language much like HTML and was designed to describe data. XML tags are not predefined. You must define your own tags according to your needs.

Client Side Programming - HTML

HyperText Markup Language – browsers use to:

Interpret and compose text

Images and other visual or audible 

The purpose of a web browser is:

Read HTML documents

Compose them into visible or audible web pages. 

Note: The browser does not display the HTML tags, but uses the tags to interpret the content of the page.

Client Side Programming - XHTML

XHTML 

(Extensible HyperText Markup Language)

XML markup languages that extends HTML

Stricter syntax rules than HTML. 

Is consistent, well structured format – web pages can be parsed by present and future web browsers. 

Easy to maintain, edit, convert and format.

An XHTML website is compatible to more browsers and rendered more accurately. 

XHTML pages can be rendered by all XML enabled devices

Why is XHTML Strict ??

Not closing empty elements (elements without closing tags in HTML4)

Incorrect: <br>

Correct: <br />

Not closing non-empty elements

Incorrect: <p>This is a paragraph.<p>This is another paragraph.

Correct: <p>This is a paragraph.</p><p>This is another paragraph.</p>

Not putting quotation marks around attribute values

Incorrect: <td rowspan=3>

Incorrect: <td rowspan='3">

Correct: <td rowspan="3">

Correct: <td rowspan='3'>

Using the ampersand character outside of entities 

Incorrect: <title>Cars & Trucks</title>

Correct: <title>Cars &amp; Trucks</title>

Incorrect: <a href="index.php?page=news&id=5">News</a>

Correct: <a href="index.php?page=news&amp;id=5">News</a>

Failing to recognize that XHTML elements and attributes are case sensitive

Incorrect: <BODY><P ID="ONE">The Best Page Ever</P></BODY>

Correct: <body><p id="ONE">The Best Page Ever</p></body>

Client Side Programming:

JavaScript is programming code that can be inserted into HTML pages.

JavaScript is a scripting language 

Adding interactivity to Web pages

Creating web applications. 

Script code may run when

User opens the Web page 

(MVJCE website?)

Clicks or drags some page element with the mouse 

(gmail drag and drop attachments?)

Types something on the keyboard

 (form validations?)

Submits a form 

(facebook wall post?)

Leaves the page 

(exit gmail without quitting?)

Client Side Programming: Javascripts

JS is an interpreted language, optional JIT-compilation support. 

No preliminary compilation

No converstion to system dependent code

Browser reads it and executes it. 

JIT Compilers (Chrome, Firefox, Safari): 

At run time, the browser decides whether (parts of) script code should be JIT-compiled for better performance. 

This makes JavaScript significantly faster and therefore more suitable for complex performance-demanding Web applications. 

Pros and Cons of Javascript

Cons: 

You can't force JavaScript on a browser.

You can't access or affect resources from another internet domain with JavaScript.

You can't access server resources with JavaScript

Pros:

Put text in an HTML page on-the-fly.

Make your web pages responsive.

Detect visitors' browsers.

Create cookies.

Validate web form data.

And much more... 

Event Handling in Javascript

A JavaScript can be executed when an event occurs, like when a user clicks on an HTML element.

Examples of HTML events:

When a user clicks the mouse

When a web page has loaded

When an image has been loaded

When the mouse moves over an element

When an input field is changed

When an HTML form is submitted

When a user strokes a key

Example of Event Handling

<!DOCTYPE html>

<html>

<body>

<h1 onclick="this.innerHTML='Ooops!'">

Click on this text!

</h1>

</body>

</html>

Let's try this

Client Side Programming - CSS

Cascading Style Sheets (CSS) 

Presentation semantics (the look and formatting)

Its most common application is to style web pages

The language can also be applied to any kind of XML document

CSS is designed primarily to enable the separation of document content from document presentation

This separation can 

improve content accessibility

provide more flexibility 

control in the specification of presentation characteristics

enable multiple pages to share formatting

reduce complexity and repetition in the structural content 

CSS can also allow the same markup page to be presented in different styles for different rendering methods, such as: 

On-screen

In print

By voice (Accessibility)

Braille-based

Ttactile devices. 

It can also be used to allow the web page to display differently: 

Depending on the screen size

Device on which it is being viewed. 

In summary

XSLT

XSL Transformations (XSLT) is a standard way to describe how to transform (change) the structure of an XML (Extensible Markup Language) document into an XML document with a different structure. XSLT is a Recommendation of the World Wide Web Consortium (W3C)

XSLT is used to describe how to transform the source tree or data structure of an XML document into the result tree for a new XML document, which can be completely different in structure. 

With XSLT you can add/remove elements and attributes to or from the output file. You can also rearrange and sort elements, perform tests and make decisions about which elements to hide and display, and a lot more.

The original document is not changed; rather, a new document is created based on the content of an existing one.

So we saw... 

Client side programming: 

HTML/XHTML

Javascript

CSS

Server Side Programming: PHP

PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language.

PHP code is interpreted by a web server with a PHP processor module which generates the resulting web page

PHP commands can be embedded directly into an HTML source document rather than calling an external file to process data.

How does PHP work ?

Without PHP- 

With PHP - http://www.mysite.com/page.php

So... 

The server first reads the PHP file carefully to see if there are any tasks that need to be executed. Only when the server has done what it is supposed to do, the result is then sent to the client. It is important to understand that the client only sees the result of the server's work, not the actual instructions.

This means that if you click "view source" on a PHP page, you do not see the PHP codes - only basic HTML tags. Therefore, you cannot see how a PHP page is made by using "view source"

My SQL

With PHP, you can connect to and manipulate databases.

MySQL is the most popular database system used with PHP.

What is MySQL?

MySQL is a database system used on the web

MySQL is a database system that runs on a server

MySQL supports standard SQL

MySQL compiles on a number of platforms

The data in MySQL is stored in tables. A table is a collection of related data, and it consists of columns and rows.

PHP combined with MySQL are cross-platform (you can develop in Windows and serve on a Unix platform)

Scripting languages: Perl

Perl is a general-purpose programming language originally developed for text manipulation

Now used for a wide range of tasks including system administration, web development, network programming, GUI development, and more.

The language is intended to be practical (easy to use, efficient, complete) rather than beautiful (tiny, elegant, minimal). 

Its major features are that it's easy to use, supports both procedural and object-oriented (OO) programming

Has powerful built-in support for text processing

Has one of the world's most impressive collections of third-party modules.

Ruby on Rails

Rails is a web framework built on Ruby, hence the name Ruby on Rails. 

It enables the programmer to easily create advanced database-driven websites using: 

Scaffolding and code generation

Following convention over configuration

Which means that if you stick to a certain set of conventions, a lot of features will work right out of the box with very little code.

Rails is based on a programming pattern called MVC

Model

The model in MVC is a class for each entity in your application. Example models are User, Category, or Product. The models hold all business logic, for example what should happen if you delete a product, add a new category, or create a new user.

View

The views in MVC hold all your presentation and presentation logic, normally HTML. It is based on ERuby which is a templating system that allows for Ruby embedded into HTML and other languages. You probably know this kind of templating system from ASP, PHP, or JSP.

Controller

The controller is what binds together the models and views, for example tells the show product view which product it should show, or handles the data from a form post when a user updates a shopping basket.

The UNIX Operating System

An 

operating system

 (or "OS") is a set of programs that controls a computer

It controls both the 

hardware

 (things you can touch—such as keyboards, displays, and disk drives)

software

 (application programs that you run, such as a word processor).

Some computers have a 

single-user

 OS, which means only one person can use the computer at a time. They can also do only one job at a time. 

But if it has a 

multiuser, multitasking

 operating system like UNIX. Then these powerful OSes can let many people use the computer at the same time and let each user run several jobs at once.

Versions of UNIX

At first there were two main versions: 

The line of UNIX releases that started at AT&T (the latest is System V Release 4), 

And from the University of California at Berkeley (the latest version is BSD 4.4).

Now there are MANY! 

Now commercial versions include SunOS, Solaris, SCO UNIX, SG IRIX, AIX, HP/UX 

The freely available versions include Linux and FreeBSD 5.2 (based on 4.4BSD)

Many Versions of Linux - Redhat, Fedroa, Debian, 

SuSE and MandrakeSoft

Apple Mac OS X (FreeBSD 5.2)

What is different with UNIX

Hardware

UNIX Kernel

Services

Commands & Shell

GUI

User 

Applications

X Windows

UNIX GUI’s -Apple OS X 10.4

UNIX GUI’s -Fedora KDE

UNIX GUI’s -Solaris

UNIX GUI’s -SG IRIX

UNIX and POSIX

POSIX (Portable Operating System Interface for UNIX): A set of programming interface standards governing how to write application source code so that the applications are portable between operating systems. 

POSIX is based on UNIX and is the basis for the X/Open specification of The Open Group. From I-gloss

The POSIX Guarentee

Why all these? Why now?

Credits

http://www.tutorialspoint.com/xhtml/

http://en.wikipedia.org/wiki/HTML

http://en.wikipedia.org/wiki/XHTML

http://www.w3schools.com/js/js_intro.asp

http://www.html.net/tutorials/javascript/lesson1.php

http://www.javascripter.net/faq/whatisja.htm

http://en.wikipedia.org/wiki/Cascading_Style_Sheets

http://reference.sitepoint.com/css/css

http://www.w3schools.com/js/js_htmldom_events.asp

http://www.w3schools.com/xsl/xsl_intro.asp

http://en.wikipedia.org/wiki/XSLT

THANK YOU!