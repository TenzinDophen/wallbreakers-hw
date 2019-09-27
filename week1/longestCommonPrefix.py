class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        size = len(strs[0])
       
        res = ""
        
        for i in range(size):
            pref = strs[0][i]
            for j in strs:
                if i >= len(j):
                    return res
                else:
                    if (j[i] != pref):
                        return res
            res += pref
            
        return res
                    