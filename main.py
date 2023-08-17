# creating a class system for each school's team
class school():
    """this is a object to model each school and each school object keeps track of the id_nums of all the other schools it has been matched up against"""
    def __init__(self,id_num):
        self.id_num = id_num
        self.previous_pairings = {} # keys are school ids (for other schools) and values are # of times this object has been paried with said school
        for x in range(1,8):
            if x != id_num:
                self.previous_pairings[x] = 0
    def count_connections(self):
        connections = 0 
        for key in self.previous_pairings.keys():
            connections += self.previous_pairings[key]
        return(connections)

# creating 7 school objects
schools = []
for x in range(1,8):
    schools.append(school(id_num=x))

def school_to_id(schools_list):
    """function that takes a list of the school objects and returns a list of the id numbers for said school"""
    output = []
    for school in schools_list:
        output.append(school.id_num)
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
                school.previous_pairings[other.id_num] = school.previous_pairings[other.id_num] +1 #not sure if you can do a +=1 with the dictionary here

matchup_schedule = [[[],[]]] # will be in the form [ [[a,b,c,d],[e,f,g] ], ... , [ [g,a,f,b], [c,e,d] ] ]
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
                    connections += school.previous_pairings[other.id_num]

                if lowest == []:
                    lowest = [school, connections]
                elif connections < lowest[1]:
                    lowest = [school, connections]
        
        group_one.append(lowest[0])
        schools_copy.remove(lowest[0]) # removing what we added to group one from schools_copy so the next bit works
    
    # adding the schools that aren't in group one to group 2
    group_two = schools_copy
    
    matchup_schedule.append([group_one,group_two])
    update_parings(matchup_schedule[round])

print_matchups() #printing the matchups
#printing the connections list for each  school
print()
for school in schools:
    print(f"{school.id_num}: {school.previous_pairings}")
