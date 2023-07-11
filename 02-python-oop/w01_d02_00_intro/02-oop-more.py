class Student:
    school="MIT"
    all_student=[]
    #!CONSTRUCTOR
    def __init__(self,first_name,last_name,age,marks,fav_number):
        # attribute ------ values
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marks = marks
        self.fav_number = fav_number
        Student.all_student.append(self)
    
    def increase_age(self):
        print("this is self:",self)
        return None
    def __repr__(self) -> str:
        return f"STUDENT FIRST NAME: {self.first_name} LAST NAME {self.last_name}"
    
john = Student("john","Max",40,[9,8,10],25)

print(john)
print(john.school)
print(Student.all_Student)

for student in Student.all_students:
    print(student.first_name)