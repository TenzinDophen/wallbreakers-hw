class Solution:
   
        
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0: 
            return 1
        
        if n == -1:
            return 1 / x
        
        halved, odd = divmod(n, 2)
        
        return self.myPow(x * x, halved) * (x if odd else 1)