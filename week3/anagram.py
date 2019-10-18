class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        
        dic = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for i in t:
            if i in dic:
                dic[i] -= 1
                if dic[i] < 0:
                    return False
            else:
                return False
            
        return True