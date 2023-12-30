# dfs - depth first search

# using binary search tree construct
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    # method to create root pointer

    def __init__(self):
        self.root = None   


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


    # def pre order

    def dfs_pre_order(self):
        results = []
        # recursive function
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)

# prints the tree from left to right
# [47, 21, 18, 27, 76, 52]
print(my_tree.dfs_pre_order())
