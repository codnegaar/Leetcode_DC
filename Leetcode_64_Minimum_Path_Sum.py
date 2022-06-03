'''
Dynamic programing solution
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:return
        
        # Define the size
        m = len(grid)
        n = len(grid[0])
        
        # Check horizontally
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
          
        #check vertically
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        
        # find the min in rows and columns
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        
        # return 
        return grid[m-1][n-1]
    

        
