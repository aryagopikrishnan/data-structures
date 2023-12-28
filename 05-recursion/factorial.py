
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))


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

# countdown1(3)

