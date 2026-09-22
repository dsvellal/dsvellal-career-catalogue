# Design Patterns An Introduction

> Converted from document `Design Patterns_An_Introduction.pdf`

Design Patterns
An Introduction

By
Dattatreya S Vellal
dsvellal@gmail.com
http://in.linkedin.com/in/dattatreyavellal

Christopher Alexander

The GoF!
Ralph
Johnson

Richard
Helm

Erich
Gamma

John
Vlissides

☺ Disclaimer ☺

BUCKLE UP!

Agenda
• Design and patterns
• Architectural design
• What’s a DP?
• Patterns in Software
• DPs for Software
• DP – Problem & Soln.
• DP Misconceptions

Design and patterns
What is a “design”?
What is a “pattern”?
Design and patterns are thus related. ☺

Design as human activity
Some design activities humans are involved in:

Governed by
- fundamental laws
- rules which humans create.

Design so beautiful
“I call architecture frozen music”
(Johann Wolfgang Goethe)

… now do you see ??

Christopher Alexander
• Born in Austria (October 4, 1936)
• Educated in UK
• Lives and works in USA
• Professor emeritus of architecture
(in Berkeley, California)

Christopher Alexander
• Mathematician: operations research, linear
programming
– a new view of design, what to design, and
how to design.

Architecture and software?
• But WAIT…
– Christopher Alexander in early 1960s
• Used computerized tools
• Developed computer-like algorithms

– There’s was a concern raised about:
• The architectural quality
• Beauty and elegance
• Disappearing Harmony
• Dehumanizing Living environment

Examples of architectural patterns

Examples of architectural patterns

Because it has to be - Utilitarian and Aesthetic in nature!

Alexandrian pattern template
IF
• you find yourself in { context }
• for example { examples }
• with { problem }
• entailing { forces }
THEN
• for some { reasons }
• apply { design from } and/or { rule }
• to construct { solution }
• leading to { new context } and { other paterns }

Pattern formal structure
•
•
•
•
•
•
•
•

Name
Intent
Problem
Context
Forces (Participants and Collaborators)
Solution
Sketch (Implementation)
Resulting context (incl. related patterns)

Wheel DP!
Wheel
•
Intent Need to move heavy objects over long distances efficiently without use of machinery
•

Problem Heavy things are hard or impossible to carry

•

Context But we need to move lots of stuff around now that we have people living in towns who
don’t grow their own food, trade is really important. . .

•

Forces Wheel, axle, bearings, propulsion system (person or beast), road

•

Solution Build vehicles with wheels and smooth surfaces (roads) for them to roll

•

Resulting context Greatly increased capacity and speed. One person or horse can move much
more stuff by pulling a cart than by carrying it. In the longer term, people who control roads get a
lot of power. In the really long term, more and more roads get built until the entire planet is
covered in concrete. . .

•

Sketch Uh. . . shall I explain? (whoever did it was a genius, though)

•

Alternatives Carry the stuff on the backs of people, or on the backs of horses or other beasts of
burden; drag it along the ground; put it on a boat or barge

Patterns in Software
Types of Software Patterns (vis-á-vis Software Life Cycle)

•
•
•
•
•
•

Analysis Patterns
Design Patterns
Implementation Patterns
Process Patterns
Project Planning Patterns
Configuration Management Patterns

We will mostly discuss Design Patterns

Design Patterns in SE
• Why patterns became so important for OO design?
– Cope with rising complexity of software.
– Structural programming, had limited abstraction
– The OO complexities manifest themselves in the relationships
between:
• procedure and associated data (encapsulation)
• procedure names to multiple procedures (polymorphism)
• classes to their parent and sibling classes (inheritance)

• Patterns provide the vocabulary to grasp these
complexities, they extend beyond objects and tie them
together.

Design Patterns benefits
• Easier to reuse successful designs and architectures.
• Create and Prove DPs not for you, but for others!!
• Choose design alternatives
– System reusable
– Avoids alternatives that compromise reusability.

• Improve the documentation and maintenance of existing
systems
– furnishing class and object interactions and their underlying
intent.

DP helps a designer get a design “right” faster.

Software DP template
• In software, the pattern template is somewhat different to
Alexandrian pattern template:
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

Software Design Patterns
There are three basic kinds of design patterns:
Structural

Behavioral

Structural patterns generally
deal with relationships
between entities, making it
easier for these entities to
work together.

Behavioral patterns are used in
communications between entities
and make it easier and more
flexible for these entities to
communicate.

Creational
Creational patterns provide
instantiation mechanisms,
making it easier to create
objects in a way that suits the
situation.

Problem!
• Class A – needed for scenario A
• Class B – needed for scenario B
Problem:
Merge Class A and Class B into a single class

Solution
• Adapter + Strategy Patterns
– Create Class C where:

Strategy Pattern – Behavioral
The strategy pattern is a behavioral design
pattern that allows you to decide which
course of action a program should take,
based on a specific context during
runtime. You encapsulate two different
algorithms inside two classes, and decide
at runtime which strategy you want to go
with.

Strategy Pattern
Example: Class C where: If record already exists
in DB – Update else – Create a new record

Adapter pattern – Structural
The adapter pattern is a structural design
pattern that allows you to repurpose a
class with a different interface, allowing it
to be used by a system which uses
different calling methods.

Non-DP approach

Adapter (or Wrapper) Pattern – Structural

Singleton – Creational
• The singleton design pattern is a
creational design pattern which makes
sure that you have one single instance of
a particular class in the duration of your
runtime, and provides a global point of
access to the single instance.

Singleton - Example

Misconceptions
Patterns are just are
• Jargon?
• Rules?
• Programming tricks or data structures?

Misconceptions about pattern use
• You need tools or methodological support to be effective: No!
• Patterns are primarily food for the brain. Main benefits (again):
– Capturing expertise
– Facilitate communication
– Provide effective documentation
– Allow more efficient design and redesign (restructuring)

Finally!
• A good programmer is one who*:
– Understands the problem and its cause
– Thinks in terms of design patterns
– Gracefully evolves the DP to form:
• Efficient, Scalable and Maintainable code

• Does NOT use DP for DP’s sake!

*Slide Credit: Avinask K Gupta (Senior programmer, Nimbula)

Questions ?

Credits
•http://forgetmenot525.multiply.com/journal/item/750
•http://flowers-macrophotography.blogspot.com/2010/07/pot-marigold-calendula-officinalis.html
•http://www.bustler.net/index.php/article/christopher_alexander_named_eleventh_vincent_scully_prize_l
aureate/
•http://www.designasp.net/blog/cs/post/2009/04/19/Prednaska-Design-Patterns-a-NET.aspx
•http://arlenepasajecartoons.blogspot.com/2009_12_01_archive.html
•http://www.picgifs.com/graphics/agenda/
•http://scenes.malvasiabianca.org/2011/02/page/2/
•http://witchesandwarts.blogspot.com/2011/05/those-fifteen-minutes.html
•http://www.businessenglishebook.com/Business-English-Idioms.htm
•http://harveymillican.files.wordpress.com
•http://www.mitt-romney.net/?tag=richness
•http://www.narutoforums.com/showthread.php?p=37352938
•http://net.tutsplus.com/articles/general/a-beginners-guide-to-design-patterns/

Thank You!

Dattatreya S Vellal
dsvellal@gmail.com
Special mention:
Mr. Alexei Khorev
Department of Computer Science
The Australian National University

