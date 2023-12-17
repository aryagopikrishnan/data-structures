
#infinite recursion
def countdown(i):
    print(i)
    countdown(i-1)


#adding a base case
def countdown1(i):
    print(i)
    if(i<=0):
        return
    else:
        countdown1(i-1)

countdown1(3)

