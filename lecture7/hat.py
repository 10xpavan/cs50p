import random


class Hat:
    #def __init__(self):               also because you dont have to instante an add anywhere now on
        #self. 
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


#hat = Hat()                               #since you are useing classmethod you dont have to create a object like this to class funcitons inside class
Hat.sort("Harry")