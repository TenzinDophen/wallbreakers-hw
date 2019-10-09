class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        both = A.split() + B.split()
        
        return [x for x in both if both.count(x) == 1]