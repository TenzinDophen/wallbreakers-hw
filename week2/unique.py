from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
       
            
        c = Counter(s)
        
        for i, n in enumerate(s):
            if c[n] == 1:
                return i
        
        return -1