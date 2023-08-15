# creating a class system for each school's team
class school():
    def __init__(self,id_num):
        self.id_num = id_num

schools = []
for x in range(1,8):
    schools.append(school(id_num=x))
    

for x in schools:
    print(x)

