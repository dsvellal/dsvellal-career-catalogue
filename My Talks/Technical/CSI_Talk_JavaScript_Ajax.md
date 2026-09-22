# CSI Talk JavaScript Ajax

> Converted from document `CSI_Talk_JavaScript_Ajax.pdf`

JavaScript and Ajax

- Padmashree K S
- Dattatreya S Vellal
1

Client-side programming
HTML is good for developing static pages

Can specify text/image layout, presentation, links
Web page looks the same each time it is accessed
In order to develop interactive/reactive pages, must
integrate programming
Programs are written in a separate programming language
e.g., JavaScript, VBScript
embedded in the HTML of a Web page with tags
e.g. <script type="text/javascript"> … </script>
the browser executes the program as it loads the page,
integrating the dynamic output of the program with the static
content of HTML
2

Scripting Language
A scripting language is a simple, interpreted
programming language
Scripts are embedded as plain text, interpreted by
application
Simpler execution model
Saves bandwidth
Platform-independence
Slower than compiled code

3

Common scripting tasks
Adding dynamic features to Web pages

Defining programs with Web interfaces
utilize buttons, text boxes, clickable images, prompts,
frames

4

JavaScript – An Introduction

5

JavaScript
The first Web scripting language, developed by Netscape in
1995
Syntactic similarities to Java/C++, but simpler & more
flexible (dynamic variables, simple objects)
JavaScript code can be embedded in a Web page using
SCRIPT tags
The output of JavaScript code is displayed directly in HTML

6

Sample code!
<html>
<!-- Simple Js.html -->
<head>
<title>JavaScript Page</title>
</head>
<body>
<script type="text/javascript">
document.write("Hello world!");
</script>
<p>
Some static text as well.
</p>
</body>
</html>

7

Basics of JavaScript
JavaScript has only three primitive data types
Strings
Numbers
Boolean

Standard C++/Java operators & control statements are provided
in JavaScript
+, -, *, /, %, ++, --,
==, !=, <, >, <=, >=
&&, ||, !
if, if-else, while, do

User defined functions
No return type
No parameter types

8

<html>
<!-- Simple example to demonstrate JS operations -->
<head>
<title>Interactive page</title>
</head>
<body>
<script type="text/javascript">
var userName = prompt("What is your name?", "");
document.write("Hello " + userName + ".")
if (checkAge()<18) {
document.write(" Do your parents know " +
"you are online?");
}
function checkAge(){
var userAge = prompt("Your age?", "");
userAge = parseFloat(userAge);
return userAge;
}
</script>
<p> There is more to it..
</body>
</html>
9

Basics of JavaScript (contd...)
JavaScript Libraries
Define functions that may be useful to many pages and store
in a separate library file.
load a library using the SRC attribute in the SCRIPT tag

JavaScript Strings
Always write with single quotes ' or double quotes "
Used to manipulate a stored content/string

JavaScript Arrays
Arrays store a sequence of items, accessible via an index

10

sample.js
function Strip(str)
{
var copy = "";
for (var i = 0; i < str.length; i++) {
if ((str.charAt(i) >= "A" && str.charAt(i) <= "Z") ||
(str.charAt(i) >= "a" && str.charAt(i) <= "z")) {
copy += str.charAt(i);
}
}
return copy;
}
function IsPalindrome(str)
{
var text = Strip(str.toUpperCase());
for(var i = 0; i < Math.floor(text.length/2); i++) {
if (text.charAt(i) != text.charAt(text.length-i-1)) {
return false;
}
}
return true;
}
11

<html>
<!-- A sample demonstrating JS library and string operations -->
<head>
<title> Palindrome example </title>
<script type="text/javascript" src="sample.js"></script>
</head>
<body>
<script type="text/javascript">
var note = prompt("Enter a word or phrase", "");
if (IsPalindrome(note)) {
document.write("'" + note + "' <b>is</b> a palindrome.");
}
else {
document.write("'" + note + "' <b>is not</b> a palindrome.");
}
</script>
</body>
</html>

12

JavaScript Events
Actions detected by JavaScript
Adds interactivity to pages
Some of the events are
onClick
onChange
onFocus
onSubmit

<html>
<!-- A sample demonstrating JavaScript Event- onclick -->
<head>
<title> JavaScript Event </title>
<script type="text/javascript">
function displayDate(){
document.getElementById("demo").innerHTML=Date();
}
</script>
</head>
<body>
<p id="demo"></p>
<button type="button" onclick="displayDate()">Display Date</button>
</body>
</html>

Ajax – An Introduction

15

What is Ajax?
Asynchronous Javascript And XML
Allows to retrieve data from the server without interfering
with the display and behavior of the existing page
Not a new programming language
Better user experience

16

17

Ajax - modus operandi

18

XMLHttpRequest
Used to exchange data with a server asynchronously
Advantages
Request/Receive data from a server after the page has
loaded
Update a web page without reloading the page

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange=function(){
if (xmlhttp.readyState==4 && xmlhttp.status==200){
document.getElementById("mDiv").innerHTML=xmlhttp.responseText;
}
}
xmlhttp.open("GET","some.xml",false);
xmlhttp.send();

19

Lets try to answer some of the questions...!!
20

21

