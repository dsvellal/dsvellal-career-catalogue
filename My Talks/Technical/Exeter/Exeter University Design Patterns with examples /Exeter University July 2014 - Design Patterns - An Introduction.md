# Exeter University July 2014 - Design Patterns - An Introduction

> Converted from document `Exeter University July 2014 - Design Patterns - An Introduction.pdf`

Design Patterns
An Introduction
Dattatreya S Vellal
OneGate – Senior Tech Lead
Exeter Software India Pvt Ltd

Christopher Alexander

2

The GoF!
Ralph
Johnson

Richard
Helm

Erich
Gamma

John
Vlissides

3

Agenda
• Design and patterns
• Software DP Template
• Common Program Patterns
• Classification of DP
• DP Examples

4

☺ Disclaimer ☺

BUCKLE UP!
5

Design and patterns
What is a “design”?
What is a “pattern”?
Design and patterns are thus related. ☺

6

Design so beautiful
“I call architecture frozen music”
(Johann Wolfgang Goethe)

7

… my EUREKA moment!

8

Examples of architectural patterns

9

Examples of architectural patterns

Because it has to be - Utilitarian and Aesthetic in nature!

10

Key Concept:

Design Pattern 

A design pattern is a combination of classes
and accompanying algorithms that fulfill a
common design purpose.

11

Software DP template
• In software, the pattern template looks like this:
Item

Description

Name (incl. alias)

A unique identifier

Intent

The pattern purpose

Problem

The problem to be solved

Solution

Description of the solution

Participant and Collaborators

The entities (usually classes) involved
in the pattern

Consequences

The pattern trade-offs; discussion of
the forces at play

Implementation

How to implement it

GoF Reference

Page # in the GoF book
12

Let’s talk about common
program patterns used by us!

A few examples!
• Problem: Exposed fields are directly
manipulated from outside, leading to
undesirable dependences that prevent
changing the implementation.

14

Encapsulation pattern
• Solution: Hide some components, permitting
only stylized access to the object.

15

A few examples!
• Problem: Similar abstractions have similar
members (fields and methods). Repeating
these is tedious, error-prone, and a
maintenance headache.

16

Subclassing pattern
• Solution: Inherit default members from a
superclass; select the correct implementation
via run-time dispatching.

17

A few examples!
• Problem: Clients that wish to access all
members of a collection must perform a
specialized traversal for each data structure.

18

Iteration pattern
• Solution: Implementations perform traversals.
The results are communicated to clients via a
standard interface.

19

A few examples!
• Problem: Errors occurring in one part of the
code should often be handled elsewhere.

20

Exception pattern
• Solution: Use language structures for
throwing and catching exceptions.

21

Conclusion
Programming languages are moving towards
Design and many patterns are being
implemented in programming languages.

22

Lets look at software design
patterns!

Software Design Patterns
There are three basic kinds of design patterns:
Structural

Behavioral

Structural patterns generally deal
with relationships between
entities, making it easier for
these entities to work together.

Behavioral patterns are used in
communications between entities
and make it easier and more flexible
for these entities to communicate.

Creational
Creational patterns provide
instantiation mechanisms,
making it easier to create objects
in a way that suits the situation.
24

Classification of DPs

25

Let’s talk design patterns!

Ok.. Situation!
• My configuration file values are NEVER refreshed! Should I read it
again and again in different classes ?
• How can I create a single logger for my application ?
• I need to manage a shared resource across applications, what do I do ?
• How do I manage connections (connection pooling) to my database ?
• How do I store a global-static state of my object ?

27

Singleton Pattern
• The singleton pattern is a design pattern that
restricts the instantiation of a class to one
object.
• The concept is sometimes generalized to
systems that operate more efficiently when
only one object exists, or that restrict the
instantiation to a certain number of objects
28

UML Representation

29

Let’s see an example!

30

Ok.. Next Situation!
• I have a class with 4 properties
• 2 of them are mandatory to create any instance of the class
• 2 of them are optional!
• I need a way to instantiate the class with the mandatory 2 and
any of the combination of the optional 2 properties!

31

Let’s complicate it a bit!
• I have a class with 100 properties
• 3 of them are mandatory to create any instance of the class
• 97 of them are optional!
• I need a way to instantiate the class with the mandatory 3 and
any of the combination of the optional 97 properties!

32

Builder Pattern
• The builder pattern is an object creation software design pattern.
• The intention of the builder pattern is to find a solution to the telescoping
constructor anti-pattern. The telescoping constructor anti-pattern occurs
when the increase of object constructor parameter combination leads to
an exponential list of constructors
• The builder pattern has another benefit. It can be used for objects that
contain flat data (html code, sql query…), that is to say, data that can't be
easily edited. This type of data cannot be edited step by step and must be
edited at once. The best way to construct such an object is to use a builder
class.

33

UML Representation

34

Let’s see an example!

35

Next DP, Factory Method Pattern
• Define an interface for creating an object, but
let the classes that implement the interface
decide which class to instantiate.
• The Factory method lets a class defer
instantiation to subclasses
• Factory method is used when Products don't
need to know how they are created.
36

UML Representation

37

Let’s see an example!

38

Ok, Next Situation!
• You are playing age-of-empires! Your town has the following characters:
–
–
–
–
–
–

A village man – who can be very handy in constructing buildings and collecting things!
A bomber – who can cause maximum damage, but he dies too!
An archer – very accurate at long distance warfare
A soldier – protects people and helps fight battles
A Priest – who heals people and buildings with his MAGIC!
A trader – who travels and trades goods and increases towns wealth

• Situation: You need to –
–
–
–
–

Build your town and construct boundaries to protect your town against invasion
Collect enough gold, wood and stone to aid construction
Explore unknown territory and gain resources
Defend against attacks from your enemies and defeat your enemies

39

Design Pattern – Strategy!
• The strategy pattern
– defines a family of algorithms,
– encapsulates each algorithm, and
– makes the algorithms interchangeable within that family.

• For instance, a class that performs validation on incoming
data may use a strategy pattern to select a validation
algorithm based on:
– the type of data,
– the source of the data,
– user choice, or other discriminating factors.
These factors are not known for each case until run-time, and may
require radically different validation to be performed.
40

UML Representation

41

Interaction

42

Let’s see an example!

43

Ok, Next Situation!
• Ok! I have a class… but I need to add additional functionalities
to the methods of the class, but I can not change or over-ride
those methods, coz they are like my base-templates! What do
I do ?
• What if I want to add additional functionality to an object,
instead of a class ?? Can I do that ??

44

Decorator Pattern
• The decorator pattern can be used to extend (decorate) the
functionality of a certain object statically, or in some cases at
run-time, independently of other instances of the same class,
provided some groundwork is done at design time.
• This pattern is designed so that multiple decorators can be
stacked on top of each other, each time adding a new
functionality to the overridden method(s)
• This difference becomes most important when there are
several independent ways of extending functionality.
45

UML Representation

46

Let’s see an example!

47

Questions ?

48

Thank you!
Exeter University July 2014 - DesignPatternProgramExamples.zip

Dattatreya S Vellal
Email: dvellal@exeter.com
Skype: dsvellal
Extn: 50003

49

Credits
•http://www.designasp.net/blog/cs/post/2009/04/19/Prednaska-Design-Patterns-a-NET.aspx
•http://net.tutsplus.com/articles/general/a-beginners-guide-to-design-patterns/
•http://en.wikipedia.org/
•http://www.bustler.net/index.php/article/christopher_alexander_named_eleventh_vincent_scully_prize_laure
ate/

50

