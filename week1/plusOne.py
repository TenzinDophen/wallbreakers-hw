class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        prev = 0
        res = 0
        result = []
        if digits:
            num = digits[len(digits)-1]
            num = num + 1
            if num >= 10:
                prev = num // 10
                num = num % 10
            res = num
        
        c = 10       
        for i in range(len(digits)-2, -1, -1):
            num = digits[i] + prev
            prev = 0
            if num >= 10:
                prev = num // 10
                num = num % 10
            
            res = num * c + res
            c = c * 10
        if prev > 0:
            res = prev * c + res
            
        resS = str(res)
        
        for num in resS:
            result.append(num)
            
        return result
            