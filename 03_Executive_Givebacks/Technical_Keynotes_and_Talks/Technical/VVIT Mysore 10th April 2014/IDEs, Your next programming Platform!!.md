# IDEs, Your next programming Platform!!

> Converted from document `IDEs, Your next programming Platform!!.pdf`

IDEs, Your next
programming Platform!!
Dattatreya S Vellal
davellal@in.ibm.com
Staff Software Engineer
Industry Solutions, India Software Labs,
IBM India Pvt. Ltd.

Agenda
Traditional Programming methods
Integrated Development Environment: An
Introduction
Features of an IDE
A note on type of IDE’s
Example IDE: Eclipse & its architecture
Features (with demo)

Programming using text editors!
Features offered:
Syntax Highlighting
Automatic Editing
Compilation and Execution Commands

IDE
A piece of software that acts as text editor,
debugger and compiler all in one sometimesbloated but generally useful package.

Useful Features of an IDE
Refactoring facilities (Renaming affects dependencies/Extract
Method/Extract interface etc.)
Intellisense (or any other code completion functionality)
Error checking (the IDE actually knows its symbols)
No setup hassle
Integrated compiler
Integrated debugger
Better navigation to and from references/declarations
Project templates / file templates
GUI builders
Can autogenerate boilerplate code
It's intuitive and can be used without knowing all the magic keys (hey,
that's why GUIs became successfull in the first place)

IDE Comparision
http://en.wikipedia.org/wiki/Comparison_of_integrated
_development_environments
Types of IDEs:
Multi-language IDEs
IDE’s for Mobile Development
Web based IDEs
IDE’s for MS / Apple apps
IDE’s for specific languages

A sample IDE comparision

What is Eclipse?
Eclipse is an open source project
http://www.eclipse.org
Consortium of companies, including IBM
Launched in November 2001
Designed to help developers with specific
development tasks

Projects
Consists of many separate projects:
Eclipse Project
Eclipse Tools Project
Eclipse Technology Project
Eclipse Web Tools Platform Project
The Eclipse Test and Performance Tools Platform (TPTP)
Project
Business Intelligence and Reporting Tools (BIRT) Project
Data Tools Platform Project (DTP)
Device Software Development Platform (DSDP)

Plug-in Architecture
Eclipse Platform
Workbench

Tool
(plug-in)
Help
Tool
(plug-in)

Workspace

Team

…
Tool
(plug-in)

Platform Runtime

How to get Eclipse
Download the latest version at: http://www.eclipse.org/
You may need to install Java SDK1.5 or JRE if you haven’t from:
http://www.oracle.com/technetwork/java/javase/downloads/index.htm
l
Unzip the zip file
Click on eclipse.exe
That’s it !!
You can configure/download eclipse for:
Java
C, C++
Modeling
Scout
Mobile development
Most of the programming languages!!

How is Eclipse Used?
As an IDE - Integrated Development Environment
Supports the manipulation of various content types
Used for writing code
As a product base
Supported through plug-in architecture and customizations

How is Eclipse Used?
IDE:
Java Development Tooling (JDT) is used for building Java code
Provides set of workbench plug-ins for manipulating Java code
Java projects, packages, classes, methods, ....
Java compiler is built in
Used for compiling Java code
Creates errors (special markers of code) if compilation fails
Production Base:
Eclipse can be used as a Java product base
Its flexible architecture used as a product framework
Reuse plug-in architecture
Create new plug-ins
Customize the environment

Workspace
Represents the desktop development environment
It contains set of tools for resource management
It provides common way of navigating through the resources
Multiple workbenches can be opened at the same time
Represents users data
It is a set of user defined resources
Files: Contain arbitrary number of bytes
Folders: Contain other folders or files
Projects: Collections of files and folders

Help
Used for creating and publishing documentation
There are two different documentation styles:
Help style documentation is published in the user guide
API documentation is published in the programmer guide

Help content is in HTML format
Help navigation is in XML format

Workspace Terminology
Menu bar

Text
editor

Tool bar
Perspective
and
Fast View
bar

Outline
view
Resource
Navigator
view
Bookmarks
view

Properties
view

Message
area
Stacked
views

Editor
Status
area
Tasks
view

Java Perspective
Java-centric view of files in Java projects
Java elements meaningful for Java programmers

Java
project
package
class
field
method

Java
editor

Java Perspective
Browse type hierarchies
“Up” hierarchy to supertypes
“Down” hierarchy to subtypes

Type
hierarchy

Selected
type’s
members

Java Perspective
Search for Java elements
Declarations or references
Including libraries and other projects
Hits
flagged
in margin
of editor

All search
results

Java Editor
Hovering over identifier shows Javadoc spec

Java Editor
Method completion in Java editor

List of plausible methods

Doc for method

Java Editor
On-the-fly spell check catches errors early

Click
to see
fixes
Problem
Quick
fixes

Preview

Java Editor
Code templates help with drudgery

Statement
template

Preview

Java Editor – Refactoring
Refactoring actions rewrite source code
Within a single Java source file
Across multiple interrelated Java source files
Refactoring actions preserve program semantics
Does not alter what program does
Just affects the way it does it
Encourages exploratory programming
Encourages higher code quality
Makes it easier to rewrite poor code

Refactoring
Growing catalog of refactoring actions
Organize imports
Rename {field, method, class, package}
Move {field, method, class}
Extract method
Extract local variable
Inline local variable
Reorder method parameters

Eclipse Java Compiler
Eclipse Java compiler
JCK-compliant Java compiler (selectable 1.3 and 1.4)
Helpful error messages
Generates runnable code even in presence of errors
Fully-automatic incremental recompilation
High performance
Scales to large projects
Multiple other uses besides the obvious
Syntax and spell checking
Analyze structure inside Java source file
Name resolution
Content assist
Refactoring
Searches

Eclipse Java Debugger
Run Java programs
In separate target JVM (user selectable)
Console provides stdout, stdin, stderr
Scrapbook pages for executing Java code snippets
Debug Java programs
Full source code debugging
Any JPDA-compliant JVM
Debugger features include
Method and exception breakpoints
Conditional breakpoints
Watchpoints
Step over, into, return; run to line
Inspect and modify fields and local variables
Evaluate snippets in context of method
Hot swap (if target JVM supports)

Eclipse Java Debugger
Run or debug Java programs
Local variables

Threads
and stack
frames
Editor with
breakpoint
marks
Console
I/O

References
http://programmers.stackexchange.com/questions/40172/should-newbiesuse-ide-autocomplete-intellisense
http://en.wikipedia.org/wiki/Integrated_development_environment
http://java.about.com/od/gettingstarted/a/ideversuseditor.htm
http://programmers.stackexchange.com/questions/102018/what-featuresof-an-ide-would-make-it-more-useful-than-a-general-purpose-editor
http://wiki.wxwidgets.org/List_of_Integrated_Development_Environments
http://hackaday.com/2010/08/24/top-5-integrated-developmentenvironments/
http://mashable.com/2010/10/06/ide-guide/
http://ebookbrowse.com/01-eclipse-introduction-v3-1-ppt-d35611462

Speaker Bio
Dattatreya S Vellal is a staff software engineer in IBM, India
Software Labs. He holds a BE degree from VTU and an MSc
degree from Annamalai University. He joined IBM in 2007 and has
worked on multiple collaboration based softwares in IBM and has coauthored multiple articles on them. He has lead programs from IBM
reaching out to the technical population within IBM and different
colleges and universities - popularizing industry based technologies. He
has also presented in many internal and external conferences. Datta is
a certified competent communicator and competent leader from
Toastmasters International, and has a Patent( yet to be published)
and an Intellectual Property Publication to his name.

Thank you
davellal@in.ibm.com

