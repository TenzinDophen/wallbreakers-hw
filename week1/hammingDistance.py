class Solution:
    def findBinary(self, num: int) -> int:
        res = ""
        while(num != 0):
            rem = num % 2
                
            res += str(rem)
            
            num = num // 2
        res = res[::-1]
        return res
        
        
    def hammingDistance(self, x: int, y: int) -> int:
        
        binaryX = self.findBinary(x)
        binaryY = self.findBinary(y)
        
        lenX = len(binaryX)
        lenY = len(binaryY)
        
        if lenX > lenY:
            lenDiff = lenX - lenY
            addDiff = "0" * lenDiff
            binaryY = addDiff + binaryY
            
        else:
            lenDiff = lenY - lenX
            addDiff = "0" * lenDiff
            binaryX = addDiff + binaryX
        res = 0   
        for i in range(len(binaryX)):
            if binaryX[i] != binaryY[i]:
                res += 1
        return res
            
        