class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        lenP = len(p)
        if lenP > len(s):
            return result
        
        p = sorted(p)
        
        sortS = sorted(s[:lenP])
        
        if sortS == p:
                result.append(0)
        for i in range(1, len(s) - lenP+1):
            
            sortS.remove(s[i-1])
            bisect.insort(sortS, s[i+lenP-1])
            
           
            if sortS == p:
                result.append(i)
        
        return result