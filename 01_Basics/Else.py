# elif is used where all the conditions are checked untill the real condition is not satisfy

light = "green"
if (light == "red"):
  print("stop")

elif (light == "green"):
  print("go")
  print("end of code")

#2nd example To know the grades by using loops

marks = int(input("enter student marks :"))
if (marks >= 90):
  grade = "A"
elif (marks >= 80 and marks <= 90):
  grade = "B"
elif (marks >= 70 and marks <= 80):
  grade = "C"
else :
  grade = "D" 
print ("grade of the student -",grade)      