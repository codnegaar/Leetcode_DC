'''

Leetcode 861 Score After Flipping Matrix

You are given an m x n binary matrix grid.
A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:
        Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
        Output: 39
        Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:        
        Input: grid = [[0]]
        Output: 1
 

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 20
        grid[i][j] is either 0 or 1.
'''

'''

Solution description:

The Python class you've provided implements an algorithm to maximize the "score" of a binary matrix by flipping rows and columns. 
The score of a matrix is calculated by interpreting each row of the matrix as a binary number and then summing these values. 
To maximize this score, the idea is to ensure the most significant bit of each row (the leftmost bit) is 1, and then to maximize the number of 1s in each column.

Here's a breakdown and improvement of your existing code:

Row Flips: First, ensure the most significant bit of each row is 1. If it's not, flip the entire row.
Column Flips: For the rest of the columns, flip the column if doing so will result in more 1s than 0s in that column.
Code Clarity and Efficiency: Your current approach is correct, but we can make it clearer and more Pythonic.
Here's the improved version of your code:
Key Changes:
Column Looping: Directly incorporated the concept of checking if the first column is 1 and then adding up the 1s or their flipped counterparts, simplifying the logic.
Count Calculation: Directly calculated the ones_count based on the status of the first column in the row, avoiding unnecessary row flips and simplifying the logic.
Commenting and Readability: Added comments to make the logic clearer for each major step.

'''


from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # Initialize the result with all 1s in the most significant bit position
        result = (1 << (m - 1)) * n

        # Iterate through columns starting from the second one
        for j in range(1, m):
            val = 1 << (m - 1 - j)  # value of the current bit position
            ones_count = 0

            for i in range(n):
                # Count 1s as they are if the first column is 1, otherwise count as flipped
                if grid[i][0] == 1:
                    ones_count += grid[i][j]
                else:
                    ones_count += 1 - grid[i][j]

            # Maximize the number of 1s in the current column
            ones_count = max(ones_count, n - ones_count)
            result += ones_count * val

        return result
