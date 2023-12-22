# hash table contructor

class HashTable:
    def __init__(self, size = 7):
        # creating a list of size 7 containing none
        self.data_map = [None] * size

    def __hash__(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


my_hash_table = HashTable()
my_hash_table.print_table()