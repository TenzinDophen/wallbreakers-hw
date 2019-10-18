class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.helper(A, 0, len(A)-1)
    
    def helper(self, A, start, end):
        mid = (start+end)//2
        
        if A[mid-1] < A[mid] > A[mid+1]:
            return mid
        
        elif A[mid-1] > A[mid]:
            return self.helper(A, start, mid-1)
        else:
            return self.helper(A, mid+1, end)