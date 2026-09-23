# 23rd April 2014 - Java Programming - Answers

> Converted from `23rd April 2014 - Java Programming - Answers.docx`


1. Answer: Option B


Explanation:


All the words in option B are among the 49 Java keywords. Although goto reserved as a keyword in Java, goto is not used and has no function.


Option A is wrong because the keyword for the primitive int starts with a lowercase i.


Option C is wrong because "virtual" is a keyword in C++, but not Java.


Option D is wrong because "constant" is not a keyword. Constants in Java are marked static and final.


Option E is wrong because "include" is a keyword in C, but not in Java.


2. Answer: Option D


Explanation:


The only legal array declaration and assignment statement is Option D


Option A is wrong because it initializes an int array with String literals.


Option B is wrong because it use something other than curly braces for the initialization.


Option C is wrong because it provides initial values for only one dimension, although the declared array is a two-dimensional array.


3. Answer: Option A


Explanation:


interface is a valid keyword.


Option B is wrong because although "String" is a class type in Java, "string" is not a keyword.


Option C is wrong because "Float" is a class type. The keyword for the Java primitive is float.


Option D is wrong because "unsigned" is a keyword in C/C++ but not in Java.


4. Answer: Option C


Explanation:


A boolean can only be assigned the literal true or false.


5. Answer: Option D


Explanation:


A char is really a 16-bit integer behind the scenes, so it supports 216 (from 0 to 65535) values.


6. Answer: Option C


Explanation:


Option C is correct. The output is "ELSE". Only when a is false do the output lines after 11 get some chance of executing.


Option A is wrong. The output is "A". When a is true, irrespective of the value of b, only the line 5 output will be executed. The condition at line 7 will never be evaluated (when a is true it will always be trapped by the line 12 condition) therefore the output will never be "A && B".


Option B is wrong. The output is "A". When a is true, irrespective of the value of b, only the line 5 output will be executed.


Option D is wrong. The output is "notB".


7. Answer: Option A


Explanation:


The compiler will complain because of incompatible types (line 4), the if expects a boolean but it gets an integer.


8. Answer: Option D


Explanation:


Using the integer 1 in the while statement, or any other looping or conditional construct for that matter, will result in a compiler error. This is old C Program syntax, not valid Java.


A, B and C are incorrect because line 1 is valid (Java is case sensitive so While is a valid class name). Line 8 is also valid because an equation may be placed in a String operation as shown.


9. Answer: Option B


Explanation:


Option B is correct because a static nested class is not tied to an instance of the enclosing class, and thus can't access the nonstatic members of the class (just as a static method can't access nonstatic members of a class).


Option A is incorrect because static nested classes do not need (and can't use) a reference to an instance of the enclosing class.


Option C is incorrect because static nested classes can declare and define nonstatic members.


Option D is wrong because it just is. There's no rule that says an inner or nested class has to extend anything.


10. Answer: Option A


Explanation:


MyInner is a static nested class, so it must be instantiated using the fully-scoped name of MyOuter.MyInner.


Option B is incorrect because it doesn't use the enclosing name in the new.


Option C is incorrect because it uses incorrect syntax. When you instantiate a nested class by invoking new on an instance of the enclosing class, you do not use the enclosing name. The difference between Option A and C is that Option C is calling new on an instance of the enclosing class rather than just new by itself.


Option D is incorrect because it doesn't use the enclosing class name in the variable declaration.


11. Answer: Option D


Explanation:


Option D is correct. Compilation fails because of an unreachable statement at line 14. It is a compile-time error if a statement cannot be executed because it is unreachable. The question is now, why is line 20 unreachable? If it is because of the assert then surely line 6 would also be unreachable. The answer must be something other than assert.


Examine the following:


A while statement can complete normally if and only if at least one of the following is true:

- The while statement is reachable and the condition expression is not a constant expression with value true.
- There is a reachable break statement that exits the while statement.

The while statement at line 11 is infinite and there is no break statement therefore line 14 is unreachable. You can test this with the following code:


12. Answer: Option A


Explanation:


Option A compiles without problem.


Option B gives error - non-static variable cannot be referenced from a static context.


Option C package ot does not exist.


Option D gives error - non-static variable cannot be referenced from a static context.


13. Answer: Option A


Explanation:


No answer description available for this question.


14. Answer: Option D


Explanation:


Compilation failed because static was an illegal start of expression - method variables do not have a modifier (they are always considered local).


15. Answer: Option A


Explanation:


If you put a finally block after a try and its associated catch blocks, then once execution enters the try block, the code in that finally block will definitely be executed except in the following circumstances:


An exception arising in the finally block itself.


The death of the thread.


The use of System.exit()


Turning off the power to the CPU.


I suppose the last three could be classified as VM shutdown.


16. Answer: Option B


Explanation:


Option B is correct. This works because it DOES throw an exception if an error occurs.


Option A is wrong. If you compile the code as given the compiler will complain:


"unreported exception must be caught or declared to be thrown" The class extends Exception so we are forced to test for exceptions.


Option C is wrong. The catch statement belongs in a method body not a method specification.


Option D is wrong. TestException is a subclass of Exception therefore the test method, in this example, must throw TestException or some other class further up the Exception tree. Throwing RuntimeException is just not on as this belongs in the java.lang.RuntimeException branch (it is not a superclass of TestException). The compiler complains with the same error as in A above.


17. Answer: Option B


Explanation:


Option B is correct because in the first line of main we're constructing an instance of an anonymous inner class extending from MyThread. So the MyThread constructor runs and prints "MyThread". The next statement in main invokes start() on the new thread instance, which causes the overridden run() method (the run() method defined in the anonymous inner class) to be invoked, which prints "foo"


18. Answer: Option C


Explanation:


Option C is suitable to start a thread.


19. Answer: Option B


Explanation:


The Math.random() method returns a number greater than or equal to 0 and less than 1 . Since we can then be sure that the sum of that number and 2.5 will be greater than or equal to 2.5 and less than 3.5, we can be sure that Math.round() will round that number to 3. So Option B is the answer.


20. Answer: Option C


Explanation:


Arguments start at array element 0 so the fourth arguement must be 2 to produce the correct output.


21. Answer: Option B


Explanation:


Line 13 fails because == compares reference values, not object values. Line 15 succeeds because both String and primitive wrapper constructors resolve to the same value (except for the Character wrapper). Lines 17, 19, and 21 fail because the equals() method fails if the object classes being compared are different and not in the same tree hierarchy.


22. Answer: Option B


Explanation:


(1) and (2) are correct. The result range for random() is 0.0 to < 1.0; 1.0 is not in range.


23. Answer: Option C


Explanation:


The code will not compile because in line 7, the line will work only if we use (x==y) in the line. The == operator compares values to produce a boolean, whereas the = operator assigns a value to variables.


Option A, B, and D are incorrect because the code does not get as far as compiling. If we corrected this code, the output would be false.


24. Answer: Option B


Explanation:


Java only ever passes arguments to a method by value (i.e. a copy of the variable) and never by reference. Therefore the value of the variable i remains unchanged in the main method.


If you are clever you will spot that 16 is 4 multiplied by 2 twice, (4 * 2 * 2) = 16. If you had 16 left shifted by three bits then 16 * 2 * 2 * 2 = 128. If you had 128 right shifted by 2 bits then 128 / 2 / 2 = 32. Keeping these points in mind, you don't have to go converting to binary to do the left and right bit shifts.


25. Answer: Option B


Explanation:


Option B is correct. The compiler complains with the error "modifier private not allowed here". The class is created private and is being used by another class on line 19.


26. Answer: Option C


Explanation:


TreeSet assures no duplicate entries; also, when it is accessed it will return elements in natural order, which typically means alphabetical.


27. Answer: Option A


Explanation:


This code is an example of an anonymous inner class. They can be declared to extend another class or implement a single interface. Since they have no name you can not use the "new" keyword on them.


In this case the annoynous class is extending the Object class. Within the {} you place the methods you want for that class. After this class has been declared its methods can be used by that object in the usual way e.g. objectname.annoymousClassMethod()


28. Answer: Option D


Explanation:


No answer description available for this question.


29. Answer: Option D


Explanation:


Option D is correct. By a process of elimination.


Option A is wrong. The variable d is a member of the Test class and is never directly set to null.


Option B is wrong. A copy of the variable d is set to null and not the actual variable d.


Option C is wrong. The variable d exists outside the start() method (it is a class member). So, when the start() method finishes the variable d still holds a reference.


30. Answer: Option C


Explanation:


Option A is wrong. This simply copies the object reference into the array.


Option B is wrong. The reference o is set to null, but, oa[0] still maintains the reference to the Float object.


Option C is correct. The thread of execution will then not have access to the object.


31. Answer : Option C and E


Explaination :


Option C and E are correct syntax for static imports. Line 4 isn't making use of static imports, so the code will also compile with none of the imports.


A, B, D, and F are incorrect based on the above.


32. Answer : Option D


Explaination :


D is correct. A -classpath included with a java invocation overrides a system classpath.


When java is using any classpath, it reads the classpath from left to right, and uses the


first match it finds.


A, B, C, and E are incorrect based on the above.


33. Answer  : Option D


Explaintation :


D is correct. The thread MyThread will start and loop three times (from 0 to 2).


A is incorrect because the Thread class implements the Runnable interface; therefore,


in line 5, Thread can take an object of type Thread as an argument in the constructor


(this is NOT recommended). B and C are incorrect because the variable i in the for


loop starts with a value of 0 and ends with a value of 2. E is incorrect based on the above.


34. Answer : Option D


D is correct. 1 and 2 will be printed, but there will be no return from the wait call because


no other thread will notify the main thread, so 3 will never be printed. It's frozen at line 7.


A is incorrect; IllegalMonitorStateException is an unchecked exception. B and C


are incorrect; 3 will never be printed, since this program will wait forever. E is incorrect


because IllegalMonitorStateException will never be thrown because the wait()


is done on args within a block of code synchronized on args. F is incorrect because any


object can be used to synchronize on and this and static don't mix.


35. Answer : Option A


A is correct. Either of the two events will make the thread a candidate for running again.


B is incorrect because a waiting thread will not return to runnable when the lock is


released, unless a notification occurs. C is incorrect because the thread will become a


candidate immediately after notification. D is also incorrect because a thread will not come


out of a waiting pool just because a lock has been released.


36.


C, D, and E are correct statements.


A is incorrect. It is acceptable to use assertions to test the arguments of private methods.


B is incorrect. While assertion errors can be caught, Sun discourages you from doing so.


37


A, D, and F are correct. A is an example of the enhanced for loop. D and F are examples


of the basic for loop.


B is incorrect because its operands are swapped. C is incorrect because the enhanced


for must declare its first operand. E is incorrect syntax to declare two variables in a for


statement


38


E is correct. When an assert statement has two expressions, the second expression must


return a value. The only two-expression assert statement that doesn’t return a value is on


line 9.


A, B, C, D, and F are incorrect based on the above


39


D is correct. This is a ternary nested in a ternary with a little unboxing thrown in.


Both of the ternary expressions are false.


A, B, C, E, and F are incorrect based on the above


40


Answer C is correct.


A refers to encapsulation, B refers to coupling, and D refers to polymorphism


41


C is correct.


A is incorrect because classes implement interfaces, they don't extend them. B is incorrect


because interfaces only "inherit from" other interfaces. D is incorrect based on the


preceding rules.


42


B and D. B is true because often two dissimilar objects can return the same hashcode


value. D is true because if the hashCode() comparison returns ==, the two objects might


or might not be equal.


A, C, and E are incorrect. C is incorrect because the hashCode() method is very flexible


in its return values, and often two dissimilar objects can return the same hash code value.


A and E are a negation of the hashCode() and equals() contract.


43


E is correct. You can't put both Strings and ints into the same TreeSet. Without generics,


the compiler has no way of knowing what type is appropriate for this TreeSet, so it allows


everything to compile. At runtime, the TreeSet will try to sort the elements as they're


added, and when it tries to compare an Integer with a String it will throw a


ClassCastException. Note that although the before() method does not use generics,


it does use autoboxing. Watch out for code that uses some new features and some old


features mixed together.


A, B, C, and D are incorrect based on the above.
