class Solution:
    
        
        
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            index = abs(n)-1
            if nums[index] > 0:
                nums[index] = -nums[index]
                
            else:
                res.append(abs(n))
        
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = -nums[i]
            else:
                res.append(i+1)
                
        return res