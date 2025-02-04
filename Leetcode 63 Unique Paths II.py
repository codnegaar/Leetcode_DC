'''
63. Unique Paths II
 
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in the grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
     Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
     Output: 2
     Explanation: There is one obstacle in the middle of the 3x3 grid above.
     There are two ways to reach the bottom-right corner:
     1. Right -> Right -> Down -> Down
     2. Down -> Down -> Right -> Right

Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1 

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
'''

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    # dp[i][j] := unique paths from (0, 0) to (i - 1, j - 1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][1] = 1  # Can also set dp[1][0] = 1

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if obstacleGrid[i - 1][j - 1] == 0:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]

# Second Solution
from typing import List
import unittest

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Finds the number of unique paths from the top-left corner to the bottom-right corner 
        of a grid while avoiding obstacles.

        Parameters:
        obstacleGrid (List[List[int]]): A 2D list where 0 represents an open space 
                                        and 1 represents an obstacle.

        Returns:
        int: The total number of unique paths to reach the bottom-right corner.
        """
        # Edge case: If the starting cell is blocked, no paths exist.
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols  # DP array to store ways to reach each cell in the current row
        dp[0] = 1  # Start point has one way to be reached

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0  # If there's an obstacle, no paths can go through
                elif c > 0:
                    dp[c] += dp[c - 1]  # Paths from the left cell

        return dp[cols - 1]  # The last cell contains the total unique paths


# Unit Tests
class TestUniquePathsWithObstacles(unittest.TestCase):
    def test_examples(self):
        solution = Solution()
        
        # Test Case 1: Standard grid with obstacles
        self.assertEqual(solution.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]), 2)  # Two valid paths avoiding the obstacle

        # Test Case 2: No obstacles, standard pathfinding
        self.assertEqual(solution.uniquePathsWithObstacles([
            [0, 0, 0],
