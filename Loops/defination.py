#loop is used to run same set of instruction again and again.

i = 1
while i <= 6:
    print (i)
    i += 1
print ("loop ended")


#print a multipication of a number.
n = int(input("enter a number :"))
i = 1
while i <= 10:
   print(n*i)
   i += 1


# search for number in tuple

num = (1, 4, 5, 6, 99, 44, 46, 36)

x = 46
i = 0
while i < len(num):
    if(num[i] == x):
      print("found at index i", i )
    i += 1