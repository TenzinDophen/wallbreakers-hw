class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.helper(nums, target, 0, len(nums)-1)
    
    def helper(self, nums, target, start, end):
        
        mid = (end + start)//2
        if start > end:
            return -1
        elif nums[mid] == target:
            return mid
        elif  target > nums[mid]:
            return self.helper(nums, target, mid+1, end)
        else:
            return self.helper(nums, target, start, mid-1)