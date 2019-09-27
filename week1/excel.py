class Solution:
    def indexChar(self, char):
        return ord(char) - ord("A") + 1
    
    def titleToNumber(self, s: str) -> int:
        size = len(s)-1
        res = 0
        for i in range(len(s)):
            num = self.indexChar(s[i])
            
            if size > 0:
                sAdd = pow(26, size) *  int(num)
            else:
                sAdd = int(num)
            res += sAdd
            
            size -= 1
            
        return res