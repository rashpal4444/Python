#The function who call itself again and again.
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)    