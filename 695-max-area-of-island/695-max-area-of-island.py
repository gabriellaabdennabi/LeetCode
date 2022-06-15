class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxAreaOfIsland = 0
        
        
        
        
        
        def dfs(grid,row,col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                return 0 
            
            grid[row][col] = 0 
            
            return 1 + (dfs(grid,row+1,col)+dfs(grid,row-1,col)+dfs(grid,row,col+1)+dfs(grid,row,col-1))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxAreaOfIsland = max(maxAreaOfIsland,dfs(grid,row,col))
                    
        return maxAreaOfIsland
                    
        
        