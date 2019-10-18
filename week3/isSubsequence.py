class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        if not s:
            return True
        
        for i in t:
            if i == s[count]:
                count += 1
                if count >= len(s):
                    return True
        return False
        
#     #def isSubsequence(self, s: str, t: str) -> bool:
        
#         if len(s) > len(t):
#             return False
        
#         if len(s) == len(t):
#             return hash(s) == hash(t)
        
#         ls = list(s)
#         while ls: 
#             try:
#                 t = t[t.index(ls.pop(0))+1:] 
#             except:
#                 return False
        
#         return True