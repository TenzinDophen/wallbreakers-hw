class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        for i, num in enumerate(A):
            if num%2 == 0:
                A[i], A[start] = A[start], A[i]
                start += 1
        
        return A