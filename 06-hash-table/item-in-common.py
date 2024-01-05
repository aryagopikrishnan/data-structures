# O(n) time complexity
# Comparing lists to find common item

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    
    return False


list1 = [1, 2, 3]
list2 = [3, 4, 5]

print(item_in_common(list1, list2))