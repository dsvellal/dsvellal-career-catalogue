# TExeter Thursday#2 - Quiz Prelims - Answer Keys

> Converted from `TExeter Thursday#2 - Quiz Prelims - Answer Keys.docx`


TExeter Thursday – Event #2


Prelims Answer Keys


### Table 1

| Q. No | Answer | Notes | Points |
| --- | --- | --- | --- |
| 1 | Option C | Option C is correct. The output is "ELSE". Only when a is false do the output lines after 11 get some chance of executing.  Option A is wrong. The output is "A". When a is true, irrespective of the value of b, only the line 5 output will be executed. The condition at line 7 will never be evaluated (when a is true it will always be trapped by the line 12 condition) therefore the output will never be "A && B".  Option B is wrong. The output is "A". When a is true, irrespective of the value of b, only the line 5 output will be executed.  Option D is wrong. The output is "notB". | 3 |
| 2 | Option A | MyInner is a static nested class, so it must be instantiated using the fully-scoped name ofMyOuter.MyInner.  Option B is incorrect because it doesn't use the enclosing name in the new.  Option C is incorrect because it uses incorrect syntax. When you instantiate a nested class by invoking new on an instance of the enclosing class, you do not use the enclosing name. The difference between Option A and C is that Option C is calling new on an instance of the enclosing class rather than just new by itself.  Option D is incorrect because it doesn't use the enclosing class name in the variable declaration. | 3 |
| 3 | Option D | Option D is correct. Compilation fails because of an unreachable statement at line 14. It is a compile-time error if a statement cannot be executed because it is unreachable. The question is now, why is line 20 unreachable? If it is because of the assert then surely line 6 would also be unreachable. The answer must be something other than assert. Examine the following:  A while statement can complete normally if and only if at least one of the following is true:  - The while statement is reachable and the condition expression is not a constant expression with value true.  -There is a reachable break statement that exits the while statement. The while statement at line 11 is infinite and there is no break statement therefore line 14 is unreachable. | 4 |
| 4 | Option B | Line 13 fails because == compares reference values, not object values. Line 15 succeeds because bothString and primitive wrapper constructors resolve to the same value (except for the Character wrapper). Lines 17, 19, and 21 fail because the equals() method fails if the object classes being compared are different and not in the same tree hierarchy. | 4 |
| 5 | Option B | Java only ever passes arguments to a method by value (i.e. a copy of the variable) and never by reference. Therefore the value of the variable i remains unchanged in the main method.  If you are clever you will spot that 16 is 4 multiplied by 2 twice, (4 * 2 * 2) = 16. If you had 16 left shifted by three bits then 16 * 2 * 2 * 2 = 128. If you had 128 right shifted by 2 bits then 128 / 2 / 2 = 32. Keeping these points in mind, you don't have to go converting to binary to do the left and right bit shifts. | 3 |
| 6 | Option D | Option D is correct. By a process of elimination.  Option A is wrong. The variable d is a member of theTest class and is never directly set to null.  Option B is wrong. A copy of the variable d is set to null and not the actual variable d.  Option C is wrong. The variable d exists outside thestart() method (it is a class member). So, when thestart() method finishes the variable d still holds a reference. | 2 |
| 7 | Option D | D is correct. A -classpath included with a java invocation overrides a system classpath.  When java is using any classpath, it reads the classpath from left to right, and uses the  first match it finds.   A, B, C, and E are incorrect based on the above. | 2 |
| 8 | Option A | Keyword super is used to call constructor of class A by constructor of class B. Constructor of a initializes i & j to 1 & 2 respectively. output: $ javac super_use.java $ java super_use 1 2 | 2 |
| 9 | Option C | class A & class B both contain display() method, class B inherits class A, when display() method is called by object of class B, display() method of class B is executed rather than that of Class A. output: $ javac inheritance_demo.java $ java inheritance_demo 2 | 2 |
| 10 | Option A | Straightforward | 1 |
| 11 | Option A | Straightforward | 1 |
| 12 | Option B | The SQL query will return the value/result that is closest to the input value | 3 |
| 13 | Option  D | Option A is not correct because that will require a LEFT JOIN where RIGHT table is NULL. Option B is not correct because that will require a RIGHT JOIN where LEFT table is NULL. Option C is not correct because that will require a CROSS JOIN By elimination, Option D is the right answer. | 2 |
| 14 | Option B | ANY compares a value with each of the values in a list or results from a query and evaluates to true if the result of an inner query contains at least one row. ANY must be preceded by comparison operators (=,>,<,<>) Employee table has 10 records and each value in non-NULL SALARY column is unique. So, in 10 records one of the record will be minimum which cannot be greater than any nine value of the salary column. Hence the condition WHERE SALARY > ANY (SELECT SALARY FROM employee) will be true nine times. So, the COUNT() outputs 9. | 2 |
| 15 | Option D | None of the decode condition checks will succeed (note that the input is 64094 and not 60494) and hence the value returned will be “Active” | 1 |
| 16 | Option D | Number of ways of selecting 3 consonants out of 7 = 7C3 Number of ways of selecting 2 vowels out of 4 = 4C2  Number of ways of selecting 3 consonants out of 7 and 2 vowels out of 4 = 7C3 x 4C2 =(7×6×53×2×1)×(4×32×1)=210 It means that we can have 210 groups where each group contains total 5 letters (3 consonants and 2 vowels).  Number of ways of arranging 5 letters among themselves = 5!= 5 x 4 x 3 x 2 x 1 = 120 Hence, Required number of ways = 210 x 120 = 25200 | 3 |
| 17 | Option B | Assume the length of the bridge = x meter Total distance covered = 130+x meter total time taken = 30s speed = Total distance covered /total time taken = (130+x)/30 m/s => 45 × (10/36) = (130+x)/30 => 45 × 10 × 30 /36 = 130+x => 45 × 10 × 10 / 12 = 130+x => 15 × 10 × 10 / 4 = 130+x => 15 × 25 = 130+x = 375 => x = 375-130 =245 | 3 |
| 18 | Option C | Whole work will be done by A and B in (3 x 5) = 15 days. | 2 |
| 19 | Option D | Let B's capital be Rs. x.  14x = 126000  x = 9000. | 1 |
| Total Points | Total Points | Total Points | 44 |
