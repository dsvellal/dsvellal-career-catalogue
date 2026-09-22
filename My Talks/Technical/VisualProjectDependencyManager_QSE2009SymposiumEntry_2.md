# VisualProjectDependencyManager QSE2009SymposiumEntry 2

> Converted from document `VisualProjectDependencyManager_QSE2009SymposiumEntry_2.pdf`

VISUAL COMPONENT DEPENDENCY MANAGER TOOL
DATTATREYA S VELLAL
WPLC, SWG – INDIA

Dattatreya (davellal@in.ibm.com) is a development engineer working in IBM
SWG Laboratory at India. He has over 2 years of working experience in IBM
client middleware technologies and SOA/Web services. He is currently a part
of Lotus Expeditor Toolkit Development team in India. He is associated with the
LotusLive team for usability testing and scenario development. His area of
interest includes Eclipse based technologies, Expeditor on Devices and Cloud
Computing.

1

© 2009 IBM Corporation

The “WHAT”
A Visual tool which helps in –
– Viewing dependencies
– Editing dependencies
– Navigating through dependencies
– Searching dependencies
– Performing forward dependency analysis

2

© 2009 IBM Corporation

The “WHY”
Projects Min
Max
Dependency* Dependency*
Websphere
adapters –
Migration plug-in

5

15

WMQ (Client /
XMS Client)

6

22

Expeditor Toolkit

0

27

Telecom
Webservices
Server (TWSS)

16

30

MDM Server

30

40

IM Global Data
Synchronization

unavailable

186

Do you work on plugins ?
Does your code
depend on other projects
?
Does your code
depend on other jars ?

Question –
How do we manage these dependencies ?
3

* Data collected by interacting with
individuals of the respective projects.
* Data refers to project / jar
dependencies.
* Nos. may not be accurate.

© 2009 IBM Corporation

The “WHY” Contd…
Pain Points

Unable to relate
project dependencies

Erm.. I need to delete this
dependency, but do not know

Too many jar dependencies

what will happen if I do !

Visual representation - YES
Visual Editing – NO !

Unable to navigate

Cannot visualize

through dependencies

secondary / tertiary

Do you face the
same problems?
4

dependencies

© 2009 IBM Corporation

The “WHY” Contd…
Dependency management – What’s there ?
– Using IDE’s (Eclipse/ RAD/ WID/ RSA/ Other IDEs)
• In-built dependency viewer / manager

– Manual Dependency Management
• Going through dependencies listed in a file (text mode)

– Using third party dependency visualization tools
• Eg: http://wiki.eclipse.org/Plug-in_Dependency_Visualization

5

© 2009 IBM Corporation

What’s “NEW” ?

Visual representation of dependencies
Browsing through dependencies
Editing dependencies and properties
Searching the “dependency tree”
Forward dependency analysis

6

© 2009 IBM Corporation

Value Proposition
Visualization of Bundle & its dependencies
In a complex dependency scenario involving hundreds of plug-ins,
visual representation of these dependencies would make
maintaining and editing of these dependencies more easier.
Improved usability and maintainability
Allowing the runtime to modify the code (automatic code
generation/ modification ) reduces manual errors.
Auto code generation can be controlled to ensure best practices.
Pluggable
The implementation is eclipse based. So it can be packaged as a
plug-in and made available to users.
Portable
The plug-in generated can be ported to any other IDE that
supports eclipse / plug-in based architecture.
7

© 2009 IBM Corporation

Work in progress - DEMO

Plug-in A

Plug-in B

Existing
workspace
dependencies

Plug-in E

Plug-in C

8

Plug-in D

© 2009 IBM Corporation

Work in progress - DEMO

Plug-in A

Plug-in B
Introducing
additional
dependency

Deleting existing
dependency

Plug-in E

Plug-in C

9

Plug-in D

© 2009 IBM Corporation

Work in progress - DEMO

Scenario
before
dependency
addition

10

Scenario
after
dependency
addition

© 2009 IBM Corporation

Work in progress - DEMO

Scenario
before
dependency
deletion

11

Scenario
after
dependency
deletion

© 2009 IBM Corporation

Work in progress - DEMO
Change visible in the manifest file

12

© 2009 IBM Corporation

