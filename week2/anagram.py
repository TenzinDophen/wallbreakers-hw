from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sizeP = len(p)
        sCounter = Counter(s[:sizeP-1])
        pCounter = Counter(p)
        
        res = []
        for i in range(sizeP-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i-sizeP+1)
            
            sCounter[s[i-sizeP+1]] -= 1
            
            if sCounter[s[i-sizeP+1]] == 0:
                del sCounter[s[i-sizeP+1]]
        return res 