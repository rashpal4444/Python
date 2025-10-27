a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c ):
    print("first number is the largest", a)
elif(b >= c):
     print("second number is the largest", b)
else:
     print("third the largest", c)          