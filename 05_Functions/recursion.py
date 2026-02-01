#The function who call itself again and again.
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5) 

def fact(l):
    if(l == 1 or l == 0):
        return 1
    return fact(l-1) * l
print(fact(4))

