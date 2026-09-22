# SOLID Principles of OO Design & Programming

> Converted from document `SOLID_Principles of OO Design & Programming.pdf`

SOLID
Principles of OO Design & Programming
Dattatreya S Vellal
dsvellal@gmail.com
Loves to tinker with 0’s & 1’s
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Agenda
• Why this? Why now?
• It’s time to boast!
• Bad code smells
• Good software design
• Revisiting the basics!
• A SOLID Counter!
• Q&A
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Why this? Why now?

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

It’s time to boast!
• Tell me about the best code you have written so far?
– How many classes?
– How many packages?
– How many interfaces?
– How many layers?
– How many projects?
– How many lines of code?

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Bad code smells!
• Rigidity – Design is hard to change
• Fragility – Design is easy to break
• Immobility – Design is hard to reuse
• Viscosity – It’s hard to do the right thing!

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

What’s a good software design?
• High Cohesion
• Low Coupling
• Follows OO principles
• Uses design patterns
On a lighter note – How do you measure
whether or not the code you wrote, is good or
bad?
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

The ONLY WAY!

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Revisiting the basics!
• What’s an Interface?
• What’s a package?
• What access modifiers do we know?
• What is sub-classing?
• What is Overloading & Overriding?

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Let’s talk about the basics!
• Why do we use an Interface?
• Why do we use a package?
• Why do we use access modifiers?
• Why do we use class hierarchy?
• Why do we use Overloading & Overriding?

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

A SOLID counter!
• S – Single Responsibility Principle
• O – Open Closed Principle
• L – Liskov Substitution Principle
• I – Interface Segregation Principle
• D – Dependency Inversion Principle
Let’s understand them better!
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Single Responsibility Principle

V/S

Fun Fact: I wrote my first C++ code (Paint Editor) and it had 1 class with 900 lines of code! 
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Single Responsibility Principle
• “Just because you can add everything you
need, into your class. It doesn’t mean that you
should!”
• Think in terms of responsibility!
– Does this code belong to this class?

• Create layers & give them responsibility!
– Front-end, Business, Logging, Metrics, Database

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Let’s look at an example!
Report
- IReportFetcher reportFetcher;
- IReportPrinter reportPrinter;
- IReportFormatter reportFormatter;
+ execute() {
Report rawReport = reportFetcher.fetch();
Report formattedReport =
reportFormatter.format(report);
reportPrinter.print(formattedReport);

}

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Open Closed Principle

You don’t need a brain surgery to put on a hat!
Fun Fact: In my editor code, to change my “fill” method, I modified more than 15 methods!
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Open Closed Principle
• “Software entities (Class, methods etc.) should
be open for extension, but closed for
modifications!”
• Extend the base to create a new behavior!
• Abstraction is the key!

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Open Closed Principle
void drawAllShapes(Shape[] list) {
for(int i=0; i<list.size(); i++) {
Shape shape = list[i];
switch(shape.type) {
case square: drawSquare(shape); break;
case circle: drawCircle(shape); break;
}
}
}

interface Shape {
public void draw();
}
Class Square implements Shape {
public void draw() {
System.out.println(“I am a square”);
}
}
Class Circle implements Shape {
public void draw() {
System.out.println(“I am a circle”);
}
}
void drawAllShapes(Shape[] list) {
for(int i=0; i<list.size(); i++) {
list[i].draw();
}
}

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Liskov Substitution Principle

A lesson to be learnt from the “Russian Dolls”

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Liskov Substitution Principle
• “Objects in a program should be replaceable
with instances of their subtypes without
altering the correctness of the program.”
• In other words: “Subclasses should behave
nicely when used in place of their parent
classes”

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Liskov Substitution Principle

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Interface Segregation Principle

Million dollar question is – why should we segregate stuff?
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Interface Segregation Principle
• “Many client-specific interfaces are better
than one general-purpose interface.”
• “You should not have to implement methods
that you don’t use.”
• Low coupling, high cohesion!

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Interface Segregation Principle
interface IWorker {
public void work();
public void eat();
}
class Worker implements IWorker{
public void work() {
}
public void eat() {
}
}
class SuperWorker implements IWorker{
public void work() {
}
public void eat() {
}
}
class Manager {
IWorker worker;
public void setWorker(IWorker w) {
worker=w;
}
public void manage() {
worker.work();
}
}

interface IWorker extends Feedable, Workable {
}
interface IWorkable {
public void work();
}
interface IFeedable{
public void eat();
}
class Worker implements IWorkable, IFeedable{
public void work() {
// ....working
}
public void eat() {
//.... eating in launch break
}
}
class Robot implements IWorkable{
public void work() {
// ....working
}
}
class SuperWorker implements IWorkable, IFeedable{
public void work() {
//.... working much more
}
public void eat() {
//.... eating in launch break
}
}
class Manager {
Workable worker;
public void setWorker(Workable w) {
worker=w;
}
public void manage() {
worker.work();
}

} not distribute without permission.
Content prepared by Dattatreya S Vellal. Do

Dependency Inversion Principle
Tip Implementations!

Tip Interface

Handle Interface
Handle Implementation

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Dependency Inversion Principle
• High-level modules should not depend on
low-level modules. Both should depend on
abstractions.
• Abstractions should not depend on details.
Details should depend on abstractions.

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Dependency Inversion Principle
class Worker {
public void work() {
// ....working
}
}

interface IWorker {
public void work();
}
class Worker implements IWorker{
public void work() {
// ....working
}
}

class Manager {
Worker worker;
public void setWorker(Worker w) {
worker = w;
}

}

public void manage() {
worker.work();
}

class SuperWorker implements IWorker{
public void work() {
//.... working much more
}
}
class Manager {
IWorker worker;

class SuperWorker {
public void work() {
//.... working much more
}
}

public void setWorker(IWorker w) {
worker = w;
}

}

public void manage() {
worker.work();
}

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

In Conclusion…
• Try exploring these principles more because..
– This is the industry standard for coding!
– This will help you think through your code better!
– You will understand the nuances of designing!
– You will, with practice, become a good
programmer!

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Your feedback is valuable!

Survey link
https://goo.gl/L53bmU
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Q&A

dsvellal@gmail.com
Must watch:
https://goo.gl/Z6JdU6
Notes - https://goo.gl/SiH1ee
Content prepared by Dattatreya S Vellal. Do not distribute without permission.

Credits
•
•
•
•
•
•
•
•
•

My wife – for the support!
My friends & family – for tolerating my constant review requests!
Google for images!
http://www.slideshare.net/confiz/solid-principles-of-oo-design-29397774
http://williamdurand.fr/2013/07/30/from-stupid-to-solid-code/
http://www.oodesign.com/interface-segregation-principle.html
http://www.slideshare.net/RiccardoCardin/solid-principles-of-object-oriented-design
https://blogs.msdn.microsoft.com/cdndevs/2009/07/15/the-solid-principles-explained-withmotivational-posters/
https://simpleprogrammer.com/2010/11/13/basic-to-basics-what-is-dependency-inversionis-it-ioc-part-1/

Content prepared by Dattatreya S Vellal. Do not distribute without permission.

