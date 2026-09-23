# TExeter Thursday#2 - Quiz Prelims - Questions

> Converted from `TExeter Thursday#2 - Quiz Prelims - Questions.docx`


TExeter Thursday – Event #2


Prelims

- Which of the below statements is correct for the Java program below?

public void foo( boolean a, boolean b)


{


if( a )


{


System.out.println("A"); /* Line 5 */


}


else if(a && b) /* Line 7 */


{


System.out.println( "A && B");


}


else /* Line 11 */


{


if ( !b )


{


System.out.println( "notB") ;


}


else


{


System.out.println( "ELSE" ) ;


}


}


}

- If a is true and b is true then the output is "A && B"
- If a is true and b is false then the output is "notB"
- If a is false and b is true then the output is "ELSE"
- If a is false and b is false then the output is "ELSE"
- Points: 3
- Which statement in the below Java program, if placed in a class other than MyOuter or MyInner, instantiates an instance of the nested class?

public class MyOuter


{


public static class MyInner


{


public static void foo() { }


}


}

- MyOuter.MyInner m = new MyOuter.MyInner();
- MyOuter.MyInner mi = new MyInner();
- MyOuter m = new MyOuter(); MyOuter.MyInner mi = m.new MyOuter.MyInner();
- MyInner mi = new MyOuter.MyInner();
- Points: 3
- What causes compilation to fail in the below Java program?

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

- Line 5
- Line 6
- Line 12
- Line 14
- Points: 4
- What will be the output of the below Java program?

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

- result = 1
- result = 10
- result = 11
- result = 11010
- Points: 4
- What will be the output of the program?

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

- 2
- 4
- 8
- 16
- Points: 3
- When is the Demo object eligible for garbage collection?

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

- After line 7
- After line 8
- After the start() method completes
- When the instance running this code is made eligible for garbage collection.
- Points: 2
- If three versions of MyClass.class exist on a file system:
- Version 1 is in /foo/bar
- Version 2 is in /foo/bar/baz
- Version 3 is in /foo/bar/baz/bing
- And the system's classpath includes
- /foo/bar/baz
- And this command line is invoked from /foo
- java -classpath /foo/bar/baz/bing:/foo/bar MyClass
- Which version will be used by java?
- /foo/MyClass.class
- /foo/bar/MyClass.class
- /foo/bar/baz/MyClass.class
- /foo/bar/baz/bing/MyClass.class
- The result is not predictable
- Points: 2
- What is the output of the below Java program?

class A {


public int i;


public int j;


A() {


i = 1;


j = 2;


}


}


class B extends A {


int a;


B() {


super(ob);


}


}


class super_use {


public static void main(String args[])


{


B obj = new B();


System.out.println(obj.i + " " + obj.j)


}


}

- 1 2
- 2 1
- Runtime Error
- Compilation Error
- Points: 2
- What is the output of the below Java program?

class A {


int i;


void display() {


System.out.println(i);


}


}


class B extends A {


int j;


void display() {


System.out.println(j);


}


}


class inheritance_demo {


public static void main(String args[])


{


B obj = new B();


obj.i=1;


obj.j=2;


obj.display();


}


}

- 0
- 1
- 2
- Compilation Error
- Points: 2
- In .NET, where do we include the user lists for Form authentication?
- < credential>
- < authorization>
- < Identity>
- < authentication>
- Points: 1
- CLR in .NET is equivalent of:
- Java Virtual Machine
- Common language runtime
- Common type system
- Common language specification
- Points: 2
- What will be the output of the below SQL program if the input (?x) is 18. Assume the table name is num_values and column name is test.
- Table - Num_values

Note: Assume qualify statement above is an equivalent of TOP (N) in other DB engines. ?x is the input parameter (18) in the above query.

- 18
- 20
- 15
- 19
- Points: 3
- Assume that there two tables (sample data is only for illustration). What will be the output of the SQL query?

Table - product:


Table - customer:


Note: <> is the not equal to operator.

- List of all products without any customers
- List of all customers without products
- A Cartesian product of ALL customers and products
- None of the above
- Points: 2
- Employee table has 10 records. It has a non null salary column that is having unique values.

What will be the output of the below SQL query?

- 10
- 9
- 0
- 1
- Points: 2
- The user issues the following statement in Oracle. What will be displayed if the EMPID selected is 64094?
- 60494
- LOA
- Terminated
- Active
- Points: 2
- Out of 7 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?
- 24400
- 21300
- 210
- 25200
- Points: 3
- A train ,130 meters long travels at a speed of 45 km/hr crosses a bridge in 30 seconds. The length of the bridge is
- 270 m
- 245 m
- 235 m
- 220 m
- Points: 2
- A does 80% of a work in 20 days. He then calls in B and they together finish the remaining work in 3 days. How long B alone would take to do the whole work?
- 23 days
- 37 days
- 371/2 days
- 40 days
- Points: 2
- A starts business with Rs. 3500 and after 5 months, B joins with A as his partner. After a year, the profit is divided in the ratio 2 : 3. What is B's contribution in the capital?
- Rs. 7500
- Rs. 8000
- Rs. 8500
- Rs. 8500
- Points: 1

### Table 1

| test |
| --- |
| 10 |
| 15 |
| 20 |
| 22 |
| 25 |
| 30 |
| 33 |
| 41 |


### Table 2

| SELECT      test FROM num_values QUALIFY RANK() over (     ORDER BY      CASE WHEN (test - ?x ) < 0 THEN  (test - ?x ) * -1 ELSE  (test - ?x )  END      ASC)=1 |
| --- |


### Table 3

| product_id | name |
| --- | --- |
| 1 | Prod 1 |
| 2 | Prod 2 |
| 3 | Prod 3 |


### Table 4

| customer_id | name | product_id |
| --- | --- | --- |
| 1 | Cust 1 | 1 |
| 2 | Cust 2 | 2 |
| 3 | Cust 3 | 1 |


### Table 5

| SELECT product.name, customer.name  FROM product JOIN customer ON product.product_id <> customer.product_id |
| --- |


### Table 6

| SELECT COUNT(*) FROM employee WHERE salary > ANY (SELECT salary FROM employee) |
| --- |


### Table 7

| SELECT DECODE(  empid,                  38475, "Terminated",                  60494, "LOA",                  "Active"             ) FROM emp; |
| --- |
