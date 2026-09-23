# TExeter Quizpressions

> Converted from presentation `TExeter Quizpressions.pptx`


## Slide 1



## Slide 2: TExeter Quizpressions!



## Slide 3


> **Notes:** I ate some Pie



## Slide 4

- Here are some words translated from an artificial language.
- gorblflur means fan belt
- pixngorbl means ceiling fan
- arthtusl means tile roof
- Which word could mean "ceiling tile"?
- A. 	gorbltusl
- B. 	flurgorbl
- C. 	arthflur
- D. 	pixnarth

> **Notes:** pixnarth



## Slide 5: Solve this!

- public Object m()
- {
- Object o = new Float(3.14F);
- Object [] oa = new Object[l];
- oa[0] = o; /* Line 5 */
- o = null;  /* Line 6 */
- oa[0] = null; /* Line 7 */
- return o; /* Line 8 */
- }
- When is the Float object, created in line 3, eligible for garbage collection?
- just after line 5
- just after line 6
- just after line 7
- just after line 8

> **Notes:** Answer: Option C
Explanation:
Option A is wrong. This simply copies the object reference into the array.
Option B is wrong. The reference o is set to null, but, oa[0] still maintains the reference to the Float object.
Option C is correct. The thread of execution will then not have access to the object.



## Slide 6

- What is the order of colors in google logo!
- Blue, Green, Red, Yellow
- Yellow, Red, Blue, Green
- Red, Blue, Green Yellow
- Blue, Red, Yellow, Green

> **Notes:** Blue, Red, Yellow, Green



## Slide 7

- What will be the output of the program?
- public class Test
- {
- public int aMethod()
- {
- static int i = 0;
- i++;
- return i;
- }
- public static void main(String args[])
- {
- Test test = new Test();
- test.aMethod();
- int j = test.aMethod();
- System.out.println(j);
- }
- }
- 0
- 1
- 2
- Compilation fails.

> **Notes:** Answer: Option D
Explanation:
Compilation failed because static was an illegal start of expression - method variables do not have a modifier (they are always considered local).



## Slide 8

- What is the order of colors in OneGate logo!
- (Ordering: Top Right Left, Quadrilateral & Pie)
- Blue Green, Green Yellow, Yellow Blue
- Blue Yellow, Yellow Green, Green Blue
- Green Yellow, Yellow Blue, Blue Green
- Green Blue, Blue Yellow, Yellow Green
- Yellow Green, Green Blue, Blue Yellow

> **Notes:** Blue Green, Green Yellow, Yellow Blue



## Slide 9: SQL Select – Err! Something went bad

- A very common SQL issue is a case of accidental Cartesian joins. Not only does this give incorrect results, it can slow down queries to a large extent!!


## Slide 10

- What is a group of crows called?

> **Notes:** A Murder!



## Slide 11

- Look at this series: 36, 34, 30, 28, 24, ... What number should come next?
- A. 	20
- B. 	22
- C. 	23
- D. 	26

> **Notes:** 22



## Slide 12

- public class MyOuter
- {
- public static class MyInner
- {
- public static void foo() { }
- }
- }
- Which statement, if placed in a class other than MyOuter or MyInner, instantiates an instance of the nested class?
- MyOuter.MyInner m = new MyOuter.MyInner();
- MyOuter.MyInner mi = new MyInner();
- MyOuter m = new MyOuter(); MyOuter.MyInner mi = m.new MyOuter.MyInner();
- MyInner mi = new MyOuter.MyInner();

> **Notes:** Answer: Option A
Explanation:
MyInner is a static nested class, so it must be instantiated using the fully-scoped name of MyOuter.MyInner.
Option B is incorrect because it doesn't use the enclosing name in the new.
Option C is incorrect because it uses incorrect syntax. When you instantiate a nested class by invoking new on an instance of the enclosing class, you do not use the enclosing name. The difference between Option A and C is that Option C is calling new on an instance of the enclosing class rather than just new by itself.
Option D is incorrect because it doesn't use the enclosing class name in the variable declaration.



## Slide 13

- What is a group of unicorns known as?

> **Notes:** A Blessing!



## Slide 14: Observe and Arrange!



## Slide 15: Observe and Arrange!

- c
- d
- a
- b


## Slide 16: Observe and Arrange!

- c
- d
- a
- b


## Slide 17

- public class While
- {
- public void loop()
- {
- int x= 0;
- while ( 1 ) /* Line 6 */
- {
- System.out.print("x plus one is " + (x + 1)); /* Line 8 */
- }
- }
- }
- Which statement is true?
- There is a syntax error on line 1.
- There are syntax errors on lines 1 and 6.
- There are syntax errors on lines 1, 6, and 8.
- There is a syntax error on line 6.

> **Notes:** Answer: Option D
Explanation:
Using the integer 1 in the while statement, or any other looping or conditional construct for that matter, will result in a compiler error. This is old C Program syntax, not valid Java.
A, B and C are incorrect because line 1 is valid (Java is case sensitive so While is a valid class name). Line 8 is also valid because an equation may be placed in a String operation as shown.



## Slide 18

- Give us the sentence that contains every letter of the English Alphabet.

> **Notes:** The quick brown fox jumps over a lazy dog



## Slide 19

- The sum of ages of 5 children born at the intervals of 3 years each is 50 years. What is the age of the youngest child?
- 4 years
- 10 years
- 8 years
- None of the above

> **Notes:** 4 years



## Slide 20

- What will be the output of the program?
- public class Foo
- {
- public static void main(String[] args)
- {
- try
- {
- return;
- }
- finally
- {
- System.out.println( "Finally" );
- }
- }
- }
- Finally
- Compilation fails.
- The code runs with no output.
- An exception is thrown at runtime.

> **Notes:** Answer: Option A
Explanation:
If you put a finally block after a try and its associated catch blocks, then once execution enters the try block, the code in that finally block will definitely be executed except in the following circumstances:
An exception arising in the finally block itself.
The death of the thread.
The use of System.exit()
Turning off the power to the CPU.
I suppose the last three could be classified as VM shutdown.



## Slide 21: Java – What’s the risk??

- What’s wrong with the code?
- Consider a web form shown below which executes the below Java code on click:
- What happens when user types in ‘testuser or 1=1’?
- What happens when user types in ‘testuser; drop table users;’
- One way to prevent SQL injection is to use ‘prepared statements’.
- The other way to prevent it is to setup correct DB permissions, but that alone will not prevent situations like 1=1 conditions


## Slide 22: Observe and Arrange!



## Slide 23: Observe and Arrange!



## Slide 24: Observe and Arrange!



## Slide 25

- Which one of these lists contains only Java programming language keywords?
- class, if, void, long, Int, continue
- goto, instanceof, native, finally, default, throws
- try, virtual, throw, final, volatile, transient
- strictfp, constant, super, implements, do
- byte, break, assert, switch, include

> **Notes:** Answer: Option B
Explanation:
All the words in option B are among the 49 Java keywords. Although goto reserved as a keyword in Java, goto is not used and has no function.
Option A is wrong because the keyword for the primitive int starts with a lowercase i.
Option C is wrong because "virtual" is a keyword in C++, but not Java.
Option D is wrong because "constant" is not a keyword. Constants in Java are marked static and final.
Option E is wrong because "include" is a keyword in C, but not in Java.



## Slide 26: Do you know!

- Give us names of all versions of Apple OS, in chronological order!

> **Notes:** 5.1 Public Beta: "Kodiak"
5.2 Version 10.0: "Cheetah"
5.3 Version 10.1: "Puma"
5.4 Version 10.2: "Jaguar"
5.5 Version 10.3: "Panther"
5.6 Version 10.4: "Tiger"
5.7 Version 10.5: "Leopard"
5.8 Version 10.6: "Snow Leopard"
5.9 Version 10.7: "Lion"
5.10 Version 10.8: "Mountain Lion"
5.11 Version 10.9: "Mavericks"
5.12 Version 10.10: "Yosemite"



## Slide 27

- Which will legally declare, construct, and initialize an array?
- int [] myList = {"1", "2", "3"};
- int [] myList = (5, 8, 2);
- int myList [] [] = {4,9,7,0};
- int myList [] = {4, 3, 7};

> **Notes:** Answer: Option D
Explanation:
The only legal array declaration and assignment statement is Option D
Option A is wrong because it initializes an int array with String literals.
Option B is wrong because it use something other than curly braces for the initialization.
Option C is wrong because it provides initial values for only one dimension, although the declared array is a two-dimensional array.



## Slide 28: Do you know!

- Give us names of all versions of android, in chronological order!

> **Notes:** Cupcake, Donut, Éclair, Froyo, Gingerbread, Honeycomb, Ice-cream Sandwich, Kitkat, Lollipop



## Slide 29

- Which one is a valid declaration of a boolean?
- boolean b1 = 0;
- boolean b2 = 'false';
- boolean b3 = false;
- boolean b4 = Boolean.false();
- boolean b5 = no;

> **Notes:** Answer: Option C
Explanation:
A boolean can only be assigned the literal true or false.



## Slide 30

- Anthony and Cleopatra are lying dead on the floor of a villa in Egypt. Nearby is a broken bowl. There is no mark on either of their bodies and they were not poisoned. How did they die?

> **Notes:** They are both fishes!



## Slide 31: C# DB Select –What’s wrong?

- Majority of performance issues in an app are due to DB bottlenecks. So, always close connections before exit !!


## Slide 32

- A woman has incontrovertible proof in court that her husband was murdered by her sister. Both the woman and her sister are before the Judge. The judge declares, "This is the strangest case I've ever seen. Though it's a cut-and-dried case, this woman before me cannot be punished." How can this possibly be?

> **Notes:** The sister and the wife are conjoint (siamese) twins!



## Slide 33

- Cathy has twelve identical black socks and twelve identical white socks in her drawer. In complete darkness, and without looking, how many socks must she take from the drawer in order to be sure to get a pair that match?

> **Notes:** 3



## Slide 34: C# - Twice the time !!

- Is the for each loop really good for this scenario??
- Foreach loop dt.Rows will access all the rows in the datatable, and thereby will slow down performance. A better option may be to use FOR loop or implement query at DB level.


## Slide 35

- Two trains enter a tunnel 200 miles long, traveling at 100 mph at the same time from opposite directions. As soon as they enter the tunnel a supersonic bee flying at 1000 mph starts from one train and heads toward the other one. As soon as it reaches the other one it turns around and heads back toward the first, going back and forth between the trains until the trains collide in a fiery explosion in the middle of the tunnel. How far did the bee travel?

> **Notes:** This puzzle is a little tricky one. One’s thinking about solving this problem goes like this “ok, so i just need to sum up the distances that the bee travels…” but then you quickly realize that its a difficult (not impossible) summation.
The tunnel is 200 miles long. The trains meet in the middle traveling at 100 mph, so it takes them an hour to reach the middle. The bee is traveling 1000 mph for an hour (since its flying the whole time the trains are racing toward one another) – so basically the bee goes 1000 miles.

