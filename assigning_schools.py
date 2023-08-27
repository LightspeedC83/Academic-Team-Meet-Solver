meet_schedule = [
    [ [1, 2, 3, 4], [5, 6, 7] ],
    [ [5, 4, 7, 3], [1, 2, 6] ],
    [ [6, 4, 7, 2], [1, 3, 5] ],
    [ [1, 7, 6, 3], [2, 4, 5] ],
    [ [5, 6, 4, 1], [2, 3, 7] ],
    [ [2, 5, 7, 1], [3, 4, 6] ]
]

connections = {
    1: {2: 3, 3: 3, 4: 2, 5: 3, 6: 3, 7: 2},
    2: {1: 3, 3: 2, 4: 3, 5: 2, 6: 2, 7: 3},
    3: {1: 3, 2: 2, 4: 3, 5: 2, 6: 2, 7: 3},
    4: {1: 2, 2: 3, 3: 3, 5: 3, 6: 3, 7: 2},
    5: {1: 3, 2: 2, 3: 2, 4: 3, 6: 2, 7: 3},
    6: {1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 7: 3},
    7: {1: 2, 2: 3, 3: 3, 4: 2, 5: 3, 6: 3}
}

class School():
    def __init__(self, id_num, id_letter, connections, meets_hosted):
        self.id_num = id_num
        self.id_letter = id_letter
        self.connections = connections
        self.meets_hosted = meets_hosted

possible_letters = ["r", "b", "w", "h", "t", "s", "e" ]
count = 0
schools = []
for key in connections.keys():
    schools.append(
        School(
            id_num=key,
            connections=connections[key],
            meets_hosted=0,
            id_letter = possible_letters[count]
        )
    )
    count +=1

# schools with only two meets together are: 1&7, 1&4, 2&3, 2&6, 3&5, 4&7, 5&6

def find_school(id_num):
    for school in schools:
        if school.id_num == id_num:
            return(school)
        

hosting_schedule = [] # list reflecting who is hosting which meet in the meet schedule in the form: [ [x,y], [x,y], [x,y], [x,y], [x,y], [x,y] ]

for meet in meet_schedule:
    hosts = []
    for split in meet:
        letters_in_split = []
        for id in split:
            letters_in_split.append(find_school(id).id_letter)
        
        for x in split: #establishing the lowest at not school r or w
            if find_school(x).id_letter not in ["r", "w"]:
                lowest = find_school(x)
                break

        for id in split:
            current_school = find_school(id)
            if current_school.meets_hosted <= lowest.meets_hosted and not (current_school.id_letter in ["r", "w"] and current_school.meets_hosted >= 1) and not (("r" in letters_in_split and "w" in letters_in_split) and current_school.id_letter in ["r", "w"]): # if the meets hosted is lower than the lowest and its not school r or w if it has already hosted 1 or more meets and if r and w are in the same split, neither can host
                lowest = current_school

        hosts.append(lowest.id_letter)
        lowest.meets_hosted = lowest.meets_hosted + 1
    
    hosting_schedule.append(hosts)



for school in schools:
    print(school.id_num, school.id_letter)
print()
for x in hosting_schedule:
    print(x)

print()

for meet in meet_schedule:
    letters_meet = []
    for split in meet:
        letters_split = []
        for x in split:
            letters_split.append(find_school(x).id_letter)
        letters_meet.append(letters_split)
    print(letters_meet)