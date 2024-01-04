# hash table contructor

class HashTable:
    def __init__(self, size = 7):
        # creating a list of size 7 containing none
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            #returns a number from 0 to 6
            my_hash = (my_hash + ord(letter) * 11) % len(self.data_map)
            # print(my_hash)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key) # create index to store kv pair
        if self.data_map[index] == None:
            self.data_map[index] = [] # initialize empty list at that index
        self.data_map[index].append([key, value])


    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key: # checks key [0]
                    return self.data_map[index][i][1] # returns value [1]
        return None
    

    def keys(self):
        key_list = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    key_list.append(self.data_map[i][j][0]) # 0 for key and 1 for value
        return key_list



my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
# print(my_hash_table.get_item('bolt'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))
print(my_hash_table.keys())
