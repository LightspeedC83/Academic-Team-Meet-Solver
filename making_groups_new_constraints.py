# creating a class system for each school's team
class school():
    """this is a object to model each school and each school object keeps track of the ids of all the other schools it has been matched up against"""
    def __init__(self,id):
        self.id = id
        self.previous_pairings = {} # keys are school ids (for other schools) and values are # of times this object has been paried with said school
        for x in "EWHTSBR":
            if x != id:
                self.previous_pairings[x] = 0
    def count_total_connections(self):
        connections = 0 
        for key in self.previous_pairings.keys():
            connections += self.previous_pairings[key]
        return(connections)

# creating 7 school objects
schools = []
for x in "EWHTSBR":
    schools.append(school(id=x))


# populating the matchup schedule list with the first match up of schools
first_meet = [ ["R","S","B","T"], ["E", "W", "H"] ]
second_meet = [ ["R","S","B","H"], ["E", "W", "T"] ]
matchup_schedule = [] # will be in the form [ [[a,b,c,d],[e,f,g] ], ... , [ [g,a,f,b], [c,e,d] ] ]

for meet in first_meet, second_meet: #adding the corresponding shcool objects to the matchup schedule
    meet_objects = []
    
    for match in meet:
        match_objects = []
        for letter in match:
            for team in schools:
                if team.id == letter:
                    match_objects.append(team)
        meet_objects.append(match_objects)

    matchup_schedule.append(meet_objects)


def print_matchup_schedule():
    """prints the matchup schedule in readable form"""
    for meet in matchup_schedule:
        meet_list =[]
        for match in meet:
            obj_list = []
            for obj in match:
                obj_list.append(obj.id)
            meet_list.append(obj_list)
        print(str(meet_list[0]) + " | " + str(meet_list[1]) )
        print()

def print_school_metadata():
    """prints the dictionaries containing the number of times each school has been with another"""
    for school in schools:
        print(school.id, school.previous_pairings, school.count_total_connections())

def find_school(id):
    """returns the school object with the same id as the argument"""
    for school in schools:
        if school.id == id:
            return(school)
        
# updating each school's metadata based on the first two rounds
for meet in matchup_schedule: # updating pairing metadata
    for match in meet:
        for first in match:
            for other in match:
                if first != other:
                    first.previous_pairings[other.id] = first.previous_pairings[other.id] + 1

for school in schools: # updating connection metadata
    school.count_total_connections()

print_matchup_schedule()
print_school_metadata()

# Now the algorithm that generates the next 4 meet pairings
for round in range(4): # there are 6 rounds but we set up the first two matchups already so this loop will govern the pairing creation for the next four rounds
    # generating the matchup for the first group (ie. the one with four slots)
    group_one = []
    group_two = []
    
    # determining the school with the least connections and then putting that in group one
    lowest = [schools[0], schools[0].count_total_connections()]
    for school in schools:
        if school.count_total_connections() < lowest[1]:
            lowest = [school, school.count_total_connections()]
    group_one.append(lowest[0])
    
    schools_copy = schools[:]
    schools_copy.remove(lowest[0])
    

    # finding the schools with the next lowest number of connections and who doesn't already have 2+ connections with the school in group one
    for slot in range(3):
        # find the schools with the lease number of connections to the schools in group one
        possibilities = schools_copy[:]
        for added in group_one:
            for key in added.previous_pairings.keys():
                if added.previous_pairings[key] >=2:
                    print(find_school(key))
                    print("key is "+ key)
                    for school in possibilities:
                        print(school.id)
                    possibilities.remove(find_school(key))
        
        if len(possibilities) == 0: #if every possible school has a connection with the school with the lowest connections
            print("aaaaaaaaaaaa")
        else:
            #finds the school with the lowest number of connections in the possibilities list
            lowest = [possibilities[0], possibilities[0].count_total_connections()]
            for school in possibilities:
                if school.count_total_connections() < lowest[1]:
                    lowest[0] = [school, school.count_total_connections()]

            group_one.append(lowest[0])
            schools_copy.remove(lowest[0])
    
    # adding the other schools to group two 
    for school in schools_copy:
        group_two.append(school)

    matchup_schedule.append([group_one,group_two])
    
    # updating the school's metadata
    for group in group_one,group_two:
        for first in group:
            for other in group:
                if first != other:
                    first.previous_pairings[other.id] = first.previous_pairings[other.id] + 1

    print_matchup_schedule()
    print_school_metadata()


















'''
def school_to_id(schools_list):
    """function that takes a list of the school objects and returns a list of the id numbers for said school"""
    output = []
    for school in schools_list:
        output.append(school.id)
    return(output)

def print_matchups():
    """function that prints the parings in the matchup_schedule list"""
    global matchup_schedule
    output = ""
    for meet in matchup_schedule:
        output += f"{school_to_id(meet[0])}, {school_to_id(meet[1])} \n"
    print(output)
 
def update_parings(meet_matchup):
    """function that updates the dictionaries keeping track of whcih school 
    has been paired with which other school in each of the school objects"""
    for matchup in meet_matchup:
        for school in matchup:
            other_schools = matchup[:]
            other_schools.remove(school)
            
            for other in other_schools:
                school.previous_pairings[other.id] = school.previous_pairings[other.id] +1 #not sure if you can do a +=1 with the dictionary here

matchup_schedule = [] # will be in the form [ [[a,b,c,d],[e,f,g] ], ... , [ [g,a,f,b], [c,e,d] ] ]
for x in range(7): # populating the matchup schedule list with the first match up of schools
    if x<4:
        matchup_schedule[0][0].append(schools[x])
    else:
        matchup_schedule[0][1].append(schools[x])

#updating the pairing records of all the school objects after that first round matchup
update_parings(matchup_schedule[0])

for round in range(1,6): # there are 6 rounds but we set up the first matchup already (this way schools start out with some histroy of playing eachother)
    # generating the matchup for the first group (ie. the one with four slots)
    group_one = []
    group_two = []
    
    # determining the school with the least connections and then putting that in group one
    lowest = [schools[0], schools[0].count_connections()]
    for school in schools:
        if school.count_connections() < lowest[1]:
            lowest = [school, school.count_connections()]
    group_one.append(lowest[0])
    schools_copy = schools[:]
    schools_copy.remove(lowest[0])
    
    for place in range(3):
        lowest = []
        for school in schools_copy: # deciding on whether or not to add this school to group_one
            if len(group_one) < 4 :
                # finding the school object that has the least number of connections to the schools in group_one 
                connections = 0
                for other in group_one:
                    connections += school.previous_pairings[other.id]

                if lowest == []:
                    lowest = [school, connections]
                elif connections <= lowest[1]:
                    lowest = [school, connections]
        
        group_one.append(lowest[0])
        schools_copy.remove(lowest[0]) # removing what we added to group one from schools_copy so the next bit works
    
    # adding the schools that aren't in group one to group 2
    group_two = schools_copy
    
    matchup_schedule.append([group_one,group_two])
    update_parings(matchup_schedule[round])

print_matchups() #printing the matchups
#printing the connections list for each school
print()
for school in schools:
    print(f"{school.id}: {school.previous_pairings}")

'''