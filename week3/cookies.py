from heapq import _heappop_max, _heapify_max
  
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
#         g.sort(reverse=True)
#         result = 0
#         for i in sorted(s, reverse = True):
#             while(g and i < g[0]):
#                 g.pop(0)
            
#             if g:
#                 g.pop(0)
#                 result += 1
#             else:
#                 break
            
#         return result
        if not g or not s:
            
            return 0
        
        _heapify_max(g)
        _heapify_max(s)
        
        gMax, sMax, result = _heappop_max(g), _heappop_max(s), 0
        
        while(True):
            
            if sMax >= gMax:
                result += 1
                if not s:
                    
                    return result
                sMax = _heappop_max(s)
            if not g:
                print(g)
                return result
            gMax = _heappop_max(g)
            
        return result