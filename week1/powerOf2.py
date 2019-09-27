class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return self.helper(n)
    
    def helper(self, n):
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        else:
            return self.helper(n//2)