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
        """returns the total number of connections with other schools that this school has made"""
        connections = 0 
        for key in self.previous_pairings.keys():
            connections += self.previous_pairings[key]
        return(connections)
    
    def get_availiable_opponents(self):
        """returns list of opponent team letters that the school has not played at least twice before"""
        availiable_opponents = []
        for key in self.previous_pairings.keys():
            if self.previous_pairings[key] < 2:
                availiable_opponents.append(key)
        return(availiable_opponents)

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

# print_matchup_schedule()
# print_school_metadata()

# Now the algorithm that generates the next 4 meet pairings
for round in range(4): # there are 6 rounds but we set up the first two matchups already so this loop will govern the pairing creation for the next four rounds
    # generating the matchup for the first group (ie. the one with four slots)
    group_one = []
    
    # determining the school with the least connections and then putting that in group one
    lowest = [schools[0], schools[0].count_total_connections()]
    for school in schools:
        if school.count_total_connections() < lowest[1]:
            lowest = [school, school.count_total_connections()]
    group_one.append(lowest[0])
    
    schools_copy = schools[:]
    schools_copy.remove(lowest[0])
    
    for slot in range(3):
        for school in schools_copy:
            for possibility in group_one:
                if possibility.id in school.get_availiable_opponents() and len(group_one) < 4:
                    group_one.append(school)
                    schools_copy.remove(school)
                    break
    
    group_two = [school for school in schools_copy]
    matchup_schedule.append([group_one,group_two])
    

    # updating the school's metadata
    for group in group_one,group_two:
        for first in group:
            for other in group:
                if first != other:
                    first.previous_pairings[other.id] = first.previous_pairings[other.id] + 1

print_matchup_schedule()
print_school_metadata()