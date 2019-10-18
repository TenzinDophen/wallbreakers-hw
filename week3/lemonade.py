from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(lambda: 0)
        
        for bill in bills:
        
            change = bill - 5
            for c in sorted(dic, reverse = True):
                
                if change >= c:
                    count = change // c
                    val = dic[c]
                    mini = min(count, val)
                    change = change - (mini*c)
                    dic[c] -= mini
    
            if change != 0:
                return False
            
            dic[bill] += 1
        return True