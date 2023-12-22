# Constructor for BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    # method to create root pointer

    def __init__(self):
        self.root = None

    # method to insert a node 

    def insert(self, value):
        new_node = Node(value)
        # if tree is empty
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                # left
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                # right
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    
    # method to check if tree contains a value
    # returns true or false

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value: # left
                temp = temp.left
            elif value > temp.value: # right
                temp = temp.right
            else: # equal
                return True
        return False




# my_tree = BinarySearchTree()
# print(my_tree.root)
                

# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
        

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)

print(my_tree.contains(76))
print(my_tree.contains(18))


        
