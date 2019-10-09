class Solution:
    def isHappy(self, n: int) -> bool:
        sumSet = set()
        
        while(n not in sumSet):
            if n == 1:
                return True
            sumSet.add(n)
            tempSum = 0
            while (n != 0):
                rem = n % 10
                tempSum += pow(rem, 2)
                n = n // 10
            n = tempSum
            
        return False