class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        print(res)
        for num in nums:

            res ^= num
            print("num", num)
            print("res", res)
        return res