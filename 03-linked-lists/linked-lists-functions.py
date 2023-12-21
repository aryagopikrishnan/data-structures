# creating a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # method to print nodes in the LL

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # method to append to tail
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    
    # method to pop from tail
    
    def pop(self):
        # if self.length == 0:
        if self.head is None:
            return None  
        else:
            temp = self.head
            pre = self.head
            #while(temp.next):
            while temp.next is not None: 
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value

    # method to prepend (add node) to the head

    def prepend(self, value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            #new_node = None
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
    
    # method to pop first node from list

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            # self.head = self.head.next
            self.head = temp.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
        

    # method to get node at given index

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value




my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
# my_linked_list.prepend(1)

print(my_linked_list.get(3))

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())


# print(my_linked_list.pop()) # returns 2
# print(my_linked_list.pop()) # returns 1
# print(my_linked_list.pop()) # returns none




