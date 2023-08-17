# Academic Team Meet Solver

- This is a program to make match ups for the academic team. 
- There are seven teams in the district, but only 4 can meet at a school at a time. There are 6 meets in the season, each meet will take place at two different schools with 4 teams at one school and 3 teams at the other. 
- This program is to find a schedule where each school has the opportunity to play every other school two times. 

## The solution the program generated:
[1, 2, 3, 4], [5, 6, 7] 
[5, 4, 7, 3], [1, 2, 6]
[6, 4, 7, 2], [1, 3, 5]
[1, 7, 6, 3], [2, 4, 5]
[5, 6, 4, 1], [2, 3, 7]
[2, 5, 7, 1], [3, 4, 6]

### The detailed infromation for the connections between schools
1: {2: 3, 3: 3, 4: 2, 5: 3, 6: 3, 7: 2}
2: {1: 3, 3: 2, 4: 3, 5: 2, 6: 2, 7: 3}
3: {1: 3, 2: 2, 4: 3, 5: 2, 6: 2, 7: 3}
4: {1: 2, 2: 3, 3: 3, 5: 3, 6: 3, 7: 2}
5: {1: 3, 2: 2, 3: 2, 4: 3, 6: 2, 7: 3}
6: {1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 7: 3}
7: {1: 2, 2: 3, 3: 3, 4: 2, 5: 3, 6: 3}