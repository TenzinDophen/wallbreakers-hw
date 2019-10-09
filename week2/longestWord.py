
class Trie:
    def __init__(self):
      
        self.arr = [None] * 26
        self.endWord = False
        self.word = ""
    
    def addWord(self, word):
        root = self
        
        for n, i in enumerate(word):
            index = ord(i) - ord("a")
            if root.arr[index] == None:
                if n != len(word)-1:
                    return 
                root.arr[index] = Trie()
                root.arr[index].word = word[:n+1]
            root = root.arr[index]
            if n == len(word)-2:
                root.endWord = False
        root.endWord = True  

class Solution:
    def findLongest(self, tree):
        result = ""
        root = tree
        queue = []
        queue.append(root)
        
        while (queue):
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                
                for j in range(25, -1, -1):
                    if (node.arr[j] != None):
                        if (node.arr[j].endWord == True):
                            
                            result = node.arr[j].word
                            
                        queue.append(node.arr[j])

        return result
                
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key = lambda x: len(x))
        tree = Trie()

        for i in words:
            tree.addWord(i)
        sol = Solution()
        return sol.findLongest( tree)