# Evidence: Feedback of Roshan Salvi

## Source
- **File:** `Feedback of Roshan Salvi.msg`
- **Date:** 2019-02-27
- **Ingested:** 2026-08-04
- **Channel:** email_archive
- **Category:** Feedback & Culture

## Email Metadata
- **From:** Vellal, Dattatreya
- **To:** Mishra, Nitin <nitin.mishra@philips.com>; Bder, Anas <anas.bder@philips.com>; Aklecha, Vishwajit <vishwajit.aklecha@philips.com>
- **Date:** 2019-02-27T11:13:02.674330-05:00
- **Thread depth:** 11
- **Is reply:** False

## Datta's Involvement
- **Role at time:** Project Architect, IDM
- **Involvement type:** Author

## Key Quotes
> From: Vellal, Dattatreya

> Discussion: (D: Datta, R: Roshan, N: Nitin)

> R: I think I should check for m & n to be greater than 0.

> D: Ok. Thank you. I have all the data points, do you have any questions?

> D: <Nitin,Datta - explain the roles and responsibilities>

## Full Email Content

```
Subject: Feedback of Roshan Salvi
From: Vellal, Dattatreya
To: Mishra, Nitin <nitin.mishra@philips.com>; Bder, Anas <anas.bder@philips.com>; Aklecha, Vishwajit <vishwajit.aklecha@philips.com>
Date: 2019-02-27T11:13:02.674330-05:00

--- Latest Reply ---
Hello Anas, Vishwa, Nitin,
Please find my feedback from my discussions with Roshan



Roshan Salvi
CG70
Coding
Java

--- Previous Message (1) ---
Collabedit scribble: http://collabedit.com/3v8j9

--- Previous Message (2) ---
Opinion: Recommend Roshan for subsequent rounds of discussion.

--- Previous Message (3) ---
Observation:
1. Roshan was steady minded, took his time to understand the problem, called out his understanding and validated it.
2. He was able to logically break the problem into sub-problem (of traversing right, down & left) & identified recursion as his style to solve this problem.
3. He was able to solve the algorithm he explained, fast, and neatly, with minimal errors.
4. There was a time when he had missed a few corner cases, but when pointed out, he was able to identify them.
5. He had initially solved the program for 'a' only, when i asked him to expand it to all the alphabets, because that's what the code demanded, he was able to identify the line where he'd make the changes.

--- Previous Message (4) ---
Problem given:

Alphabet Island - Figure out the no. of alphabet islands in the given mXn array.
The mXn array will be filled with 0 (water) and alphabets (land). The task is to figure out the no. of islands connected by land, and surrounded by water. Land "a" is said to be connected to land "b" if via one hop, land "b" can be reached via a vertical move, a horizontal move, or a diagonal move.

Input:
First line contains the value of m
Second line contains the value of n
From the third, there will be n lines, each containing m elements, every element separated by a space.

Output:
No. of alphabet islands in the given mXn array.

Here's an example:
6
6
0 0 a 0 0 0
0 a a a 0 0
a 0 0 0 a 0
0 0 0 0 0 0
a 0 0 0 0 0
0 0 0 0 0 a

Output:
3

--- Previous Message (5) ---
Final solution:
public int  findIsland(int[][] mn, int m, int n){

    if(m < 0 || n < 0 )
      return 0;

    int count = 0;
    for(int i=0 ; i < m-1 ; i++ ) {

       for(int j=0; j < n-1; j++ ) {

          if(mn[m][n] == 'a'){

              searchForAdjacentTile(mn, m , n );
              count += 1;
          }
       }

    }

    return count;

}

public void searchForAdjacentTile(int[][] mn, int m , int n ){
        if(m < 0  && m > (mn.length - 1)) return ;
        if(n < 0  && n > (mn[0].length-1)) return ;

        if(mn[m][n] == '0') return;

        mn[m][n]='0';

        searchForAdjacentTile(mn,m , n+1); //right
        searchForAdjacentTile(mn,m+1 , n); // down
        searchForAdjacentTile(mn,m , n-1); // left
        searchForAdjacentTile(mn,m+1,n+1); // missed - condition
        searchForAdjacentTile(mn,m-1,n-1); // missed - condition
}

--- Previous Message (6) ---
Discussion: (D: Datta, R: Roshan, N: Nitin)
D: <introduced himself, his role, and his background>
D: <explained the expectation of today's discussion>
D: <opened the floor for any questions, there were none, started with the problem statement>
<read the problem above, to know the problem statement>

D: Please take a few mins, read through the problem, let me know if you understand the problem, or need help, and then let's agree upon an approach to solve the problem and then i'll need your help in coding the approach. Is that ok?
R: Sure.

R: <explains the problem, has understood the problem correctly>

D: Ok, please articulate how you intend to solve this problem & then we can start coding.
R: Ok.
Go through all the index of mXn array.
The approach - I will have a counter, set to 0, counting the no. of islands.
Start with index 0, whenever we get 'a' in the index, have to traverse, right - solve this using recursion
start with 0,0, if there is no 'a', then i'll traverse the next index.
if there is an 'a', then i'll call this function recursively, will first go to current,right
the next traversal will be current,down
the next traversal will be current,left
all these are subjected to the base conditions - array boundary conditions

When I encounter a 0, i can convert it to -1, <thinks> - well it doesn't matter.
Instead, whenever i encounter an a, i will change it 0 (or -1)

D: What would you choose, 0 or -1, for replacing 'a' with?
R: If I choose -1, I have to <is unable to answer this>

D: Ok, may be the second question may help, what is the time-complexity of the algorithm?
R: I'll definitely be iterating for mXn * no. of islands we have.
D: Ok, so in the worst case you'll end up traversing the entire mXn, so the worst case complexity is O(k*m*n) -> 0(n^2)
R: Yeah.
D: Ok. Got it.
R: I am trying to see how we can avoid traversing the already visited node here.
D: Ok. May be we can delay th

[... truncated, full content in database ...]
```