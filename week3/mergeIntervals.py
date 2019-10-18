class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        result = []
        for interval in intervals:
            
            if not result:
                result.append(interval)
            else:
                start = interval[0]
                if start <= result[-1][1]:
                    end = max(result[-1][1],interval[1])
                    result[-1][1] = end
                else:
                    result.append(interval)
                    
        return result