# SCHEDULER_VIEWER
This program contains this three algorithms:<br>
- Round Robin <br>
- Shortest Remaining time <br>
- Preemptive with priorities <br>
<br>
This program lets you visualualize in an excel sheet, how the scheduler handles the processes execute time in a cpu given a quantum (<i>if you run the RoundRobin option</i>) and given the data of the processes you want.<br><br>

| Process Name   |      Petition Time      |  TotalCpuTime |
|----------|:-------------:|------:|
| A |  0 | 6 |
| B |    1   |   6 |
| C | 4 |   2 |
| D | 8 |   7 |
| E | 11 |   5 |<br>

If you want to compute the data from the table above, you will need to insert the data to the Data.txt just like the format below.<br><br>
A<br>
0<br>
6<br>
B<br>
1<br>
6<br>
C<br>
4<br>
2<br>
D<br>
8<br>
7<br>
E<br>
11<br>
5<br>
<br>
If you want to compute the scheduler given priorities (<i>the lowest priority goes first</i>):<br>

| Process Name   |      Petition Time      |   TotalCpuTime  |  Priority  |
|----------|:-------------:|------:|------:|
| A |  0 | 5 |3 |
| B |    2   |   3 |3 |
| C | 4 |   3 |1 |
| D | 6 |   4 |2 |
| E | 8 |   2 |1 |<br>
<br>
If you want to calculate the scheduler with priorities, you will need to insert the data to the Data.txt just like the format below.<br><br>
A<br>
0<br>
5<br>
3<br>
B<br>
2<br>
3<br>
3<br>
C<br>
3<br>
4<br>
1<br>
D<br>
6<br>
4<br>
2<br>
E<br>
8<br>
2<br>
1<br>
