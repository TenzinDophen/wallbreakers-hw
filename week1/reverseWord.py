class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        
        s = s.split()
        
        for i, n in enumerate(s):
            for j in range(len(n)-1, -1, -1):
                result += n[j]
                
            if i != len(s)-1:
                result += " "
            
        return result