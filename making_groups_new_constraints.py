import random

# creating a class system for each school's team
class school():
    """this is a object to model each school and each school object keeps track of the ids of all the other schools it has been matched up against"""
    def __init__(self,id):
        self.id = id
        self.previous_pairings = {} # keys are school ids (for other schools) and values are # of times this object has been paried with said school
        for x in "EWHTSBR":
            if x != id:
                self.previous_pairings[x] = 0
        
        self.num_group_two = 0

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
    x =1
    for meet in matchup_schedule:
        meet_list =[]
        for match in meet:
            obj_list = []
            for obj in match:
                obj_list.append(obj.id)
            meet_list.append(obj_list)
        print(f"Meet {x}: " + str(meet_list[0]) + " | " + str(meet_list[1]) )
        print()
        x+=1

def print_school_metadata():
    """prints the dictionaries containing the number of times each school has been with another"""
    for school in schools:
        print(f"{school.id}: - {school.previous_pairings} - (connections={school.count_total_connections()}, num_group_two={school.num_group_two})")

def find_school(id):
    """returns the school object with the same id as the argument"""
    for school in schools:
        if school.id == id:
            return(school)
        

def update_pairings(matchup_schedule):
    """updates all school pairing metadata based on the matchup schedule"""
    for school in schools: #first clearing all the pairing metadata
        for key in school.previous_pairings.keys():
            school.previous_pairings[key] = 0

    for meet in matchup_schedule: # updating pairing metadata based on the matchup schedule
        for match in meet:
            for first in match:
                for other in match:
                    if first != other:
                        first.previous_pairings[other.id] = first.previous_pairings[other.id] + 1

# updating each school's metadata based on the first two rounds
update_pairings(matchup_schedule)

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
print("Schedule that meets bare minimum criteria:")
print_matchup_schedule()
print_school_metadata()
print()

# taking the output from the initial generation of a solution and swapping values to find alternate arraingements that fit the criteria
identifier_distributions = []
for x in range(1000):
    meet_index = 1
    for meet in matchup_schedule[2:]:
        meet_index +=1
        found_new_option = False
        num_tries = 0
        while not found_new_option and num_tries < 100:
            # swapping two random schools across the lists
            meet_copy = meet[:]
            school_one = meet_copy[0].pop(random.randint(0,len(meet_copy[0])-1))
            school_two = meet_copy[1].pop(random.randint(0,len(meet_copy[1])-1))
            meet_copy[0].append(school_two)
            meet_copy[1].append(school_one)

            
            # updating the parings for the schools with the new possible arraingment
            matchup_schedule_copy = matchup_schedule[:]
            matchup_schedule_copy[meet_index] = meet_copy
            update_pairings(matchup_schedule_copy)

            # checking to see if the schools in the new matchup arraingment have at least two connections with every school
            good_swap = True 
            for school in schools:
                for key in school.previous_pairings.keys():
                    if school.previous_pairings[key] < 2:
                        good_swap = False
                        break
            
            if good_swap:
                found_new_option = True
                matchup_schedule = matchup_schedule_copy
                
                #checking to see if the total connection distributions is acceptable
                update_pairings(matchup_schedule)
                printable = True
                for school in schools:
                    if school.count_total_connections() not in [14,15,16]: #checking connection distribution
                        printable = False
                        break
                    for key in school.previous_pairings.keys(): # making sure max connections between schools doesn't exceed 4
                        if school.previous_pairings[key] > 4:
                            printable = False
                            break
                
                # Ensuring that no one school has more than 3 meets in group 2
                for meet in matchup_schedule: #updating the number of times each school has been in group two in the metadata
                    for school in meet[1]:
                        school.num_group_two +=1

                for school in schools: #if any school has been in group two more than 3 times, it's not printable
                    if school.num_group_two > 4:
                        printable = False
                        break
                        
                if printable:
                    # getting a connection distribution
                    connection_distribution = []
                    for school in schools:
                        connection_distribution.append(school.count_total_connections())
                    group_two_distribution = []
                    for school in schools:
                        group_two_distribution.append(school.num_group_two)

                    identifier_distribution = [connection_distribution, group_two_distribution]
                    if identifier_distribution not in identifier_distributions:
                        identifier_distributions.append(identifier_distribution)
                        print("alternate schedule option:")
                        print_matchup_schedule()
                        print_school_metadata()
                        print()
                        break
                else:
                    #resetting the school's metadata for the number of times it's been in group 2
                    for school in schools:
                        school.num_group_two = 0
            else:
                num_tries +=1
