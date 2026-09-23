# Design Patterns Introduction and Evolution Dattatreya S Vellal Talk

> Converted from document `Design Patterns_Introduction and Evolution_Dattatreya S Vellal_Talk.pdf`

Design Patterns
Introduction & Evolution
from
Christopher Alexander
to
The Gang of Four!!
By
Dattatreya S Vellal
Lead developer, Industry Solutions – IBM ISL
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
• Designs humans do
• Architectural design
• Christopher Alexander
• Great architecture
• What’s a DP?
• Patterns in Software
• Patterns and Idioms
• DPs for Software
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

Why architecture is different?
Software Developers (we) want design process:
- Reliable
- Well defined
- Scientific

The Architectural Design
- Methodical process
- An art form.

Design so beautiful
“I call architecture frozen music”
(Johann Wolfgang Goethe)

… now do you see ??

Architecture and software
• Object paradigm in 1980s
– “find-the-object”
– classes and objects v/s increasingly complex systems

• In 1987, Ward Cunningham (CRC cards, Wiki) and Kent Beck (CRC, EP, JUnit)
– design patterns => create => Smalltalk.

• But WAIT…
– An architect, Christopher Alexander (early 1960s)
• computerized tools
• computer-like algorithms

– Alexander concluded that this approach was threatening
– The architectural quality
– Beauty and elegance
– Harmony were disappearing
– Living environment got dehumanized.

Christopher Alexander
• Born in Austria (October 4, 1936)
• Educated in UK
• Lives and works in USA
• Professor emeritus of architecture
(in Berkeley, California)

Ch. Alexander
• Mathematician: operations research, linear programming
– a new view of design, what to design, and how to design”.
– Realized – it was all wrong!!

Quote from his book: Timeless Way of Building

Alexander and his influence!
Notable books he wrote:
– A Pattern Language, 1977
• contains 253 patterns

– The Timeless Way of Building, 1979
– The Nature of Order, 4 books 199x

Wiki claims
• “Notes on the Synthesis of Form” – must read at MIT
• Ward Cunningham (wiki) => The Hillside Group => Design Pattern
philosophy.

Will Wright (born on 20th Jan, 1960, game designer)
• Sims games (SimCity, SimEarth, SimAnt) to Alexander’s influence.

Patterns of great architecture
According to Alexander, the great architectures:
– rigorous, planned designs
– pieces custom fit to each-other and to their environment
– aesthetics is attuned to human needs and comfort
– involve recurring themes (patterns)

Patterns express design in terms:
– relationship between parts of a house
– the rules that transform these relationships.”

This is a holistic approach compared to a method of
building houses from predesigned modules.

Examples of architectural patterns

Examples of architectural patterns

Because it has to be - Utilitarian and Aesthetic in nature!

Parts and the Whole
From The Timeless Way of Building: Design is:
• Synthesis, combination, putting things together.
• Parts – first :: form of the whole – later.
But….
• Character of nature by adding preformed parts?
• Parts are identical, therefore NOT unique
Patterns emphasize the role of relationship
between the parts in determining the nature of
the whole.

What is Design Pattern?
According to Alexander:
(A DP is) “A piece of literature that describes a
design problem and a general solution for the
problem in a particular context”
“Each is a three-part rule, which expresses a
relation between a certain context, a problem
and a solution.
A pattern is a conflict, its resolution and the
resulting synthesis.

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

Abstraction in Software Patterns
• Architectural Patterns (aka macro-architectures) These
are templates for concrete software architectures —
provide central organizing concept which determines the
system integrity
– Dataflow
– Independent component
– Call-and-Return
– Virtual machines
– Repositories
• Design Patterns proper (aka micro-architectures)
• Idioms (aka nano-architectures) They deal with the
implementation of particular design issues

Idioms
Idioms are low-level patterns specific to a particular programming language. According to James
Coplien: “You can master a language only after its idioms become second nature” (IEEE Software,
14(1), p. 36–42, 1997)
In C programming, when a beginner would code like this:
int plaincmp(char* s1, char* s2) {
int i;
for (i = 0; s1[i] == s2[i]; i++)
if (s1[i] == 'n0')
return 0;
return s1[i] s2[i];
}
the experienced programmer simply writes:
int idiomcmp(char* s1, char* s2) {
//pointer arithmetic and "statement is expression" are
crucial
while (*s1++ == *s2++)
if (*s1 == 'n0')
return 0;
return *s1 *s2;
}

Patterns ?= idioms
Other idioms come with languages features or libraries
With Exceptions
loop
read next item
process item
end loop
exception-handler:
when EOF => continue
when others =>
propagate error-exception

Without Exceptions
loop
read next item
if read-past-EOF then
break-exit loop
else process item
end loop

in Java
try {
for (;;) {
process(stream.next());
}
catch (StreamEndException e) {
stream.close();
}

in C
while ((x=getchar()) != EOF)
process(x);
OR even like this
while (g = scanf("%d", &n))
process(n);

Patterns => Features
Singleton in Java:

in Java
public class Singleton {
private static Singleton inst = null;
private Singleton() { ... }
public static Singleton Instance() {
if (inst == null)
inst = new Singleton();
return inst;
}
}

Other examples:
• clone in Java — a rather controversial AIP-based idiom
• direct encapsulation in Java (private access modifier)

Why care about IDIOMS ?
Language features (exception handling):
• Constraint - implementation language
• Increase the complexity of the
implementers'’ job (simulating EH)
• Increase the risks of errors.

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

Aspects of the pattern definition
•
•
•
•

Name Generation Gap
Context After a code was generated by a code-generation tool (eg, in Netbeans GUI
builder), a programmer modifies the code altering the behaviour.
Problem How do you prevent subsequent regeneration from corrupting a
programmer’s modifications?
Forces
–
–
–

•
•

need to control the access to generated internals
comments-based approach ugly, unchecked
auto-diff-and-merge too imprecise

Solution Use inheritance to separate generated code from modifications (generated
classes are immutable)
Consequences
(+) modifications are decoupled from generated code
(+) modifications can have privileged access
(+) subsequent regeneration doesn’t mean reapplying changes
(–) double the number of classes
(–) complicates integration into existing class hierarchies

Misconceptions
Patterns are just are
• Jargon? Not just jargon: a good pattern writer avoids patter-specific
jargon
• Rules? Patterns are not meant to be applied automatically
• Programming tricks or data structures? The solution is an
important aspect, but there are equally important others – problem,
context, intent. . .
Misconceptions about pattern use
You need tools or methodological support to be effective: No!
Patterns are primarily food for the brain. Main benefits (again):
– Capturing expertise
– Facilitate communication
– Provide effective documentation
– Allow more efficient design and redesign (restructuring)

Questions ?

Just before we end…
“Patterns do not guarantee reusable software,
higher productivity, world peace, etc. Patterns
do nothing to remove the human from the
creative process. Patterns are just another
weapon in the developer’s arsenal. To ascribe
more is counterproductive. Under-promise and
over-deliver — that’s the best defense against
hype and backlash.”

Image credits
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

Thank You!

Dattatreya S Vellal
dsvellal@gmail.com
Special mention:
Mr. Alexei Khorev
Department of Computer Science
The Australian National University

