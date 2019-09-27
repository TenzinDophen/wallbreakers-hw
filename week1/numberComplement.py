class Solution:
    def findComplement(self, num: int) -> int:
        res = ""
        while(num != 0):
            rem = num % 2
            if rem == 0:
                rem = 1
            else: 
                rem = 0
                
            res += str(rem)
            
            num = num // 2
        res = res[::-1]
        size = len(res)-1
        
        result = 0
        for i in range(len(res)):
            result += pow(2, size) * int(res[i])
            size -= 1
            
        return result
            