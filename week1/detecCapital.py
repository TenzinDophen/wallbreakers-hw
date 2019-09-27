class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitalFirst = False
        capitalAll = True
        smallAll = True
        
        for i, w in enumerate(word):
            if i == 0:
                if w.isupper():
                    capitalFirst = True
                    smallAll = False
                else:
                    capitalAll = False
                    
            else:
                if w.isupper(): 
                    smallAll = False
                    capitalFirst = False
                
                else:
                    capitalAll = False
                    
                    
        
        if capitalFirst or capitalAll or smallAll:
            return True
        return False
            
            