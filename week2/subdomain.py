from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = Counter()
        for i in cpdomains:
            s = i.split()
            
            dic = {}
            
            key = s.pop(0)
            s = "".join(s)

            s = s.split(".")
            
            for i in range(len(s)):
                r = ".".join(s[i:])
                if r in dic:
                    dic[r] += 1
                else:
                    dic[r] = int(key)
                    
            c.update(dic)
        
        res = []
        for i in c:
            
            res.append(str(c[i]) +  " " + str(i)) 
        
        return res