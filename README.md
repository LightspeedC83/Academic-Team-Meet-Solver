# Academic Team Meet Solver

- This is a program to make match ups for the academic team. 
- There are seven teams in the district, but only 4 can meet at a school at a time. There are 6 meets in the season, each meet will take place at two different schools with 4 teams at one school and 3 teams at the other. 
- This program is to find a schedule where each school has the opportunity to play every other school two times. 

## The solution the program generated:
schools are identified with a number 1-7 and each list marks a meet location, while each newline marks a different day
- [1, 2, 3, 4], [5, 6, 7] 
- [5, 4, 7, 3], [1, 2, 6]
- [6, 4, 7, 2], [1, 3, 5]
- [1, 7, 6, 3], [2, 4, 5]
- [5, 6, 4, 1], [2, 3, 7]
- [2, 5, 7, 1], [3, 4, 6]

## The detailed infromation for the connections between schools
in the form of school id followed by {dictionary with keys that are the ids of other schools and values of how many times the school in question were matched with said school}
- 1: {2: 3, 3: 3, 4: 2, 5: 3, 6: 3, 7: 2}
- 2: {1: 3, 3: 2, 4: 3, 5: 2, 6: 2, 7: 3}
- 3: {1: 3, 2: 2, 4: 3, 5: 2, 6: 2, 7: 3}
- 4: {1: 2, 2: 3, 3: 3, 5: 3, 6: 3, 7: 2}
- 5: {1: 3, 2: 2, 3: 2, 4: 3, 6: 2, 7: 3}
- 6: {1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 7: 3}
- 7: {1: 2, 2: 3, 3: 3, 4: 2, 5: 3, 6: 3}


## constraints for finding a meeting arraingement and assigning schools
Now that there is a grouping of "schools" for all 6 meet days, we need to assign what schools those numbers actually correlate to. 

There are 7 Schools, each assigned one of the following letters:
- R
- B
- H
- T
- S
- E
- W

The assignment of letters to numbers in the needs to comply to the following constraints:
- Each school can host up to 2 matches (preferably one with 4 and one with 3)
- School R and school W only host one match each
- School R and school W cannot host eachother (ie. school R can't go to a match being hosted by school W and vice versa)

## what the program came up with
The program came up with the following hosting arraingement:

School number...
- 1 is r
- 2 is b
- 3 is w
- 4 is h
- 5 is t
- 6 is s
- 7 is e

The hosting arraingement is: (the index in the first list corresponds to who is hosting the matchup for that same index in the list on the right)
- ['h', 'e'] --> [ ['r', 'b', 'w', 'h'], ['t', 's', 'e'] ]
- ['w', 's'] --> [ ['t', 'h', 'e', 'w'], ['r', 'b', 's'] ]
- ['b', 't'] --> [ ['s', 'h', 'e', 'b'], ['r', 'w', 't'] ]
- ['s', 't'] --> [ ['r', 'e', 's', 'w'], ['b', 'h', 't'] ]
- ['r', 'e'] --> [ ['t', 's', 'h', 'r'], ['b', 'w', 'e'] ]
- ['b', 'h'] --> [ ['b', 't', 'e', 'r'], ['w', 'h', 's'] ]

## That's what the program came up with, but we can manually switch it so that the meet school w hosts only has three schools
If we do that, the new hosting arraingement is:
- ['h', 'e'] --> [ ['r', 'b', 'w', 'h'], ['t', 's', 'e'] ]
- ['e', 's'] --> [ ['t', 'h', 'e', 'w'], ['r', 'b', 's'] ]
- ['b', 't'] --> [ ['s', 'h', 'e', 'b'], ['r', 'w', 't'] ]
- ['s', 't'] --> [ ['r', 'e', 's', 'w'], ['b', 'h', 't'] ]
- ['r', 'w'] --> [ ['t', 's', 'h', 'r'], ['b', 'w', 'e'] ]
- ['b', 'h'] --> [ ['b', 't', 'e', 'r'], ['w', 'h', 's'] ]

## Presenting the solution a little more nicely:
(note that the meet numbers can be switched up so that schools don't have to host at back to back meets)

- Meet 1:
    - Matchup 1 hosted by H:
        - [R, B, W, H]
    - Matchup 2 hosted by E:
        - [T, S, E]

- Meet 2:
    - Matchup 1 hosted by E:
        - [T, H, E, W]
    - Matchup 2 hosted by S:
        - [R, B, S]

- Meet 3:
    - Matchup 1 hosted by B:
        - [S, H, E, B]
    - Matchup 2 hosted by T:
        - [R, W, T]

- Meet 4:
    - Matchup 1 hosted by S:
        - [R, E, S, W]
    - Matchup 2 hosted by T:
        - [B, H, T]

- Meet 5:
    - Matchup 1 hosted by R:
        - [T, S, H, R]
    - Matchup 2 hosted by W:
        - [B, W, E]

- Meet 6:
    - Matchup 1 hosted by B:
        - [B, T, E, R]
    - Matchup 2 hosted by H:
        - [W, H, S]


# New Contraints:
So the Problem has changed slightly and the contraints are now as follows:
- Still 6 meets with one grouping of 4 schools and one grouping of 3
- Each School still must be paired with every other school at least twice
- School E and School W must be paired with each other in the group of 3 for both of the times that they play eachother
- The third school in that grouping of 3 with School E and School W must be either School H or School T

# What the program came up with
The program came up with the following schedule:
- Meet 1: ['R', 'S', 'B', 'T'] | ['E', 'W', 'H']

- Meet 2: ['R', 'S', 'B', 'H'] | ['E', 'W', 'T']

- Meet 3: ['E', 'H', 'S', 'R'] | ['W', 'T', 'B']

- Meet 4: ['W', 'H', 'S', 'R'] | ['E', 'T', 'B']

- Meet 5: ['E', 'S', 'R', 'W'] | ['H', 'T', 'B']

- Meet 6: ['T', 'H', 'R', 'S'] | ['E', 'W', 'B']

The pairing information for this matchup possibility is as follows:
- School E: - {'W': 4, 'H': 2, 'T': 2, 'S': 2, 'B': 2, 'R': 2} - (connections = 14)
- School W: - {'E': 4, 'H': 2, 'T': 2, 'S': 2, 'B': 2, 'R': 2} - (connections = 14)
- School H: - {'E': 2, 'W': 2, 'T': 2, 'S': 4, 'B': 2, 'R': 4} - (connections = 16)
- School T: - {'E': 2, 'W': 2, 'H': 2, 'S': 2, 'B': 4, 'R': 2} - (connections = 14)
- School S: - {'E': 2, 'W': 2, 'H': 4, 'T': 2, 'B': 2, 'R': 6} - (connections = 18)
- School B: - {'E': 2, 'W': 2, 'H': 2, 'T': 4, 'S': 2, 'R': 2} - (connections = 14)
- School R: - {'E': 2, 'W': 2, 'H': 4, 'T': 2, 'S': 6, 'B': 2} - (connections = 18)

# Smoothing out connection problems with that answer
So that schedule fits the minimum criteria, but there are schools playing solely in one group way too many times. Now the task is to smooth out the unevenness in the total connections data (ie. we can't have some schools with 14 connections and others with 18, the distribution needs to be more even). The algorithm swaps random schools between groups in a meet and then only returns arraingements that have unique connection distributions, unique group 2 distributions, and at least two but no more than four connections with every other school.

The distribution that seemed best was: 

- Meet 1: ['R', 'S', 'B', 'T'] | ['E', 'W', 'H']

- Meet 2: ['R', 'S', 'B', 'H'] | ['E', 'W', 'T']

- Meet 3: ['W', 'B', 'T', 'H'] | ['E', 'R', 'S']

- Meet 4: ['R', 'B', 'W', 'E'] | ['T', 'H', 'S']

- Meet 5: ['S', 'R', 'W', 'H'] | ['T', 'E', 'B']

- Meet 6: ['E', 'S', 'W', 'H'] | ['R', 'T', 'B']

The metadata for this arraingement is as follows:
- E: - {'W': 4, 'H': 2, 'T': 2, 'S': 2, 'B': 2, 'R': 2} - (connections=14, num_group_two=4)
- W: - {'E': 4, 'H': 4, 'T': 2, 'S': 2, 'B': 2, 'R': 2} - (connections=16, num_group_two=2)
- H: - {'E': 2, 'W': 4, 'T': 2, 'S': 4, 'B': 2, 'R': 2} - (connections=16, num_group_two=2)
- T: - {'E': 2, 'W': 2, 'H': 2, 'S': 2, 'B': 4, 'R': 2} - (connections=14, num_group_two=4)
- S: - {'E': 2, 'W': 2, 'H': 4, 'T': 2, 'B': 2, 'R': 4} - (connections=16, num_group_two=2)
- B: - {'E': 2, 'W': 2, 'H': 2, 'T': 4, 'S': 2, 'R': 4} - (connections=16, num_group_two=2)
- R: - {'E': 2, 'W': 2, 'H': 2, 'T': 2, 'S': 4, 'B': 4} - (connections=16, num_group_two=2)

# Part 2: Electric Boogaloo!
- The above stuff was for the 2023-2024 school year, and now the constraints have changed (agian) for the 2024-2025 school year. So let's solve this problem again baby! Working with the new constraints is in the file "making_groups_2024-2025.py"

## The new contraints
The schools are as follows (there's one more added):
- RCHS
- SHS
- BHS
- RHS
- HHS
- TAHS
- ERHS
- WMHS

The last 2 schools (ERHS & WMHS) are the ones that will only host once, everyone else will host twice (7 week schedule.)
The parameters are otherwise the same:
- When ERHS and WMHS host, they should have only 3 teams at that event, and NOT RCHS or SHS.
- When RCHS hosts, ERHS and WMHS should not be scheduled to come (too great of a distance.)
- Every pair of schools has to be at the same location at least twice. Each school should be able to play only 2 of the other schools at any meet.

This is the first attempt at a solution that the program came up with:
- [['RCHS', 'SHS', 'BHS', 'RHS'], ['TAHS', 'ERHS', 'WMHS']]
- [['HHS', 'TAHS', 'RCHS', 'SHS'], ['RHS', 'ERHS', 'WMHS']]
- [['RCHS', 'WMHS', 'HHS', 'BHS'], ['SHS', 'RHS', 'TAHS', 'ERHS']]
- [['RCHS', 'ERHS', 'HHS', 'RHS'], ['SHS', 'BHS', 'TAHS', 'WMHS']]
- [['RCHS', 'WMHS', 'ERHS', 'BHS'], ['SHS', 'RHS', 'HHS', 'TAHS']]
- [['RCHS', 'TAHS', 'WMHS', 'RHS'], ['SHS', 'BHS', 'HHS', 'ERHS']]
- [['RCHS', 'ERHS', 'TAHS', 'BHS'], ['SHS', 'RHS', 'HHS', 'WMHS']]

The problem is that BHS and RHS only meet once, let's see if we can manually change that and still get a valid answer. So I switched BHS and SHS in the 5th meet to get this pairing infromation:
- [['RCHS', 'SHS', 'BHS', 'RHS'], ['TAHS', 'ERHS', 'WMHS']]
- [['HHS', 'TAHS', 'RCHS', 'SHS'], ['RHS', 'ERHS', 'WMHS']]
- [['RCHS', 'WMHS', 'HHS', 'BHS'], ['SHS', 'RHS', 'TAHS', 'ERHS']]
- [['RCHS', 'ERHS', 'HHS', 'RHS'], ['SHS', 'BHS', 'TAHS', 'WMHS']]
- [['RCHS', 'WMHS', 'ERHS', 'SHS'], ['BHS', 'RHS', 'HHS', 'TAHS']]
- [['RCHS', 'TAHS', 'WMHS', 'RHS'], ['SHS', 'BHS', 'HHS', 'ERHS']]
- [['RCHS', 'ERHS', 'TAHS', 'BHS'], ['SHS', 'RHS', 'HHS', 'WMHS']]

I then wrote some shit code tacked on to the end of the same file ("making_groups_2024-2025.py") that manually put in this meet schedule and then checked whether or not it worked. And it does work! The pairing information for this tweaked shedule is as follows:
- RCHS: {SHS:3, BHS:3, RHS:3, HHS:3, TAHS:3, ERHS:3, WMHS:3}
- SHS: {RCHS:3, BHS:3, RHS:3, HHS:3, TAHS:3, ERHS:3, WMHS:3}
- BHS: {RCHS:3, SHS:3, RHS:2, HHS:3, TAHS:3, ERHS:2, WMHS:2}
- RHS: {RCHS:3, SHS:3, BHS:2, HHS:3, TAHS:3, ERHS:3, WMHS:3}
- HHS: {RCHS:3, SHS:3, BHS:3, RHS:3, TAHS:2, ERHS:2, WMHS:2}
- TAHS: {RCHS:3, SHS:3, BHS:3, RHS:3, HHS:2, ERHS:3, WMHS:3}
- ERHS: {RCHS:3, SHS:3, BHS:2, RHS:3, HHS:2, TAHS:3, WMHS:3}
- WMHS: {RCHS:3, SHS:3, BHS:2, RHS:3, HHS:2, TAHS:3, ERHS:3}

if schools don't sit out in the first rounds, we get this schedule:
- [['RCHS', 'SHS', 'BHS', 'RHS', 'HHS'], ['TAHS', 'ERHS', 'WMHS']]
- [['HHS', 'TAHS', 'RCHS', 'SHS', 'BHS'], ['RHS', 'ERHS', 'WMHS']]
- [['RCHS', 'WMHS', 'ERHS', 'HHS'], ['SHS', 'BHS', 'RHS', 'TAHS']]
- [['RCHS', 'WMHS', 'TAHS', 'RHS'], ['SHS', 'BHS', 'HHS', 'ERHS']]
- [['RCHS', 'ERHS', 'TAHS', 'RHS'], ['SHS', 'BHS', 'HHS', 'WMHS']]
- [['RCHS', 'WMHS', 'BHS', 'ERHS'], ['SHS', 'RHS', 'HHS', 'TAHS']]
- [['RCHS', 'SHS', 'WMHS', 'ERHS'], ['BHS', 'RHS', 'HHS', 'TAHS']]

if HHS withdraws from competition, and we move to a 6 week schedule, things get more complicated...