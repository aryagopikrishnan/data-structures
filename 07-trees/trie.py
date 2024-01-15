class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString= False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insertion
    def insert(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("insert successful")


my_trie = Trie()
my_trie.insert("App")
my_trie.insert("AppS")