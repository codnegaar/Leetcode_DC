'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
        
Example 2:
        Input: n = 1
        Output: [["Q"]]
        
Constraints:
        1 <= n <= 9

'''
class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    ans = []
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def dfs(i: int, board: List[int]) -> None:
      if i == n:
        ans.append(board)
        return

      for j in range(n):
        if cols[j] or diag1[i + j] or diag2[j - i + n - 1]:
          continue
        cols[j] = diag1[i + j] = diag2[j - i + n - 1] = True
        dfs(i + 1, board + ['.' * j + 'Q' + '.' * (n - j - 1)])
        cols[j] = diag1[i + j] = diag2[j - i + n - 1] = False

    dfs(0, [])
    return and


# Second solution:
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solves the N-Queens problem and returns all possible solutions.

        Parameters:
        n (int): The size of the chessboard (n x n) and number of queens.

        Returns:
        List[List[str]]: A list of valid board configurations, where each board is represented as a list of strings.
        """
        solutions = []  # Stores all valid board configurations
        cols = [False] * n  # Tracks occupied columns
        diag1 = [False] * (2 * n - 1)  # Tracks occupied diagonals (\ direction)
        diag2 = [False] * (2 * n - 1)  # Tracks occupied diagonals (/ direction)

        def backtrack(row: int, board: List[str]) -> None:
            """
            Backtracking function to place queens row by row.

            Parameters:
            row (int): The current row index where we are placing a queen.
            board (List[str]): The current board configuration.
            """
            # If all queens are placed successfully, store the solution
            if row == n:
                solutions.append(board[:])  # Store a copy of the board
                return

            for col in range(n):
                # Check if the column or diagonals are already occupied
                if cols[col] or diag1[row + col] or diag2[col - row + n - 1]:
                    continue

                # Place the queen
                cols[col] = diag1[row + col] = diag2[col - row + n - 1] = True
                board.append('.' * col + 'Q' + '.' * (n - col - 1))  # Construct row

                # Recur to place next queen
                backtrack(row + 1, board)

                # Backtrack: Remove the last queen placed
                board.pop()
                cols[col] = diag1[row + col] = diag2[col - row + n - 1] = False

        # Start backtracking from row 0
        backtrack(0, [])
        return solutions

# Example Usage
solution = Solution()
n = 4
result = solution.solveNQueens(n)
for i, board in enumerate(result):
    print(f"Solution {i + 1}:")
    for row in board:
        print(row)
    print()

