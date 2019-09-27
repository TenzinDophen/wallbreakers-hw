class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in dic:
                val = dic[i]
                val += 1
                dic[i] = val
            
            else:
                dic[i] = 1 
                
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
                if dic[j] < 0:
                    return False
        
        return True