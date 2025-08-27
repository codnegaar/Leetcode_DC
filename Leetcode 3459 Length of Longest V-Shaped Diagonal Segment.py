'''
Leetcode 3459 Length of Longest V-Shaped Diagonal Segment

You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
        Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
        Continues the sequence in the same diagonal direction.
        Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.
        Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

Example 1:
        Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
        Output: 5
        Explanation: The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:
        Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
        Output: 4
        Explanation: The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:
        Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
        Output: 5
        Explanation: The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:
Input: grid = [[1]]
Output: 1
Explanation: The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

Constraints:
        n == grid.length
        m == grid[i].length
        1 <= n, m <= 500
        grid[i][j] is either 0, 1 or 2.
        
'''
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])  # Get the dimensions of the grid
        
        @cache  # Memoization to optimize recursive calls
        def dfs(row, col, turn, direction, target):
            # Base case: Check boundaries and if the cell matches the target value
            if row not in range(n) or col not in range(m) or grid[row][col] != target:
                return 0
            
            # Toggle the target between 2 and 0 after each step
            target = 0 if grid[row][col] == 2 else 2
            
            # Move diagonally based on the direction
            if direction == 0:  # Top-left diagonal
                if turn:
                    return 1 + max(dfs(row - 1, col - 1, turn, 0, target), 
                                   dfs(row - 1, col + 1, False, 1, target))
                return 1 + dfs(row - 1, col - 1, turn, 0, target)
            
            elif direction == 1:  # Top-right diagonal
                if turn:
                    return 1 + max(dfs(row - 1, col + 1, turn, 1, target), 
                                   dfs(row + 1, col + 1, False, 2, target))
                return 1 + dfs(row - 1, col + 1, turn, 1, target)
            
            elif direction == 2:  # Bottom-right diagonal
                if turn:
                    return 1 + max(dfs(row + 1, col + 1, turn, 2, target), 
                                   dfs(row + 1, col - 1, False, 3, target))
                return 1 + dfs(row + 1, col + 1, turn, 2, target)
            
            else:  # Bottom-left diagonal
                if turn:
                    return 1 + max(dfs(row + 1, col - 1, turn, 3, target), 
                                   dfs(row - 1, col - 1, False, 0, target))
                return 1 + dfs(row + 1, col - 1, turn, 3, target)

        longest_v = 0  # Variable to store the longest V-diagonal length
        
        # Iterate through the grid to find starting points (cells with value 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Start DFS in all four diagonal directions
                    longest_v = max(longest_v, 
                        1 + max(dfs(i - 1, j - 1, True, 0, 2),  # Top-left
                                dfs(i - 1, j + 1, True, 1, 2),  # Top-right
                                dfs(i + 1, j + 1, True, 2, 2),  # Bottom-right
                                dfs(i + 1, j - 1, True, 3, 2))) # Bottom-left
        
        return longest_v

        
                       


