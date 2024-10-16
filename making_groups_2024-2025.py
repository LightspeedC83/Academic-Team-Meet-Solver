import random

# creating a class system for each school's team
class school():
    """this is a object to model each school and each school object keeps track of the id_nums of all the other schools it has been matched up against"""
    def __init__(self,id_num,name):
        self.name = name
        self.id_num = id_num
        self.previous_pairings = {} # keys are school ids (for other schools) and values are # of times this object has been paried with said school
        for x in range(1,9):
            if x != id_num:
                self.previous_pairings[x] = 0
    
    def count_total_connections(self):
        """returns the total number of connections with other schools that this school has made"""
        connections = 0 
        for key in self.previous_pairings.keys():
            connections += self.previous_pairings[key]
        return(connections)
    
    def get_availiable_opponents(self):
        """returns list of opponent team names that the school has not played at least twice before"""
        availiable_opponents = []
        for key in self.previous_pairings.keys():
            if self.previous_pairings[key] < 2:
                availiable_opponents.append(key)
        return(availiable_opponents)


# creating the 8 school objects
schools = []
for x, y in zip(range(1,9), ["RCHS","SHS","BHS","RHS","HHS","TAHS","ERHS","WMHS"]):
    schools.append(school(id_num=x, name=y))

ordered_schools = schools[::]

# creating the first two meets in the meet schedule
matchup_1 = [[schools[0], schools[1], schools[2], schools[3], schools[4]], [schools[5], schools[6], schools[7]]] #HHS would sit out, if doing sit outs
matchup_2 = [[schools[4], schools[5], schools[0], schools[1], schools[2]], [schools[3], schools[6], schools[7]]] #BHS would sit out, if doing sit outs

meet_schedule = [matchup_1, matchup_2] # creating a list of all the meets and matchups

# updating the pairings dictionaries for each of the school objects to reflect the matchups
for round in [matchup_1, matchup_2]:
    for matchup in round:
        for school in matchup:
            matchup_copy = matchup[::]
            matchup_copy.remove(school)
            for other in matchup_copy:
                school.previous_pairings[other.id_num] += 1



for x in range(5):
    schools_copy = schools[::]
    random.shuffle([schools_copy])
    matchup_1 = [schools_copy.pop(0)]
    
    for x in range(3):
        #finding the school with the least number of connections to the schools in matchup_1
        candidate_connections = {}
        for candidate in schools_copy:
            total_connections = 0
            for school in matchup_1:
                total_connections += candidate.previous_pairings[school.id_num]
            candidate_connections[candidate] = total_connections
        
        best = schools_copy[0]
        for key in candidate_connections.keys():
            if candidate_connections[key] <= candidate_connections[best]:
                best = key
        matchup_1.append(best)
        schools_copy.remove(best)

    meet_schedule.append([matchup_1, schools_copy])

    # updating the pairing information
    for matchup in [matchup_1, schools_copy]:
        for school in matchup:
            matchup_copy = matchup[::]
            matchup_copy.remove(school)
            for other in matchup_copy:
                school.previous_pairings[other.id_num] += 1

#checking if every school is matched twice with every other school
check = True
for school in schools:
    for key in school.previous_pairings.keys():
        if school.previous_pairings[key] <2:
            check = False
    
# finding the schools that have too few matches with eachother
unmatched = []
for school in schools:
    for key in school.previous_pairings.keys():
        if school.previous_pairings[key] < 2:
            unmatched.append(schools[key-1])


#printing the meet infromation
for matchup in meet_schedule:
    print()
    matchup_list = []
    for section in matchup:
        section_list = []
        for school in section:
            section_list.append(school.name)
        matchup_list.append(section_list)
    print(matchup_list)

#printing the pairing information for each school with every other school
for school in ordered_schools:
    print(school.name+":")
    for key in school.previous_pairings.keys():
        print("   "+ ordered_schools[key-1].name, ":", school.previous_pairings[key])
    print()

print(check)
for school in unmatched:
    print(school.name)

    
"""

############################
#okay so the solution that this generates, is only off by one pairing. let's check our tweaked solution (refer to readme)

#checking our tweaked solution
tweaked_solution = [
    [['RCHS', 'SHS', 'BHS', 'RHS'], ['TAHS', 'ERHS', 'WMHS']],
    [['HHS', 'TAHS', 'RCHS', 'SHS'], ['RHS', 'ERHS', 'WMHS']],
    [['RCHS', 'WMHS', 'HHS', 'BHS'], ['SHS', 'RHS', 'TAHS', 'ERHS']],
    [['RCHS', 'ERHS', 'HHS', 'RHS'], ['SHS', 'BHS', 'TAHS', 'WMHS']],
    [['RCHS', 'WMHS', 'ERHS', 'SHS'], ['BHS', 'RHS', 'HHS', 'TAHS']],
    [['RCHS', 'TAHS', 'WMHS', 'RHS'], ['SHS', 'BHS', 'HHS', 'ERHS']],
    [['RCHS', 'ERHS', 'TAHS', 'BHS'], ['SHS', 'RHS', 'HHS', 'WMHS']]
    ]

#turning the names in the tweaked solution into objects
tweaked_solution_obj = []
for meet in tweaked_solution:
    meet_list = []
    for matchup in meet:
        matchup_list = []
        for school_name in matchup:
           matchup_list.append(ordered_schools[["RCHS","SHS","BHS","RHS","HHS","TAHS","ERHS","WMHS"].index(school_name)])

        meet_list.append(matchup_list)
    tweaked_solution_obj.append(meet_list)

#resetting the pairing information
for school in schools:
    for key in school.previous_pairings.keys():
        school.previous_pairings[key] = 0

#updating the pairing information based off the tweaked solution
for round in tweaked_solution_obj:
    for matchup in round:
        for school in matchup:
            matchup_copy = matchup[::]
            matchup_copy.remove(school)
            for other in matchup_copy:
                school.previous_pairings[other.id_num] += 1
        
#printing the meet infromation
for matchup in tweaked_solution_obj:
    print()
    matchup_list = []
    for section in matchup:
        section_list = []
        for school in section:
            section_list.append(school.name)
        matchup_list.append(section_list)
    print(matchup_list)

#printing the pairing information for each school with every other school
for school in ordered_schools:
    print(school.name+":")
    for key in school.previous_pairings.keys():
        print("   "+ ordered_schools[key-1].name, ":", school.previous_pairings[key])
    print()

#checking if every school is matched twice with every other school
check = True
for school in schools:
    for key in school.previous_pairings.keys():
        if school.previous_pairings[key] <2:
            check = False
print(check)

# finding the schools that have too few matches with eachother
unmatched = []
for school in schools:
    for key in school.previous_pairings.keys():
        if school.previous_pairings[key] < 2:
            unmatched.append(schools[key-1])
for school in unmatched:
    print(school.name)
    
    """