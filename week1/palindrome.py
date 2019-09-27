class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s)-1
        
        while(start < end):
            
            while start < end and not s[start].isalnum():
                start += 1
                
            sT = s[start]
            
            while start < end and not s[end].isalnum():
                end -= 1
                
            sE = s[end]
                
            if sT.lower() != sE.lower():
                return False
            start += 1
            end -= 1
            
            
        return True