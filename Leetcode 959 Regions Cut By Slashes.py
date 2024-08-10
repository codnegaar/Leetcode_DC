'''
Leetcode 959 Regions Cut By Slashes

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
Given the grid grid represented as a string array, return the number of regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'. 

Example 1:
        Input: grid = [" /","/ "]
        Output: 2
        
Example 2:
        Input: grid = [" /","  "]
        Output: 1

Example 3:
        Input: grid = ["/\\","\\/"]
        Output: 5
        Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
         
Constraints:
        n == grid.length == grid[i].length
        1 <= n <= 30
        grid[i][j] is either '/', '\', or ' '.
'''

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Divide each square into 4 triangles
        uf = UnionFind(4 * n * n) 
        
        for row in range(n):
            for col in range(n):
                cell = grid[row][col]
                index = 4 * (row * n + col) 
                
                # Union all parts of the cell based on the character
                if cell == ' ':
                    # Union all 4 triangles
                    uf.union(index + 0, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)
                elif cell == '/':
                    # Union top-left and bottom-right, top-right and bottom-left
                    uf.union(index + 0, index + 3)
                    uf.union(index + 1, index + 2)
                elif cell == '\\':
                    # Union top-left and top-right, bottom-left and bottom-right
                    uf.union(index + 0, index + 1)
                    uf.union(index + 2, index + 3)
                
                # Union current cell with the cell below it
                if row < n - 1:
                    uf.union(index + 2, index + 4 * n)
                
                # Union current cell with the cell to the right
                if col < n - 1:
                    uf.union(index + 1, index + 4 + 3)
        
        # Count the number of unique regions
        unique_regions = sum(1 for i in range(4 * n * n) if uf.find(i) == i)
        
        return unique_regions
