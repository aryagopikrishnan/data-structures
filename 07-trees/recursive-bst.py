# recursive binary search tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    # method to create root pointer

    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)


    def r_insert(self, value):
        self.__r_insert(self.root, value)

    # recursive contains

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST Contains 27:")
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))