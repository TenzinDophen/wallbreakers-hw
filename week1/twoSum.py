class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #not sorted
        
        res = {}
        for n, i in enumerate(nums):
            num = target - i
            if num in res:
                return [res[num], n]
            res[i] = n
            
        return False