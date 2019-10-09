from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        
        for i in t:
            c[i] -= 1
            if c[i] < 0:
                return i