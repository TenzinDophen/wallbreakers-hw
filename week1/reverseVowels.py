class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "aeiou"
        s = list(s)
        
        start = 0
        end = len(s)-1
        
        while start <= end:
            i = s[start]
            j = s[end]
            
            if i.lower() in vowels:
                if j.lower() in vowels:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                if j.lower() in vowels:
                    start += 1
                else:
                    start += 1
                    end -= 1
                
        return "".join(s)
                    
        
        
                        
            