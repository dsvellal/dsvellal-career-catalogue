# 23rd April 2014 - Java programming contest - Questionnaire

> Converted from `23rd April 2014 - Java programming contest - Questionnaire.docx`


1. Which one of these lists contains only Java programming language keywords?


class, if, void, long, Int, continue


goto, instanceof, native, finally, default, throws


try, virtual, throw, final, volatile, transient


strictfp, constant, super, implements, do


byte, break, assert, switch, include


2. Which will legally declare, construct, and initialize an array?


int [] myList = {"1", "2", "3"};


int [] myList = (5, 8, 2);


int myList [] [] = {4,9,7,0};


int myList [] = {4, 3, 7};


Compilation fails.


"odd" will always be output.


"even" will always be output.


"odd" will be output for odd values of x, and "even" for even values.


8.


public class While


{


public void loop()


{


int x= 0;


while ( 1 ) /* Line 6 */


{


System.out.print("x plus one is " + (x + 1)); /* Line 8 */


}


}


}


Which statement is true?


There is a syntax error on line 1.


There are syntax errors on lines 1 and 6.


There are syntax errors on lines 1, 6, and 8.


There is a syntax error on line 6.


9. Which statement is true about a static nested class?


You must have a reference to an instance of the enclosing class in order to instantiate it.


It does not have access to nonstatic members of the enclosing class.


It's variables and methods must be static.


It must extend the enclosing class.


10.


public class MyOuter


{


public static class MyInner


{


public static void foo() { }


}


}


Which statement, if placed in a class other than MyOuter or MyInner, instantiates an instance of the nested class?


MyOuter.MyInner m = new MyOuter.MyInner();


MyOuter.MyInner mi = new MyInner();


MyOuter m = new MyOuter(); MyOuter.MyInner mi = m.new MyOuter.MyInner();


MyInner mi = new MyOuter.MyInner();


11.


public class Test


{


public void foo()


{


assert false; /* Line 5 */


assert false; /* Line 6 */


}


public void bar()


{


while(true)


{


assert false; /* Line 12 */


}


assert false;  /* Line 14 */


}


}


What causes compilation to fail?


Line 5


Line 6


Line 12


Line 14


12.


public class Outer


{


public void someOuterMethod()


{


//Line 5


}


public class Inner { }


public static void main(String[] argv)


{


Outer ot = new Outer();


//Line 10


}


}


Which of the following code fragments inserted, will allow to compile?


new Inner(); //At line 5


new Inner(); //At line 10


new ot.Inner(); //At line 10


new Outer.Inner(); //At line 10


13. What will be the output of the program?


public class Test


{


public static void main(String args[])


{


class Foo


{


public int i = 3;


}


Object o = (Object)new Foo();


Foo foo = (Foo)o;


System.out.println("i = " + foo.i);


}


}


i = 3


Compilation fails.


i = 5


A ClassCastException will occur.


14. What will be the output of the program?


public class Test


{


public int aMethod()


{


static int i = 0;


i++;


return i;


}


public static void main(String args[])


{


Test test = new Test();


test.aMethod();


int j = test.aMethod();


System.out.println(j);


}


}


0


1


2


Compilation fails.


15. What will be the output of the program?


public class Foo


{


public static void main(String[] args)


{


try


{


return;


}


finally


{


System.out.println( "Finally" );


}


}


}


Finally


Compilation fails.


The code runs with no output.


An exception is thrown at runtime.


16.


public class ExceptionTest


{


class TestException extends Exception {}


public void runTest() throws TestException {}


public void test() /* Point X */


{


runTest();


}


}


At Point X on line 5, which code is necessary to make the code compile?


No code is necessary.


throws Exception


catch ( Exception e )


throws RuntimeException


17. What will be the output of the program?


class MyThread extends Thread


{


MyThread()


{


System.out.print(" MyThread");


}


public void run()


{


System.out.print(" bar");


}


public void run(String s)


{


System.out.println(" baz");


}


}


public class TestThreads


{


public static void main (String [] args)


{


Thread t = new MyThread()


{


public void run()


{


System.out.println(" foo");


}


};


t.start();


}


}


foo


MyThread foo


MyThread bar


foo bar


18.


class X implements Runnable


{


public static void main(String args[])


{


/* Missing code? */


}


public void run() {}


}


Which of the following line of code is suitable to start a thread ?


Thread t = new Thread(X);


Thread t = new Thread(X); t.start();


X run = new X(); Thread t = new Thread(run); t.start();


Thread t = new Thread(); x.run();


19. What is the value of "d" after this line of code has been executed?


double d = Math.round ( 2.5 + Math.random() );


2


3


4


2.5


20.


public class Myfile


{


public static void main (String[] args)


{


String biz = args[1];


String baz = args[2];


String rip = args[3];


System.out.println("Arg is " + rip);


}


}


Select how you would start the program to cause it to print: Arg is 2


java Myfile 222


java Myfile 1 2 2 3 4


java Myfile 1 3 2 2


java Myfile 0 1 2 3


21. What will be the output of the program?


public class WrapTest


{


public static void main(String [] args)


{


int result = 0;


short s = 42;


Long x = new Long("42");


Long y = new Long(42);


Short z = new Short("42");


Short x2 = new Short(s);


Integer y2 = new Integer("42");


Integer z2 = new Integer(42);


if (x == y) /* Line 13 */


result = 1;


if (x.equals(y) ) /* Line 15 */


result = result + 10;


if (x.equals(z) ) /* Line 17 */


result = result + 100;


if (x.equals(x2) ) /* Line 19 */


result = result + 1000;


if (x.equals(z2) ) /* Line 21 */


result = result + 10000;


System.out.println("result = " + result);


}


}


result = 1


result = 10


result = 11


result = 11010


22. What two statements are true about the result obtained from calling Math.random()?


The result is less than 0.0.


The result is greater than or equal to 0.0..


The result is less than 1.0.


The result is greater than 1.0.


The result is greater than or equal to 1.0.


1 and 2


2 and 3


3 and 4


4 and 5


23. What will be the output of the program?


class Equals


{


public static void main(String [] args)


{


int x = 100;


double y = 100.1;


boolean b = (x = y); /* Line 7 */


System.out.println(b);


}


}


true


false


Compilation fails


An exception is thrown at runtime


24. What will be the output of the program?


public class Test


{


public static void leftshift(int i, int j)


{


i <<= j;


}


public static void main(String args[])


{


int i = 4, j = 2;


leftshift(i, j);


System.out.printIn(i);


}


}


2


4


8


16


25. What will be the output of the program?


package foo;


import java.util.Vector; /* Line 2 */


private class MyVector extends Vector


{


int i = 1; /* Line 5 */


public MyVector()


{


i = 2;


}


}


public class MyNewVector extends MyVector


{


public MyNewVector ()


{


i = 4; /* Line 15 */


}


public static void main (String args [])


{


MyVector v = new MyNewVector(); /* Line 19 */


}


}


Compilation will succeed.


Compilation will fail at line 3.


Compilation will fail at line 5.


Compilation will fail at line 15.


26. What will be the output of the program?


TreeSet map = new TreeSet();


map.add("one");


map.add("two");


map.add("three");


map.add("four");


map.add("one");


Iterator it = map.iterator();


while (it.hasNext() )


{


System.out.print( it.next() + " " );


}


one two three four


four three two one


four one three two


one two three four one


27. What will be the output of the program?


public static void main(String[] args)


{


Object obj = new Object()


{


public int hashCode()


{


return 42;


}


};


System.out.println(obj.hashCode());


}


42


Runtime Exception


Compile Error at line 2


Compile Error at line 5


28.


void start() {


A a = new A();


B b = new B();


a.s(b);


b = null; /* Line 5 */


a = null;  /* Line 6 */


System.out.println("start completed"); /* Line 7 */


}


When is the B object, created in line 3, eligible for garbage collection?


after line 5


after line 6


after line 7


There is no way to be absolutely certain.


29.


class Test


{


private Demo d;


void start()


{


d = new Demo();


this.takeDemo(d); /* Line 7 */


} /* Line 8 */


void takeDemo(Demo demo)


{


demo = null;


demo = new Demo();


}


}


When is the Demo object eligible for garbage collection?


After line 7


After line 8


After the start() method completes


When the instance running this code is made eligible for garbage collection.


30.


public Object m()


{


Object o = new Float(3.14F);


Object [] oa = new Object[l];


oa[0] = o; /* Line 5 */


o = null;  /* Line 6 */


oa[0] = null; /* Line 7 */


return o; /* Line 8 */


}


When is the Float object, created in line 3, eligible for garbage collection?


just after line 5


just after line 6


just after line 7


just after line 8


31.


Given:


1. // insert code here


2. class StatTest {


3. public static void main(String[] args) {


4. System.out.println(Integer.MAX_VALUE);


5. }


6. }


Which, inserted independently at line 1, compiles? (Choose all that apply.)


A. import static java.lang;


B. import static java.lang.Integer;


C. import static java.lang.Integer.*;


D. import static java.lang.Integer.*_VALUE;


E. import static java.lang.Integer.MAX_VALUE;


F. None of the above statements are valid import syntax


32.


If three versions of MyClass.class exist on a file system:


Version 1 is in /foo/bar


Version 2 is in /foo/bar/baz


Version 3 is in /foo/bar/baz/bing


And the system's classpath includes


/foo/bar/baz


And this command line is invoked from /foo


java -classpath /foo/bar/baz/bing:/foo/bar MyClass


Which version will be used by java?


A. /foo/MyClass.class


B. /foo/bar/MyClass.class


C. /foo/bar/baz/MyClass.class


D. /foo/bar/baz/bing/MyClass.class


E. The result is not predictable


33.


Given:


3. class MyThread extends Thread {


4. public static void main(String [] args) {


5. MyThread t = new MyThread();


6. Thread x = new Thread(t);


7. x.start();


8. }


9. public void run() {


10. for(int i=0;i<3;++i) {


11. System.out.print(i + "..");


12. } } }


What is the result of this code?


A. Compilation fails


B. 1..2..3..


C. 0..1..2..3..


D. 0..1..2..


E. An exception occurs at runtime


34.


Given:


1. public class WaitTest {


2. public static void main(String [] args) {


3. System.out.print("1 ");


4. synchronized(args){


5. System.out.print("2 ");


6. try {


7. args.wait();


8. }


9. catch(InterruptedException e){}


10. }


11. System.out.print("3 ");


12. } }


What is the result of trying to compile and run this program?


A. It fails to compile because the IllegalMonitorStateException of wait() is not dealt


with in line 7


B. 1 2 3


C. 1 3


D. 1 2


E. At runtime, it throws an IllegalMonitorStateException when trying to wait


F. It will fail to compile because it has to be synchronized on the this object


35.


Assume the following method is properly synchronized and called from a thread A on an object B: wait(2000);


After calling this method, when will the thread A become a candidate to get another turn at


the CPU?


A. After object B is notified, or after two seconds


B. After the lock on B is released, or after two seconds


C. Two seconds after object B is notified


D. Two seconds after lock B is released


36.


Which are true? (Choose all that apply.)


A. It is appropriate to use assertions to validate arguments to methods marked public


B. It is appropriate to catch and handle assertion errors


C. It is NOT appropriate to use assertions to validate command-line arguments


D. It is appropriate to use assertions to generate alerts when you reach code that should not


be reachable


E. It is NOT appropriate for assertions to change a program’s state


37.


Given:


1. class Loopy {


2. public static void main(String[] args) {


3. int[] x = {7,6,5,4,3,2,1};


4. // insert code here


5. System.out.print(y + " ");


6. }


7. } }


Which, inserted independently at line 4, compiles? (Choose all that apply.)


A. for(int y : x) {


B. for(x : int y) {


C. int y = 0; for(y : x) {


D. for(int y=0, z=0; z<x.length; z++) { y = x[z];


E. for(int y=0, int z=0; z<x.length; z++) { y = x[z];


F. int y = 0; for(int z=0; z<x.length; z++) { y = x[z];


38.


Given:


3. public class Clumsy {


4. public static void main(String[] args) {


5. int j = 7;


6. assert(++j > 7);


7. assert(++j > 8): "hi";


8. assert(j > 10): j=12;


9. assert(j==12): doStuff();


10. assert(j==12): new Clumsy();


11. }


12. static void doStuff() { }


13. }


Which are true? (Choose all that apply.)


A. Compilation succeeds


B. Compilation fails due to an error on line 6


C. Compilation fails due to an error on line 7


D. Compilation fails due to an error on line 8


E. Compilation fails due to an error on line 9


F. Compilation fails due to an error on line 10


39


Given:


class Hexy {


public static void main(String[] args) {


Integer i = 42;


String s = (i<40)?"life":(i>50)?"universe":"everything";


System.out.println(s);


}


}


What is the result?


A. null


B. life


C. universe


D. everything


E. Compilation fails


F. An exception is thrown at runtime


40


Which statement(s) are true? (Choose all that apply.)


A. Cohesion is the OO principle most closely associated with hiding implementation details


B. Cohesion is the OO principle most closely associated with making sure that classes know


about other classes only through their APIs


C. Cohesion is the OO principle most closely associated with making sure that a class is


designed with a single, well-focused purpose


D. Cohesion is the OO principle most closely associated with allowing a single object to be


seen as having many types


41


Which is true? (Choose all that apply.)


A. "X extends Y" is correct if and only if X is a class and Y is an interface


B. "X extends Y" is correct if and only if X is an interface and Y is a class


C. "X extends Y" is correct if X and Y are either both classes or both interfaces


D. "X extends Y" is correct for all combinations of X and Y being classes and/or interfaces


42


Which statements are true about comparing two instances of the same class, given that the


equals() and hashCode() methods have been properly overridden? (Choose all that apply.)


A. If the equals() method returns true, the hashCode() comparison == might return false


B. If the equals() method returns false, the hashCode() comparison == might return true


C. If the hashCode() comparison == returns true, the equals() method must return true


D. If the hashCode() comparison == returns true, the equals() method might return true


E. If the hashCode() comparison != returns true, the equals() method might return true


43


Given:


public static void before() {


Set set = new TreeSet();


set.add("2");


set.add(3);


set.add("1");


Iterator it = set.iterator();


while (it.hasNext())


System.out.print(it.next() + " ");


}


Which statements are true?


A. The before() method will print 1 2


B. The before() method will print 1 2 3


C. The before() method will print three numbers, but the order cannot be determined


D. The before() method will not compile


E. The before() method will throw an exception at runtime


### Table 1

| 3. Which is a valid keyword in java? interface string Float unsigned |  |
| --- | --- |
| 4. Which one is a valid declaration of a boolean? boolean b1 = 0; boolean b2 = 'false'; boolean b3 = false; boolean b4 = Boolean.false(); boolean b5 = no; |  |
| 5. What is the numerical range of a char? -128 to 127 -(215) to (215) - 1 0 to 32767 0 to 65535  6.  public void foo( boolean a, boolean b) { 	if( a ) 	{     	System.out.println("A"); /* Line 5 */ 	} 	else if(a && b) /* Line 7 */ 	{     	System.out.println( "A && B"); 	} 	else /* Line 11 */ 	{     	if ( !b )     	{         	System.out.println( "notB") ;     	}     	else     	{         	System.out.println( "ELSE" ) ;     	} 	} }  If a is true and b is true then the output is "A && B" If a is true and b is false then the output is "notB" If a is false and b is true then the output is "ELSE" If a is false and b is false then the output is "ELSE" |  |
| 7.  public void test(int x) { 	int odd = 1; 	if(odd) /* Line 4 */ 	{     	System.out.println("odd"); 	} 	else 	{     	System.out.println("even"); 	} }  Which statement is true? |  |
