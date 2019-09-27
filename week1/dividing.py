class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            temp = i
            print(temp)
            while(temp != 0):
                num = temp % 10
                if num == 0 or i % num != 0 :
                    break
                temp = temp // 10
            
            if temp == 0:
                res.append(i)
                
        return res
                
                