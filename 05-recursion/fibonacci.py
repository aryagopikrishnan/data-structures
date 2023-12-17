# fibonacci using recursion

def fib(i):
    
    if i == 0:
        return 0
    elif i == 1:
        return 1
    b = fib(i-1) + fib(i-2)
    print(b)
    return b


a = fib(5)
print(a)

