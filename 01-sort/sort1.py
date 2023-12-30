# sort array from smallest to largest (selection sort)


def findSmallest(arr):
    # stores the smallest value
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# sorts in a new array

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([4,6,3,56,54,7,9,0]))
