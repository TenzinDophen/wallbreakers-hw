class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 0
        result = 0
        if len(prices) == 0:
            return 0
        mini = prices[0]
        
        for price in prices:
            result = max(price-mini, result)
            mini = min(mini, price)
            
        return result