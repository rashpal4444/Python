# If statement this statement is true when the conditions are fullfilled

age = 18
if age >= 18:
   print("You are an adult")
else:
   print("not an adult")  

print("age is >",age)


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible to vote!")
else:
    print(f"{name}, you are NOT eligible to vote.")