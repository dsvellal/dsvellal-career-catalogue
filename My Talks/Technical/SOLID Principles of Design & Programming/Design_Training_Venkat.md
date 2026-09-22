# Design Training Venkat

> Converted from presentation `Design_Training_Venkat.pptx`


## Slide 1

- HSDP-PH : Design Training
- Design Principles(SOLID)
- Design Pattern
- Refactoring
- HSDP
- Venkateshan Pandi
- Architecture and Product owner Group


## Slide 2: Agenda

- What is good design?
- What is bad design? Rotting Design Symptoms
- Two core principles: Cohesion and Coupling
- 5 OO Design Principles based on the core principles (SOLID) + 2 bonus guidelines (DRY and YAGNI)
- Most commonly used Design Pattern
- Factory Method
- Builder Pattern
- Strategy
- Decorator
- State
- Composite
- Command
- Template Method
- Observer
- Adapter
- Visitor
- Refactoring
- What is Refactoring?
- Why is it necessary?
- Code smell (Bad code) List
- Around 20 – 30 Refactoring patterns
- Tools – Like Refactor!


## Slide 3: Good Design

- We are talking about design that not only meets today’s requirements, but is ready for tomorrow’s requirements!
- “...when dependencies are well managed, the code remains flexible, robust, and reusable...therefore these principles, are at the foundation of the -ilities that software developers desire”. Uncle Bob

> **Notes:** http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod



## Slide 4: Good Design = Maintainable Software

- Maintainability : is a measure of the cost of introducing change in Software.
- What influences maintainability?
- What makes it difficult to change code?


## Slide 5: What is bad design?

- Rigidity
- Fragility
- Immobility
- Viscosity


## Slide 6: Rigidity

- The tendency for software to be difficult to change, even in simple ways.
- Every change causes a cascade of subsequent changes in dependent modules.

> **Notes:** What begins as a simple two day change to one module grows into a multiweek marathon of change in module after module as the engineers chase the thread of the change through the application.
When software behaves this way, managers fear to allow engineers to fix non-critical problems. This reluctance derives from the fact that they don’t know, with any reliability, when the engineers will be finished. If the managers turn the engineers loose on such problems, they may disappear for long periods of time. The software design begins to take on some characteristics of a roach motel -- engineers check in, but they
don’t check out.
When the manager’s fears become so acute that they refuse to allow changes to software, official rigidity sets in. Thus, what starts as a design deficiency, winds up being adverse management policy.



## Slide 7: Fragility

- The tendency of the software to break in many places every time it is changed.
- Closely related to rigidity is fragility
- Often the breakage occurs in areas that have no conceptual relationship with the area that was changed

> **Notes:** Closely related to rigidity is fragility. Fragility is the tendency of the software to break in many places every time it is changed. Often the breakage occurs
in areas that have no conceptual relationship with the area that was changed. Such errors fill the hearts of managers with foreboding. Every time they authorize a fix, they fear that the software will break in some unexpected way.  As the fragility becomes worse, the probability of breakage increases with time, asymptotically approaching 1. Such software is impossible to maintain. Every fix makes it worse, introducing more problems than are solved.

Such software causes managers and customers to suspect that the developers have lost control of their software. Distrust reigns, and credibility is lost.



## Slide 8: Immobility

- The inability to reuse software from other projects or from parts of the same project
- Software is simply rewritten instead of reused.

> **Notes:** Immobility is the inability to reuse software from other projects or from parts of the same project. It often happens that one engineer will discover that he
needs a module that is similar to one that another engineer wrote. However, it also often happens that the module in question has too much baggage that it depends upon.  After much work, the engineers discover that the work and risk required to separate the desirable parts of the software from the undesirable parts are too great to tolerate.
And so the software is simply rewritten instead of reused.



## Slide 9: Viscosity

- Viscosity of the design – deviations from the original principles.
- Viscosity of the environment – designs made with environmental constraints (build time, check in time etc) rather than focused on design constraints.

> **Notes:** Viscosity comes in two forms: viscosity of the design, and viscosity of the environment. When faced with a change, engineers usually find more than one way to make the change. Some of the ways preserve the design, others do not (i.e.they are hacks.) When the design preserving methods are harder to employ than the hacks, then the viscosity of the design is high. It is easy to do the wrong thing, but hard to do the right thing.

Viscosity of environment comes about when the development environment is slow and inefficient. For example, if compile times are very long, engineers will be tempted to make changes that don’t force large recompiles, even though those changes are not optimal from a design point of view. If the source code control system requires hours to check in just a few files, then engineers will be tempted to make changes that require as few check-ins as possible, regardless of whether the design is preserved



## Slide 10: Summary

- These four symptoms are the tell-tale signs of poor architecture. Any application that exhibits them is suffering from a design that is rotting from the inside out.
- But what causes that rot to take place?
- Do check you projects for this symptoms?
- Courtesy: Robert C. Martin, www.objectmentor.com


## Slide 11: Two Core Principles: Coupling and Cohesion

- Aim for loose external coupling means one change does not influence all other parts of the software
- lowering cost of change
- Aim for high internal cohesion means that a change is likely localized in a single subsystem, easier to spot
- lowering the cost of change


## Slide 12: Coupling

- Coupling : is a measure of how strongly dependent one software unit is on other software units.
- Unit, is a well delimited unit of code: class, package, module, method, application, etc.
- Loose external coupling: few dependencies
- Tight external coupling: lot of dependencies


## Slide 13: Coupling - Example

- Change
- Change
- Fig. a
- Fig. b


## Slide 14: Coupling: Degree of dependence among components

- No dependencies
- Loosely coupled-some dependencies
- Highly coupled-many dependencies
- High coupling makes modifying parts of the system difficult, e.g., modifying a component affects all the components to which the component is connected.


## Slide 15: Coupling – Exercise

- What are all the OO language constructs or techniques that brings dependencies between two classes.

> **Notes:** objec references
global access to variables
database access
method calls
formats on Data
interpretations on data



## Slide 16: Coupling - rule

- Assign responsibility so coupling is low
- Benefits,
- Local change has no/less impact
- Easier to understand modules in isolation
- Higher probability of reuse with few dependencies


## Slide 17: Range of Coupling

- High Coupling
- Loose
- Low
- Content
- Common
- Control
- Stamp
- Data
- Uncoupled


## Slide 18: Content coupling

- Definition: One component references contents of another
- Example:
- Component directly modifies another’s data
- Component refers to local data of another component in terms of numerical displacement
- Component modifies another’s code, e.g., jumps into the middle of a routine

> **Notes:** Pp220+ pfleeger



## Slide 19: Example of Content Coupling-1

- Part of program handles lookup for customer.
- When customer not found, component adds customer by directly modifying the contents of the data structure containing customer data.


## Slide 20: Example of Content Coupling-2

- Part of program handles lookup for customer.
- When customer not found, component adds customer by directly modifying the contents of the data structure containing customer data.
- Improvement:
- When customer not found, component calls the AddCustomer() method that is responsible for maintaining customer data.


## Slide 21: Common Coupling

- Definition: Two components share data
- Global data structures
- Common blocks
- Usually a poor design choice because
- Lack of clear responsibility for the data
- Reduces readability
- Difficult to determine all the components that affect a data element (reduces maintainability)
- Difficult to reuse components
- Reduces ability to control data accesses

> **Notes:** Pp220+ pfleeger



## Slide 22: Example-1

- Each source process writes directly to global data store. Each sink process reads directly from global data store.
- Process control component maintains current data about state of operation. Gets data from multiple sources. Supplies data to multiple sinks.


## Slide 23: Example-2

- Each source process writes directly to global data store.
- Each sink process reads directly from global data store.
- Improvement
- Data manager component is responsible for data in data store.
- Processes send data to and request data from data manager.
- Process control component maintains current data about state of operation. Gets data from multiple sources. Supplies data to multiple sinks.


## Slide 24: Control Coupling

- Definition: Component passes control parameters to coupled components.
- May be either good or bad, depending on situation.
- Bad when component must be aware of internal structure and logic of another module
- Good if parameters allow factoring and reuse of functionality

> **Notes:** Example of good: Sort that takes a comparison function as an argument.
The sort function is clearly defined: return a list in sorted order, where sorted is determined by a parameter.



## Slide 25: Example

- Acceptable: Module p calls module q and q passes back flag that says it cannot complete the task, then q is passing data
- Not Acceptable: Module p calls module q and q passes back flag that says it cannot complete the task and, as a result, writes a specific message.

> **Notes:** In right hand side, the sort code is unchanged.



## Slide 26: Stamp Coupling

- Definition: Component passes a data structure to another component that does not have access to the entire structure.
- Requires second component to know how to manipulate the data structure (e.g., needs to know about implementation)
- May be necessary due to efficiency factors: this is a choice made by insightful designer, not lazy programmer.

> **Notes:** Be sure you know the difference between the insightful designer and the lazy programmer.
Know what tradeoffs you are making in your design.



## Slide 27: Example-1

- The print routine of the customer billing accepts a customer data structure as an argument, parses it, and prints the name, address, and billing information.
- Customer billing system


## Slide 28: Example-2

- The print routine of the customer billing accepts a customer data structure as an argument, parses it, and prints the name, address, and billing information.
- Improvement
- The print routine takes the customer name, address, and billing information as an argument.
- Customer Billing System


## Slide 29: Data Coupling

- Definition: Two components are data coupled if there are homogeneous data items.
- Every argument is simple argument or data structure in which all elements are used
- Good, if it can be achieved.
- Easy to write contracts for this and modify component independently.


## Slide 30: Coupling - Summary

- Object-oriented designs tend to have low coupling.


## Slide 31: Cohesion:



## Slide 32: Cohesion

- Cohesion: is a measure of how strongly related and focused the responsibilities of a software unit is.
- The degree to which all elements of a component are directed towards a single task and all elements directed towards that task are contained in a single component.
- Internal glue with which  component is constructed
- All elements of component are directed toward and essential for performing the same task


## Slide 33: Cohesion - Example

- Subsystem X:
- All classes whose name begins with either A, B, or C.
- Subsystem Y:
- All classes related to the booking of a seat in a flight.
- What is the cohesion of System.util? System.console?


## Slide 34: Level of cohesion

- Functional Cohesion
- Sequential Cohesion
- Communicational Cohesion
- Procedural Cohesion
- Temporal Cohesion
- Logical Cohesion
- Coincidental Cohesion


## Slide 35: Good Cohesion


> **Notes:** Is informational and communicational different?
Are functional, informational/communicational and sequential really arranged in order?  
Isn’t functional the cohesion you are trying to achieve for a function, informational the cohesion you are trying to achieve for a class/object and sequential for a pipeline architecture?



## Slide 36: Poor Cohesion


> **Notes:** Definition: Parts of the component are only related by their location in source code.  Elements needed to achieve some functionality are scattered throughout the system.  Accidental and worst form



## Slide 37

- Coincidental Cohesion
- Definition: Module is one whose activities have no meaningful relationship to one another.
- Example: Module one which performs various functions such as computing net pay, calculating inventory reorder amount or generating an invoice depending on the value of the parameters passed to the module.


## Slide 38: Logical Cohesion

- Definition: Elements of component are related logically and not functionally.
- Several logically related elements are in the same component and one of the elements is selected by the client component.
- Example: module is a general I/O routine which reads, writes or deletes various combinations of records, depending on the value of a control flag.


## Slide 39: Logical Cohesion - Example

- A component reads inputs from tape, disk, and network. All the code for these functions are in the same component. Operations are related, but the functions are significantly different.
- Code Smell
- A case statement switching between input types
- Improvement
- A device component has a read operation that is overridden by sub-class components. The tape sub-class reads from tape. The disk sub-class reads from disk. The network sub-class reads from the network.

> **Notes:** I don’t even want to think about it.



## Slide 40: Temporal Cohesion

- Definition: Elements of a component are related by timing.
- Difficult to change because you may have to look at numerous components when a change in a data structure is made.
- Increases chances of regression fault
- Component unlikely to be reusable.
- Example: module is an initialization routine that initializes data used by many modules throughout a system.


## Slide 41: Temporal Cohesion - Example

- A system initialization routine: this routine contains all of the code for initializing all of the parts of the system. Lots of different activities occur, all at init time.
- Code Smell
- A single class/routine that is coupled to every other part of the system.
- Improvement
- A system initialization routine sends an initialization message to each component.
- Each component initializes itself at component instantiation time.

> **Notes:** I don’t even want to think about it.



## Slide 42: Procedural Cohesion

- Definition: Elements of a component are related only to ensure a particular order of execution.
- Actions are still weakly connected and unlikely to be reusable
- Module performs several different and possibly unrelated activities in which control flows from each activity within the module to the next.


## Slide 43: Example

- ...
- Read part number from data base
- update repair record on maintenance file.
- ...
- May be useful to abstract the intent of this sequence. Make the data base and repair record components handle reading and updating. Make component that handles more abstract operation.


## Slide 44: Communicational Cohesion

- Definition: Module performs a series of actions related by a sequence of steps to be followed by the product and all actions are performed on the same data
- Module is one which performs several functions on the same input or output data
- Example: obtain author, title, or price of the book from bibliographic record, based on a passed flags.


## Slide 45: Example

- Update record in data base and send it to the printer.
- database.Update (record).
- record.Print().

> **Notes:** I don’t even want to think about it.



## Slide 46: Sequential Cohesion

- The output of one component is the input to another.
- Occurs naturally in functional programming languages
- Good situation
- Example: module retrieve customer, retrieve customer order, and generate invoice


## Slide 47: Informational Cohesion

- Definition: Module performs a number of actions, each with its own entry point, with independent code for each action, all performed on the same data.
- Different from logical cohesion
- Each piece of code has single entry and single exit
- In logical cohesion, actions of module intertwined
- ADT and object-oriented paradigm promote


## Slide 48: Functional Cohesion

- Definition: Every essential element to a single computation is contained in the component.
- Every element in the component is essential to the computation.
- Performs one and only one problem related task
- Ideal situation.
- Example:
- Drag Drop – an event triggered when a dragged object is dropped on a window,
- Sum elements in Arrays
- Convert Kilometers to miles
- Calculate Net Pay


## Slide 49: Problem: Classify cohesion for each module

- Compute average daily temperatures at various sites
- Initialize sums and open files
- Create new temperature record
- Store temperature record
- Close files and print average temperatures
- Read in site, time, and temperature
- Store record for specific site
- Edit site, time, or temperature field


## Slide 50: Let’s come back to Maintainability…

- Maintainable software generally has loose external coupling and high internal cohesion.
- Loose external coupling means one change does not influence all other parts of the software
- lowering cost of change
- High internal cohesion means that a change is likely localized in a single subsystem, easier to spot
- lowering the cost of change


## Slide 51: Questions…

- P1: What is the effect of cohesion on maintenance?
- P2: What is the effect of coupling on maintenance?
- P3: Produce an example of each type of cohesion. Justify your answers.
- P4: Produce an example of each type of coupling. Justify your answers.

> **Notes:** I don’t even want to think about it.



## Slide 52: Characteristics of Good Design

- Component independence (high internal cohesion and loose external coupling)
- Exception identification and handling
- Fault prevention and fault tolerance


## Slide 53: Design Principles



## Slide 54: S.O.L.I.D. OO Code

- SOLID is a set of design principles
- First collected and described by Robert Martin in 2008 “Principles and Patterns” book
- Guidelines, not mandates


## Slide 55: S.O.L.I.D. code

- Single responsibility principle
- Open closed principle
- Liskov substitution principle
- Dependency inversion principle
- Interface segregation principle


## Slide 56: Single Responsibility Principle (SRP)

- A responsibility is a reason to change
- More responsibilities = more coupling
- Coupling between dependencies means changing one responsibility
- Impacts others
- Restricts others
- Increases test area
- Fragile!
- A class should only have one reason to change


## Slide 57: SRP - Example #1

- MainForm uses MenuBar, StatusBar, AllowClose
- WindowManager uses Id, OwnerName, Type
- Multiple responsibilities, so how do we fix it?


## Slide 58: SRP - Separate the responsibilities

- DocumentWindow and UIDocumentWindow now only have one reason to change


## Slide 59: SRP Example #2

- public interface IModem
- {
- void Dial(string phoneNumber);
- void Hangup();
- void Send(char c);
- char Recv();
- }
- Where are the responsibilities here?
- Where is the code most likely to change?

> **Notes:** -Making/Breaking a connection
-Send/Receive
Change is likely for ADSL modem, or Satellite, or Ethernet, etc



## Slide 60



## Slide 61: SRP practicalities

- Many (many) small classes
- Hard to start this way, and you probably shouldn’t try
- Preparing for change
- Cohesion is a way to split along responsibilities

> **Notes:** Preparing for change
If you need to modify a class to meet a new requirement, think about the SRP and if you should redesign the class



## Slide 62: SRP - Cohesion

- Cohesion is the amount to which a classes methods use it’s member variables
- A class with a maximum level of cohesion means each method is using each member variable
- Classes with multiple responsibilities tend to have member variable and method groupings
- Assign responsibility so cohesion is high

> **Notes:** Cohesion: is a measure of how strongly related and focused the responsibilities of a software unit is.
The degree to which all elements of a component are directed towards a single task and all elements directed towards that task are contained in a single component.
Internal glue with which  component is constructed
All elements of component are directed toward and essential for performing the same task



## Slide 63: SRP – A Final example

- public class TwoNumberMath
- {
- private readonly int _first;
- private readonly int _second;
- public TwoNumberMath(int first, int second)
- {
- _first = first;
- _second = second;
- }
- public int Add()
- {
- return _first + _second;
- }
- public int Subtract()
- {
- return _first - _second;
- }
- }
- Two reasons this could change
- Multiply operation needs to be added
- An individual method needs to be changed


## Slide 64: SRP – Example Solution

- We can now add more operations or modify existing ones
- public abstract class TwoNumberMath
- {
- protected int First { get; private set;}
- protected int Second { get; private set; }
- protected TwoNumberMath(int first, int second)
- {
- First = first;
- Second = second;
- }
- public abstract int Operate();
- }
- internal class Add : TwoNumberMath
- {
- public Add(int first, int second)
- : base(first, second)
- {
- }
- public override int Operate()
- {
- return First + Second;
- }
- }
- internal class Subtract : TwoNumberMath
- {
- public Subtract(int first, int second)
- : base(first, second)
- {
- }
- public override int Operate()
- {
- return First - Second;
- }
- }


## Slide 65: S.O.L.I.D. code

- Single responsibility principle
- Open closed principle
- Liskov substitution principle
- Dependency inversion principle
- Interface segregation principle


## Slide 66: Open Closed Principle (OCP)

- “Open for extension”
- Behavior of the module can be extended. i.e. we can make the module meet the needs of new requirements
- “Closed for modification”
- No changes to the module are allowed
- Conflicting?
- Abstractions are our new best friend
- Software entities should be open for extension,
- but closed for modification

> **Notes:** If a single change requires cascading changes to dependent modules, we understand that this is a bad design.  Rigid, unreusable, fragile. 

OCP says you should design classes that never change.  When requirements change, you extend the behaviour of modules by adding new code, not by changing old code that works



## Slide 67: OCP - Abstractions

- An abstraction can take the form of an abstract base class or interface


## Slide 68: OCP - Example

- Consider the following Draw Shape
- public enum ShapeType
- {
- Circle,
- Square
- }
- public class Shape
- {
- public ShapeType Type { get; set; }
- }
- public class DrawAllShapes
- {
- public void DrawShapes(IList<Shape> shapes)
- {
- foreach (var shape in shapes)
- {
- switch (shape.Type)
- {
- case ShapeType.Circle:
- DrawCircle(shape);
- break;
- case ShapeType.Square:
- DrawSquare(shape);
- break;
- }
- }
- }
- private void DrawSquare(Shape shape)
- {
- //implementation
- }
- private void DrawCircle(Shape shape)
- {
- //implementation
- }
- }


## Slide 69: OCP – Example

- This solution conforms to OCP
- public interface IShape
- {
- void Draw();
- }
- internal class Circle : IShape
- {
- public void Draw()
- {
- //Implementation
- }
- }
- internal class Square : IShape
- {
- public void Draw()
- {
- //Implementation
- }
- }
- public class DrawAllShapes
- {
- public void DrawShape(IList<IShape> shapes)
- {
- foreach (var shape in shapes)
- {
- shape.Draw();
- }
- }
- }


## Slide 70: OCP practicalities

- OCP drives many of the conventions we adhere to in everyday programming
- Make all member variables private
- No global variables
- Select case/switch statements are a design smell


## Slide 71: S.O.L.I.D. code

- Single responsibility principle
- Open closed principle
- Liskov substitution principle
- Dependency inversion principle
- Interface segregation principle


## Slide 72: Liskov Substitution Principle (LSP)

- Or
- “What is wanted here is something like the following substitution property: If for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T.” [Barbara Liskov 1998]
- Functions that use references to base classes must be
- able to use objects of derived types without knowing it.


## Slide 73: LSP – No up-casting

- If a method takes a base class as a parameter, and then up-casts it to a derived type, it violates LSP
- public abstract class Shape
- {
- abstract public void Draw();
- }
- internal class Circle : Shape
- {
- public override void Draw()
- {
- //Implementation
- }
- public void PreDrawCircle()
- {
- //Implmentation
- }
- }
- internal class Square : Shape
- {
- public override void Draw()
- {
- //Implementation
- }
- public void PostDrawSquare()
- {
- //Implmentation
- }
- }
- public class DrawAllShapes
- {
- public void DrawShapes(IList<Shape> shapes)
- {
- foreach (var shape in shapes)
- {
- if (shape is Square)
- {
- shape.Draw();
- ((Square)shape).PostDrawSquare();
- }
- if (shape is Circle)
- {
- shape.Draw();
- ((Circle)shape).PreDrawCircle();
- }
- }
- }
- }

> **Notes:** Draw shape must know every derivative of shape, and must change when new derivatives are added (violation of SRP)



## Slide 74: LSP – Subtle example

- What is wrong with the following?
- public class Rectangle
- {
- public int Width { get; set; }
- public int Height { get; set; }
- }
- public class Square : Rectangle
- {
- }

> **Notes:** Change the width and the height is wrong for square



## Slide 75: LSP – Subtle example

- Okay, what about now?
- public class Rectangle
- {
- public virtual int Width { get; set; }
- public virtual int Height { get; set; }
- }
- public class Square : Rectangle
- {
- public override int Height
- {
- get { return base.Height; }
- set
- {
- base.Height = value;
- base.Width = value;
- }
- }
- public override int Width
- {
- get { return base.Width; }
- set
- {
- base.Width = value;
- base.Height = value;
- }
- }
- }

> **Notes:** What if the client does something like Area = rectangle.width * rectangle.height



## Slide 76: LSP – Subtle example

- This works fine until a Square is passed!
- public class AreaCalculator
- {
- private int CalculateArea(Rectangle rectangle)
- {
- return rectangle.Width*rectangle.Height;
- }
- public void ValidateArea(Rectangle rectangle)
- {
- rectangle.Height = 5;
- rectangle.Width = 4;
- if (CalculateArea(rectangle) != 20)
- {
- throw new Exception("Area should be 20!");
- }
- }
- }

> **Notes:** What if the client does something like Area = rectangle.width * rectangle.height



## Slide 77: LSP - Practicalities

- A model is only complete when it is validated against its users.
- Users of the model define the behavior
- Inheritance should be based on behavior
- Behavior defines the ISA relationship for objects
- OOD is about the behavior of objects
- LSP is at the heart of OCP
- If you break LSP, you cannot close your object to changes


## Slide 78: S.O.L.I.D. code

- Single responsibility principle
- Open closed principle
- Liskov substitution principle
- Dependency inversion principle
- Interface segregation principle


## Slide 79: Dependency Inversion Principle (DIP)

- A corollary to this is that abstractions should not depend on details, details should depend on abstractions.
- These principles turn the typical dependencies in a layered application upside down
- High-level modules should not depend on low-level modules.
- Both should depend on abstractions.


## Slide 80: DIP - Layering

- A typical layered application
- High level is dependent on low level

> **Notes:** Common principle that classes are layered, from high level policy classes that define the application to Utility classes that perform specific low level actions



## Slide 81: DIP – Inversion

- Using OCP to create abstractions yields
- High level no longer depends on low level
- Where should the abstractions be defined?


## Slide 82: DIP – Example #2



## Slide 83: DIP – Example #2…



## Slide 84: DIP – Abstraction ownership

- The ownership has been inverted as well
- “Hollywood principle”
- Don’t call us, we’ll call you
- Client can be reused in other situations
- The interface will only change when the client needs it to change
- More robust, flexible and resistant to change
- Many clients and one server
- Abstraction should be defined in a separate package


## Slide 85: DIP – Depend on abstractions

- Do not depend on concrete classes
- All relationships in a program should finish with an abstract class or interface
- Conventions that are driven by these principles
- No variable should hold a reference to a concrete class
- No class should derive from a concrete class
- No method should override an implemented method of any of its base classes
- Pragmatically
- If a concrete class is not going to change much, and there will be no derivatives, depending on the class is probably okay


## Slide 86: S.O.L.I.D. code

- Single responsibility principle
- Open closed principle
- Liskov substitution principle
- Dependency inversion principle
- Interface segregation principle


## Slide 87: Interface Segregation Principle (ISP)

- Interfaces that contain methods that only a subset of clients use are considered to be “Fat”
- Dependency forces go both ways
- Server changes change clients
- Client changes change servers
- If clients do not use all the methods of a server, they are needlessly forced to change when other clients force a change
- This can be clarified with an example
- Classes should not be forced to depend on methods
- they do not use.


## Slide 88: ISP - Example

- CDF “Fat” interface example
- Originally had MenuStrip
- Then we added ToolStrip
- Then we added StatusBar
- By the time we got to RibbonBar we’d woken up!
- public interface IDocumentWindow
- {
- bool AllowClose();
- DockingWindow[] DockingWindows { get; }
- string Moniker { get; }
- StatusStrip StatusBar { get; }
- ToolStrip[] ToolBars { get; }
- System.Collections.Generic.IDictionary<String, Object> Context { get; set;}
- string DocumentWindowType { get; }
- string OwnerName { get; set;}
- MenuStrip MenuBar { get; }
- }


## Slide 89: Bonus Principles Acronyms

- Don’t Repeat Yourself (DRY)
- Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
- Simple in theory, hard in practice
- Strive hard to avoid duplication
- Code and Algorithms can be duplicated
- You Ain’t Going to Need It (YAGNI)
- OCP can be taken too far
- Adding things you might need:
- Limits your choices later
- Adds code that must be maintained
- Makes it harder to maintain
- “Always implement things when you actually need them, never when you just foresee that you need them”


## Slide 90: Where to Next?

- Review the principles to understand them
- Read your code
- Read others code
- Analyze the code from these points of view
- Think about how you might change the code
- Talk with others about the principles
- It’s up to you


## Slide 91: Questions and Answers



## Slide 92: References

- “Principles and Patterns” Robert Martin 2000
- http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf
- Agile Principles and Patterns in C#
- Robert C Martin & Micah Martin
- http://www.amazon.com/Principles-Patterns-Practices-Robert-Martin/dp/0131857258/ref=sr_1_9?ie=UTF8&s=books&qid=1245321827&sr=1-9
- Clean Code
- Robert C Martin
- http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&s=books&qid=1245321733&sr=8-1
- Object Mentor
- http://www.objectmentor.com/resources/publishedArticles.html
- Refactoring – Improving the design of existing code
- Martin Fowler
- http://www.amazon.com/exec/obidos/ASIN/0201485672


## Slide 93: Design Pattern and Refactoring

- Resource:
- Design Patterns: Elements of Reusable Object-Oriented Software By Erich Gamma, Richard Helm, Ralph Johnson, John M. Vlissides


## Slide 94: Some Design Patterns

- Factory Method
- Builder Pattern
- Strategy
- Decorator
- State
- Composite
- Command
- Template Method
- Observer
- Adapter
- Visitor


## Slide 95: What is a design pattern

- a standard solution to a common programming problem
- a technique for making code more flexible by making it meet certain criteria
- a design or implementation structure that achieves a particular purpose
- a high-level programming idiom
- shorthand for describing certain aspects of program organization
- connections among program components
- the shape of a heap snapshot or object model


## Slide 96: What is a design pattern

- Describes recurring design structure
- – names, abstracts from concrete designs
- – identifies classes, collaborations, responsibilities
- applicability, trade-offs, consequences


## Slide 97: What is a design pattern

- Design patterns represent solutions to problems that arise when developing software within a particular context
- “Patterns == problem/solution pairs in a context”
- Patterns capture the static and dynamic structure and collaboration among key participants in software designs
- Especially good for describing how and why to resolve nonfunctional issues
- Patterns facilitate reuse of successful software architectures and designs.


## Slide 98: Applications

- Wide variety of application domains: drawing editors, banking, CAD, CAE, cellular network management, telecomm switches, program visualization
- Wide variety of technical areas:  user interface, communications, persistent objects, O/S kernels, distributed systems


## Slide 99: Definition

- “Each pattern describes a problem which occurs over and over again in our environment and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it in the same way twice”
- Christopher Alexander, A Pattern Language, 1977


## Slide 100: Design Patterns

- A pattern has 4 essential elements:
- Pattern name
- Problem
- Solution
- Consequences


## Slide 101: How a Pattern is Defined (GoF form)

- Name - good name
- Intent- what does it do
- Also Known As
- Motivation - a scenario
- Applicability - when to use
- Structure- UML
- Participants - classes
- Collaborations - how they work together
- Consequences - trade offs
- Implementation- hints on implementation
- Sample Code
- Known Uses
- Related Patterns


## Slide 102: Classes of Design Patterns

- Creational patterns:
- Deal with initializing and configuring classes and objects
- Structural patterns:
- Deal with decoupling interface and implementation of classes and objects
- Composition of classes or objects
- Behavioral patterns:
- Deal with dynamic interactions among societies of classes and objects
- How they distribute responsibility


## Slide 103: Another view of classification

- Standard patterns used in refactoring
- Creation—creation methods, factory, builder, and singleton
- Simplification—composition, strategy, decorator, state, composite, command
- Generalization—template, composite, observer, adapter, interpreter
- Protection—singleton, null object, generalization
- Accumulation (visitor) patterns—will be skipped.
- Miscellany—utilities


## Slide 104

- Factory Method


## Slide 105: Factory Method Pattern

- Synopsis: Define an interface for creating an object, but let subclasses decide which class to instantiate.
- Factory Method lets a class defer instantiation to subclasses
- Context: Example is that of a GUI framework. The generic Application class will have a method createDocument to create a generic document. A specific use of the framework for, say, word-processing GUI would subclass the generic Application class and override the  createDocument method to generate word-processing documents.


## Slide 106: Factory Method Pattern

- Forces: Use the Factory Method pattern when:
- a class can’t anticipate the class of objects it must create
- a class wants its subclasses to specify the objects it creates
- the set of classes to be generated may be dynamic


## Slide 107: Factory Method Pattern

- Solution: Use a factory method to create the instances:
- Product (e.g. Document) – defines the interface of objects the factory method creates
- ConcreteProduct (e.g. MyDocument) – implements the Product interface
- Creator (e.g. Application) – declares the factory method which returns an object of type Product (possibly with a default implementation); may call the factory method to create a Produce object
- ConcreteCreator (e.g. MyApplication) – overrides the factory method to return an instance of ConcreteProduct


## Slide 108: Factory Method Pattern



## Slide 109: Factory Method Pattern

- Factory method – class creational
- Consequences:
- It eliminates the need to bind application-specific classes into your code. The code only deals with the Product interface and therefore can work with any user-defined ConcreteProduct classes.
- A client will have to subclass the Creator class just to create a particular ConcreteProduct instance.


## Slide 110: Factory Method Pattern

- Provides hooks for subclasses to provide extended versions of objects
- Connects parallel class hierarchies, e.g. Application – Document vs MyApplication – MyDocument
- The set of product classes that can be instantiated may change dynamically


## Slide 111: Factory Method Pattern

- Applicability : Use when
- a class cannot anticipate the class of objects it must create
- a class wants its subclasses to specify the objects it creates
- classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass to delegate.


## Slide 112

- Builder Pattern


## Slide 113: Builder

- Separate the construction of a complex object from its representation so that the same construction process can create different representations.


## Slide 114: Builder



## Slide 115: Builder Structure…



## Slide 116: Builder



## Slide 117: Builder Discussion

- Sometimes creational patterns are complementory: Builder can use one of the other patterns to implement which components get built. Abstract Factory, Builder, and Prototype can use Singleton in their implementations.
- Builder focuses on constructing a complex object step by step. Abstract Factory emphasizes a family of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory is concerned, the product gets returned immediately.
- Builder is to creation as Strategy is to algorithm.


## Slide 118: Builder Discussion

- Builder often builds a Composite.
- Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.


## Slide 119: Builder Consequences

- It lets you vary a product's internal representation
- It isolates code for construction and representation
- It gives you finer control over the construction process


## Slide 120

- Strategy


## Slide 121: Strategy – Behavioral

- Consider a system that needs to break a stream of text into lines. There are many algorithms for doing this – hardwiring a particular algorithm may be undesirable:
- clients will be more complex if they include the algorithm – different algorithms will be appropriate at different times or in different contexts
- it is difficult to add new algorithms
- The solution is to define classes which encapsulate different line-breaking algorithms
- the so-called Strategy pattern


## Slide 122: Strategy

- Synopsis: Define a family of algorithms, encapsulate each one,and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it
- Context: In a document editor you may want to vary the choice of line-breaking strategies, possibly on-the-fly
- Forces: Use the Strategy pattern when:
- many related classes differ only in their behavior, in which case the Strategy provides a way of configuring a class with one of many behaviors
- you need different variants of an algorithm
- an algorithm uses data that clients shouldn’t know about –
- Strategy avoids exposing complex, algorithm-specific data structures
- a class defines multiple alternative behaviors


## Slide 123: Strategy

- Solution: Encapsulate the algorithm in an object:
- – Strategy (e.g. Compositor) – declares an interface common to all supported algorithms.
- –Context uses this interface to call the algorithms defined by a ConcreteStrategy
- – ConcreteStrategy (e.g. SimpleCompositor) – implements the algorithm using the Strategy interface
- – Context (e.g. Composition) – is configured with a ConcreteStrategy object, and may define an interface that lets Strategy access its data.


## Slide 124: Strategy



## Slide 125: Strategy

- Consequences: The Strategy pattern has the following benefits and drawbacks:
- families of related algorithms can be defined using a class hierarchy, thus allowing common functionality of the algorithms to be factored out
- an alternative to subclassing for providing a variety of algorithms or behaviours. Subclassing for modifying behaviour hard-wires the behaviour into Context. Further, subclassing does not support dynamic modification of the algorithm
- Strategies can eliminate conditional statements used to select the particular algorithm
- Strategies provide a choice of implementations, depending for example, on different time and space tradeoffs


## Slide 126

- Decorator


## Slide 127: Decorator - Intent

- Attach additional responsibility to an object dynamically.  Decorators provide a flexible alternative to sub-classing for extending functionality.


## Slide 128: Synopsis

- Provides a dynamic and lightweight substitute for subclassing
- Each object is only decorated with the functionality it needs
- Takes full advantage of the class hierarchy and inheritance


## Slide 129: Context

- Many possible uses
- X windows uses Decorators to apply decorations to windows, hence the name
- Generally used when the programmer wants many instances of the same parent class with many different behaviors, but without creating many subclasses.


## Slide 130: Forces

- Suppose you have a user interface toolkit and you wish to make a border or scrolling feature available to clients without defining new subclasses of all existing classes. The client "attaches" the border or scrolling responsibility to only those objects requiring these capabilities.
- Widget*  aWidget = new BorderDecorator(
- new HorScrollDecorator(
- new VerScrollDecorator(
- new TextWidget( 80, 24 ))));
- aWidget->draw();


## Slide 131: Forces

- Allows transparent addition of functionality.
- Decorators are decoupled from base class and each other.
- Decorators can be added or removed dynamically and easily.


## Slide 132: Solution

- Enclose the base class in a decorator class that maintains the same interface
- Totally transparent to program using the Decorators and to other decorators


## Slide 133: Consequences

- Good Things
- Allows the use of multiple decorators, including the same one multiple times
- Totally decoupled. Each decorator is only aware of the thing it is decorating, and the base class is not aware that it has been decorated.
- Bad things
- Can be difficult to remove specific decorators dynamically
- Decorator has the same interface as base class, but is not the same object, which can lead to problems if, for example, the address of the base class is needed


## Slide 134: Implementation

- If the object needs to call itself or pass itself, it may need to pass its decorators as well. If this is the case, it must be made aware of them.
- Changing the middle decorator of a pile can be like removing the middle layer of noodles from lasagna. It’s possible, but easier said than done and quite messy.


## Slide 135: Related patterns

- Adapter changes interface
- Proxy duplicates interface
- Decorator enhances interface


## Slide 136

- State


## Slide 137: State

- Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
- Any methods whose behaviors depend on the state of the object are simply delegated on in to the state, and handled there. Thus you will see the same methods in the context as in the states. Since the states are separate objects from the context, all the properties of the context need to have accessor methods that are at least package visible.
- The "Context" object needs to add a "set" accessor method so the states can modify which state is the active state. This method would be package visible so as to encapsulate the behavior away from the sight of the user.


## Slide 138: Example



## Slide 139: Structure



## Slide 140: Consequences

- It localizes state-specific behavior and partitions behavior for different states
- It makes state transitions explicit
- State objects can be shared


## Slide 141

- Composite


## Slide 142: Composite Pattern

- Compose objects into tree structures to represent part whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.


## Slide 143: Composite Example



## Slide 144: Composite Example



## Slide 145: Composite Structure



## Slide 146

- Command


## Slide 147: Command Pattern…

- Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.


## Slide 148: Command Example



## Slide 149: Command Example



## Slide 150: Command Structure



## Slide 151: Command Structure



## Slide 152: Command Consequences

- Command decouples the object that invokes the operation from the one that knows how to perform it.
- Commands are first-class objects. They can be manipulated and extended like any other object.
- It's easy to add new Commands, because you don't have to change existing classes.


## Slide 153: Applying Composite on Command



## Slide 154

- Template Method


## Slide 155: Template Pattern - Intent

- Define the skeleton of an algorithm in an operation, deferring some steps to client subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. [GoF, p325]
- Base class declares algorithm “placeholders”, and derived classes implement the placeholders.


## Slide 156: Problem

- Two different components have significant similarities, but demonstrate no reuse of common interface or implementation. If a change common to both components becomes necessary, duplicate effort must be expended.


## Slide 157: Template Method – structure



## Slide 158: Example

- The Template Method defines a skeleton of an algorithm in an operation, and defers some steps to subclasses. Home builders use the Template Method when developing a new subdivision. A typical subdivision consists of a limited number of floor plans with different variations available for each. Within a floor plan, the foundation, framing, plumbing, and wiring will be identical for each house. Variation is introduced in the later stages of construction to produce a wider variety of models. [Michael Duell, "Non-software examples of software design patterns", Object Magazine, Jul 97, p54]


## Slide 159

- Observer


## Slide 160: Observer - Behavioral

- One-to-many dependency between objects: change of one object will automatically notify observers


## Slide 161: Observer: Applicability

- A change to one object requires changing an unknown set of others
- Object should be able to notify others that may not be known at the beginning


## Slide 162: Observer: Structure



## Slide 163: Observer: Consequences

- Abstract coupling between subject and observer
- Support for broadcast communication
- Hard to maintain


## Slide 164: Observer: Consequences

- Loose coupling in communication
- Observers decide what happens
- Dynamic change of communication
- Anonymous communication
- Multi-cast and broadcast communication


## Slide 165

- Adapter


## Slide 166: Adapter Pattern - Structural

- Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.


## Slide 167: The Adapter (Wrapper) Pattern

- Context: you are building an inheritance hierarchy and want to incorporate it into an existing class
- The reused class is also often already part of its own inheritance hierarchy
- Problem: how to obtain the power of polymorphism when reusing a class whose methods have the same function, but NOT the same signature as the other methods in the hierarchy?
- Forces: you do not have access to multiple inheritance or you do not want to use it


## Slide 168: More on Adapter

- In fact, there are two variants of the adapter pattern:
- Class adapter, which uses multiple inheritance to adapt one interface to another
- Object adapter, which uses single inheritance and delegation


## Slide 169: Adapter pattern

- Delegation used to bind an Adapter and an Adaptee
- Interface inheritance used to specify the interface of the Adapter class


## Slide 170: Adapter Example



## Slide 171: Adapter Structure



## Slide 172

- Visitor


## Slide 173: Visitor Pattern - Behavioral

- Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.


## Slide 174: Visitor Pattern

- Parse Trees
- • If an expression has a correct syntax according to a grammar then we can make a parse tree for it.


## Slide 175: Visitor Pattern

- Visitor pattern works for a tree data structure with many different types of nodes.
- Compilers and other programs (ex: pretty printers) do lots of operations by traversing the parse tree – visiting every node.


## Slide 176: Visitor example



## Slide 177: Visitor example



## Slide 178: Visitor applicability

- many distinct and unrelated operations need to be performed on objects in an object structure, and you want to avoid "polluting" their classes with these operations


## Slide 179: Visitor Structure



## Slide 180: Visitor Structure



## Slide 181: Pros and Cons

- Pros
- Visitor makes adding new operations easy
- Visitor gathers related operations and separates unrelated ones
- Ability to visit across hierarchies
- Ability to accumulate states
- Cons
- Adding concrete element classes is hard
- slots encapsulation


## Slide 182: Visitor Consequences

- Visitor makes adding new operations easy
- A visitor gathers related operations and separates unrelated ones
- Adding new Concrete Element classes is hard
- Visiting across class hierarchies
- Accumulating state.
- sloting encapsulation


## Slide 183



## Slide 184: Refactoring

- What is refactoring?
- Refactoring is a "behavior-preserving transformation"
- "a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior"  by Martin Fowler
- Resource:
- Kerievsky, J., 2005, Refactoring to Patterns, Addison-Wesley.


## Slide 185: Why Refactor?

- Make it easier to add new code.
- Improve the design of existing code.
- Improve the design of existing code.
- Clean up messes in the code
- Simplify the code
- Better readability and understandability
- Find bugs
- Reduce debugging time
- Build in learning we do about the application
- Redoing things is fundamental to every creative process


## Slide 186

- 186
- Code Smells
- Indicators that something may be wrong in the code
- Can occur both in production code and test code


## Slide 187: Code Smells

- Duplicated code
- Long method
- Large class
- Long parameter list
- Message chain
- Feature envy
- Switch statements
- Data class
- Speculative generality
- Temporary field
- Refused bequest
- Middle Man
- Parallel Inheritance Hierarchies
- Primitive Obsession
- Shotgun Surgery
- Alternative Classes with Different Interfaces
- Comments
- Data Clumps
- Divergent Change
- Feature Envy
- Inappropriate Intimacy
- Incomplete Library Class
- Lazy Class


## Slide 188: Duplicate code

- Duplicate methods in subclasses
- Move to superclass, possibly create superclass
- Duplicate expressions in same class
- Extract method
- Duplicate expressions in different classes
- Extract method, move to common component


## Slide 189: Long method

- Too Big to fit on this page
- Can’t think of whole thing at once
- Extract function
- Loop body
- Places where there is (or should be) a comment


## Slide 190: Large class

- More than a couple dozen methods, or half a dozen variables
- Split into component classes
- Create super class
- If using switch statement, split into subclasses
- Refactorings
- Extract Class
- Extract Subclass
- Extract Interface
- Replace Data Value with Object


## Slide 191: Lazy Class

- A class that isn’t doing enough work to justify its maintenance
- Refactorings
- Inline Class
- Collapse Hierarchy


## Slide 192: Long parameter list

- Many parameters passed into a method
- Only worthwhile if there are several methods with same parameter list, and they call each other
- Refactorings
- Replace Parameter with Method
- Introduce Parameter Object
- Preserve Whole Object


## Slide 193: Message chain

- One object asks another object for something, which causes the asked object to ask another object, and so on
- Refactorings
- Hide Delegate
- Example:
- customer.getAddress().getState()
- window.getBoundingbox().getOrigin().getX()
- Replace with shorter calls:
- customer.getState()
- window.leftBoundary()


## Slide 194: Feature envy

- A method making more use of another class than the one it is in
- Code wishes it were in another class; move it
- Example:
- From:
- teacher.getClasses().add(thisClass);
- teacher.setClassLoad(teacher.getClassLoad()+1);
- To:
- teacher.addClass(thisClass);
- Refactorings
- Move Method
- Move Field
- Extract Method


## Slide 195: Data class

- Class has no methods except for getter and setters
- What to do:
- Look for missing methods (feature envy?) and move them to the class
- Merge with another class
- Refactorings
- Move Method
- Encapsulate Field
- Encapsulate Collection


## Slide 196: Switch statement

- Using a switch statement where polymorphism would work better
- Replace switch (or nested if) with a method call
- Make subclass for each case
- Use dynamic dispatch/polymorphism
- Special case: instanceof for “switch”
- Refactorings
- Replace Conditional with Polymorphism
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy
- Replace Parameter with Explicit Methods
- Introduce Null Object


## Slide 197: Alternative Classes with Different Interfaces

- Methods that do the same thing but have different signatures
- Refactorings
- Rename Method
- Move Method


## Slide 198: Temporary field

- Instance variable is only used during part of the lifetime of an object
- For example, it is only used while the object is initialized
- Move variable into another object (perhaps a new class)


## Slide 199: Refused bequest

- A is a subclass of B
- A
- Overrides inherited methods of B
- Does not use some variables of B
- Does not use some methods of B
- Give A and B a common superclass and move common code into it


## Slide 200: List of Refactorings

- Add Parameter
- Change Bidirectional Association to Unidirectional
- Change Reference to Value
- Change Unidirectional Association to Bidirectional
- Change Value to Reference
- Collapse Hierarchy
- Consolidate Conditional Expression
- Consolidate Duplicate Conditional Fragments
- Convert Dynamic to Static Construction by Gerard M. Davison
- Convert Static to Dynamic Construction by Gerard M. Davison
- Decompose Conditional
- Duplicate Observed Data
- Eliminate Inter-Entity Bean Communication (Link only)
- Encapsulate Collection
- Encapsulate Downcast
- Encapsulate Field
- Extract Class
- Extract Interface
- Extract Method
- Extract Package by Gerard M. Davison
- Extract Subclass
- Extract Superclass
- Form Template Method
- Hide Delegate
- Hide Method
- Hide presentation tier-specific details from the business tier (Link only)
- Inline Class
- Inline Method
- Inline Temp
- Introduce A Controller (Link only)
- Introduce Assertion
- Introduce Business Delegate (Link only)
- Introduce Explaining Variable
- Introduce Foreign Method
- Introduce Local Extension
- Introduce Null Object
- Introduce Parameter Object
- Introduce Synchronizer Token (Link only)
- Localize Disparate Logic (Link only)
- Merge Session Beans (Link only)
- Move Business Logic to Session (Link only)
- Move Class by Gerard M. Davison
- Move Field
- Move Method
- Parameterize Method
- Preserve Whole Object
- Pull Up Constructor Body
- Pull Up Field
- Pull Up Method
- http://www.refactoring.com/catalog/index.html


## Slide 201: List of Refactorings (cont)

- Push Down Field
- Push Down Method
- Reduce Scope of Variable by Mats Henricson
- Refactor Architecture by Tiers (Link only)
- Remove Assignments to Parameters
- Remove Control Flag
- Remove Double Negative by Ashley Frieze and Martin Fowler
- Remove Middle Man
- Remove Parameter
- Remove Setting Method
- Rename Method
- Replace Array with Object
- Replace Assignment with Initialization by Mats Henricson
- Replace Conditional with Polymorphism
- Replace Conditional with Visitor by Ivan Mitrovic
- Replace Constructor with Factory Method
- Replace Data Value with Object
- Replace Delegation with Inheritance
- Replace Error Code with Exception
- Replace Exception with Test
- Replace Inheritance with Delegation
- Replace Iteration with Recursion by Dave Whipp
- Replace Magic Number with Symbolic Constant
- Replace Method with Method Object
- Replace Nested Conditional with Guard Clauses
- Replace Parameter with Explicit Methods
- Replace Parameter with Method
- Replace Record with Data Class
- Replace Recursion with Iteration by Ivan Mitrovic
- Replace Static Variable with Parameter by Marian Vittek
- Replace Subclass with Fields
- Replace Temp with Query
- Replace Type Code with Class
- Replace Type Code with State/Strategy
- Replace Type Code with Subclasses
- Reverse Conditional by Bill Murphy and Martin Fowler
- Self Encapsulate Field
- Separate Data Access Code (Link only)
- Separate Query from Modifier
- Split Loop by Martin Fowler
- Split Temporary Variable
- Substitute Algorithm
- Use a Connection Pool (Link only)
- Wrap entities with session (Link only)
- http://www.refactoring.com/catalog/index.html


## Slide 202

- 202
- Refactoring to Patterns
- Replace Ctors with Creation methods, chain Ctors
- Encapsulate Classes with Factory
- Introduce Polymorphic Creation with Factory Method
- Replace Conditional Logic with Strategy
- Form Template Method
- Compose Method
- Replace Implicit Tree with Composite
- Encapsulate Composite with Builder
- Move Accumulation to Collecting Parameter
- Extract Composite, Replace one/many with Composite.
- Replace Conditional Dispatcher with Command
- Extract Adapter, Unify Interfaces with Adapter
- Replace Type Code with Class
- Replace State-Altering Conditionals with State
- Introduce Null Object
- Inline Singleton, Limit Instantiation with Singleton
- Replace Hard-Coded Notifications with Observer
- Move Embellishment to Decorator, Unify Interfaces, Extract Parameter
- Move Creation Knowledge to Factory
- Move Accumulation to Visitor
- Replace Implicit Language with Interpreter
- Out of ~140 techniques from previous slide


## Slide 203: Extract Class

- You have one class doing work that should be done by two.
- Create a new class and move the relevant fields and methods from the old class into the new class.


## Slide 204: Extract Subclass

- A class has features that are used only in some instances.
- Create a subclass for that subset of features.


## Slide 205: Extract method

- You have a code fragment that can be grouped together.
- Turn the fragment into a method whose name explains the purpose of the method.
- void printOwing() {
- printBanner(); //print details
- System.out.println ("name: " + _name);
- System.out.println ("amount " + getOutstanding());
- }
- void printOwing() {
- printBanner();
- printDetails(getOutstanding());
- }
- void printDetails (double outstanding) {
- System.out.println ("name: " + _name);
- System.out.println ("amount " + outstanding);
- }


## Slide 206: Extract Adapter

- Extract Adapter:
- One Class adapts
- multiple versions of component, library,
- API or other Entity.
- Solution:
- Extract an Adapter for
- a single version of  the component , library, API
- or other Entity.


## Slide 207: The Template Method

- The Template Method:
- Template Methods lead to an inverted control structure
- A superclass calls methods in its subclass
- Template methods are so fundamental that they can be found in almost every abstract class
- Template Method uses inheritance
- A similar pattern, Strategy Pattern, uses delegation rather than inheritance


## Slide 208: The Template Method

- Example : Big fish and little fish
- The scenario: “big fish” and “little fish” move around in an “ocean”
- Fish move about randomly
- A big fish can move to where a little fish is (and eat it)
- A little fish will not move to where a big fish is


## Slide 209: The Template Method

- General outline of the method:
- public void move() {    choose a random direction;          // same for both    find the location in that direction; // same for both    check if it’s ok to move there;       // different    if it’s ok, make the move;             // same for both}
- Solution:
- Extract the check on whether it’s ok to move
- In the Fish class, put the actual (template) move() method
- Create an abstract okToMove() method in the Fish class
- Implement okToMove() in each subclass


## Slide 210: The Template Method

- Note how this works: When a BigFish tries to move, it uses the move() method in Fish
- But the move() method in Fish uses the okToMove(locn) method in BigFish
- And similarly for LittleFish


## Slide 211: Encapsulates Classes with Factory

- Encapsulates Classes with Factory:
- Clients directly instantiate classes that reside in one package and implement a common interface.
- Solution:
- Make the class constructors non-public
- and let clients creates instances of them using a factory.


## Slide 212: Encapsulate Composite with Builder

- Encapsulate Composite with Builder:
- Building a composite is repititive , complicated or error-prone.
- Solution:
- Simplify the build by letting the Builder handles the details.


## Slide 213: Embellishment to Decorator

- Embellishment to Decorator:
- Code Provides an embellishment to a class‘  core responsibility.
- Solution:
- Move the embellishment code to a Decorator.


## Slide 214: Replace Conditional Logic with Stratergy

- Replace Conditional Logic with Stratergy:
- conditional logic in a method controls which of several variants of a calculation are executed.
- Solution:
- create a Stratergy for each variant and make the method delegate the caliculation to a single stratergy.


## Slide 215: Replace Hard-Coded Notifications with Observer

- Replace Hard-Coded Notifications with Observer:
- Subclasses are hardcoded to notify a single instance of another class.
- Solution:
- Remove the subclasses by making their superclass capable of notifying  one or more instances of any classes that implement a observable interface.


## Slide 216: Summary

- Patterns describe common ways of doing things. They are collected by people who spot repeating themes in designs.
- We should refactor any time we detect a “bad smell” in the code. Refactoring  makes code easier to understand, maintain and modify.
- Various Refactoring techniques to the patterns can be applied to the real-world problems depending up on the application criteria and usage of the system. (For e.g.: Observer ,Strategy and Template Patterns, etc. are most commonly used).


## Slide 217: Development Tools Support – Refactoring Automated

- Refactor! For c++
- http://www-106.ibm.com/developerworks/java/library/os-ecref/?ca=dgr-jw01os-ecref


## Slide 218

- Exercise
- Is the coupling loose or tight?
- How many references are there?
- Are all objects created via interfaces or the concrete class directly?
- Is external object creation scattered throughout the class (making automated unit testing difficult) or is it all done in the constructor (making dependency injection and therefore AUT easier)?
- Is the internal cohesion low or high?
- Do the names of all the member variables and methods seem related to the name of the class?
- Is the namespace correct and the class/function names themselves logically correct?  Are there specific names used when the class/function is quite generic or conversely is a generic name used when class/function is quite specific?
- Is the class or its method’s too big?
- Is there repetition?
- Is there consistent exception handling?
- Are there automated unit tests?
- List done code smells in your projects and identify the refactoring techniques for fix


## Slide 219: For More Information

- Book:
- “Refactoring – Improving the Design of Existing Code”, Martin Fowler,
- Website:
- http://www.refactoring.com/
- Others:
- Refactoring to Patterns - http://www.industriallogic.com/xp/refactoring/


## Slide 220

