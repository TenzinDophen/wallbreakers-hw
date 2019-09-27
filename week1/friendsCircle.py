class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    if i == j:
                        count += 1
                        self.allFriends(M, i, j)
                        
        return count
                    
    
    def allFriends(self, M, row, col):
        M[row][col] = 0
        M[col][row] = 0
        
        for i in range(len(M[row])):
            if M[row][i] == 1:
                if row == i:
                    M[row][i] = 0
                else:
                    self.allFriends(M, i, row)
                
        