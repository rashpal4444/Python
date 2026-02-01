# A function inside a class is called a method, and it defines the behavior of an object.
# calculate average of 3 subjects of a student
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi" , self.name, "your av score is" , sum/3)
s1 = student("rashpal" , [99, 67, 88] ) 
s1.get_avg()       