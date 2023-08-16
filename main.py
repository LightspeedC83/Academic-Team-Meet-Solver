# creating a class system for each school's team
class school():
    """this is a object to model each school and each school object keeps track of the id_nums of all the other schools it has been matched up against"""
    def __init__(self,id_num):
        self.id_num = id_num
        self.previous_pairings = {} # keys are school ids (for other schools) and values are # of times this object has been paried with said school
        for x in range(1,8):
            if x != id_num:
                self.previous_pairings[x] = 0

# creating 7 school objects
schools = []
for x in range(1,8):
    schools.append(school(id_num=x))
    
matchup_schedule = [] # will be in the form [ [[a,b,c,d],[e,f,g] ], ... , [ [g,a,f,b], [c,e,d] ] ]

def school_to_id(schools_list):
    """function that takes a list of the school objects and returns a list of the id numbers for said school"""
    output = []
    for school in schools_list:
        output.append(school.id_num)
    return(output)

for round in range(6): # there are 6 rounds
    # generating the matchup for the first group (ie. the one with four slots)
    group_one = []
    for school in schools: # deciding on whether or not to add this school to group_one
        