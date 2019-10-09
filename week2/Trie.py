class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.endWord = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for i in word:
            index = ord(i)-ord("a")
            if root.children[index] == None:
                root.children[index] = Trie()
            root = root.children[index]
        root.endWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        
        for i in word:
            index = ord(i)-ord("a")
            if root.children[index] == None:
                return False
            root = root.children[index]
        if root.endWord == True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self
        
        for i in prefix:
            index = ord(i)-ord("a")
            if root.children[index] == None:
                return False
            root = root.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)