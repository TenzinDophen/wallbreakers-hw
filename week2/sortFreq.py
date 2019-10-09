class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        
        key  = sorted(c, key = lambda x: -c[x])
        
        res = ""
        for i in key:
            res += (i * c[i])
        
        return res