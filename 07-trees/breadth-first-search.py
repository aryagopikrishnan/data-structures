# bfs - breadth first search using queues

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



    # breadth first search method

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
        


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
# returns the return list 
# in the same order the tree was created
print(my_tree.BFS())
