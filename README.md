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

Meet 1:
    Matchup 1 hosted by H:
        [R, B, W, H]
    Matchup 2 hosted by E:
        [T, S, E]

Meet 2:
    Matchup 1 hosted by E:
        [T, H, E, W]
    Matchup 2 hosted by S:
        [R, B, S]

Meet 3:
    Matchup 1 hosted by B:
        [S, H, E, B]
    Matchup 2 hosted by T:
        [R, W, T]

Meet 4:
    Matchup 1 hosted by S:
        [R, E, S, W]
    Matchup 2 hosted by T:
        [B, H, T]

Meet 5:
    Matchup 1 hosted by R:
        [T, S, H, R]
    Matchup 2 hosted by W:
        [B, W, E]

Meet 6:
    Matchup 1 hosted by B:
        [B, T, E, R]
    Matchup 2 hosted by H:
        [W, H, S]
