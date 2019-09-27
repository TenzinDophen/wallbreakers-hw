class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate through each item
        #do DFS hortinatally and vertically and assign visited
        #count
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    res += 1
                    self.dfs(grid, i, j, visited)
        return res
    
    def dfs(self, grid, i, j, visited):
        
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and (i,j) not in visited:
            visited.add((i,j))
            self.dfs(grid, i+1, j, visited)
            self.dfs(grid, i-1, j, visited)
            self.dfs(grid, i, j+1, visited)
            self.dfs(grid, i, j-1, visited)
        
                    
        
                    
                    