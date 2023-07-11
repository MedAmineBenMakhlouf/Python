# OOP
# attributes & method
# attribute : what student can have - characteristics (nouns)
# method: what the student can do - (functions inside the class) actions (verbs)

student_1 = ["John","Mayer",40,[9.8,10,10]] #list

student_1 = {
    'first_name':"John",
    'last_name':"Mayer",
    'age':40,
    'marks':[9.8,10,10],
    'fav_number': 25
} #dict

class Student:
    #!CONSTRUCTOR
    def __init__(self,first_name,last_name,age,marks,fav_number):
        # attribute ------ values
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marks = marks
        self.fav_number = fav_number
    
    def increase_age(self):
        print("this is self:",self)
        return None

john = Student("John","Max",35,[9.0,8.9,10],25)

print(john.first_name,john.last_name)