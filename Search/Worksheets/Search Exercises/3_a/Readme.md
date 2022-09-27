
Question 1
Given the following search graph, how many states will be visited until reaching the goal state using depth-first search?. Trace the states inside the search agenda until reaching the goal state.

<img width="340" alt="image" src="https://user-images.githubusercontent.com/63984422/192617527-f387931a-83a1-49c0-9442-938bdf0d026b.png">

The Goal state is 22

1, <br />
2,3,4, <br />
5,6,7,3,4, <br />
12,13,6,7,3,4,<br />
13,6,7,3,4,<br />
6,7,3,4,<br />
14,15,7,3,4,<br />
15,7,3,4,<br />
7,3,4,<br />
16,17,18,3,4,<br />
17,18,3,4,<br />
18,3,4,<br />
3,4,<br />
8,9,10,11,4,<br />
19,20,21,9,10,11,4,<br />
20,21,9,10,11,4,<br />
21,9,10,11,4,<br />
9,10,11,4,<br />
22,23,24,10,11,4,<br />

The number of visited states is 19
