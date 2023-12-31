# constructor - using linked lists to create a stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


    # method to push a value to stack
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    # method to pop / remove

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height -= 1
            return temp.value
        



# my_stack = Stack(2)
# my_stack.push(1)
# my_stack.print_stack()
        
my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
print(my_stack.pop(), '\n')
my_stack.print_stack()

