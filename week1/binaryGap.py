class Solution:
    
    def findBinary(self, num: int) -> int:
        res = ""
        while(num != 0):
            rem = num % 2
                
            res += str(rem)
            
            num = num // 2
        res = res[::-1]
        
        return res
        
        
    def binaryGap(self, N: int) -> int:
        x = self.findBinary(N)
        print(x)
        prev = -1
        res = 0
        i = 0
        while( i < len(x)):
            if x[i] == "1":
                if prev == -1:
                    prev = i
                else:
                    res = max(res, (i - prev))
                    while( i < len(x) and x[i] == "1"):
                        i += 1
                    prev = i-1
           
            i += 1   
                        
        return res
        
            
            
            