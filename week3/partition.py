class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = []
        stack = []
        if len(S) == 0:
            return 0
        stack.append([0,1])
        for i in range(1,len(S)):
            c = S[i]
            
            if c not in S[0:i]:
                stack.append([stack[-1][1], i+1])
                
            else:
                while(c not in S[stack[-1][0]:stack[-1][1]]):
                    stack.pop()
                
                stack[-1][1] = i+1
            
        for i in stack:
            result.append(i[1]-i[0])
            
        return result