class Student:
    college_name = "ct college"

    def __init__(self, name, marks):
        self.name = name
        self .marks = marks
    def welcome(self):
        print("welcome student", s1.name )    




s1 = Student("rashpal" , 99)
print(s1.name, s1.marks)

s2 = Student("rahul" , 66)
print(s2.name , s2.marks)

print(Student.college_name)