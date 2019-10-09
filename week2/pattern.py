class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        pattern = list(pattern)
        
        
        return len(s) == len(pattern) and len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s))