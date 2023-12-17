# summing an array using recursion

def sum(arr):
    if not arr:
        return 0
    else:
        a = arr[0] + sum(arr[1:])
    return a

# sum([2,4,6])



# Recursive function to count number of items in a list
def count(arr):
    if not arr:
        return 0
    else:
        counter = 1 + count(arr[1:])
        print(counter)
    return counter
    
# count([2,4,6])



# Recursive function to find maximum number in an array




