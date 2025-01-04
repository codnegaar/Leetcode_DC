'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
      Input: n = 4
      Output: 2
      Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
      Input: n = 1
      Output: 1
Constraints:
      1 <= n <= 9

'''
class Solution:
  def totalNQueens(self, n: int) -> int:
    ans = 0
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def dfs(i: int) -> None:
      nonlocal ans
      if i == n:
        ans += 1
        return

      for j in range(n):
        if cols[j] or diag1[i + j] or diag2[j - i + n - 1]:
          continue
        cols[j] = diag1[i + j] = diag2[j - i + n - 1] = True
        dfs(i + 1)
        cols[j] = diag1[i + j] = diag2[j - i + n - 1] = False

    dfs(0)
    return ans

# solution 2
class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Calculate the number of distinct solutions for placing N queens on an 
        N x N chessboard such that no two queens threaten each other.

        Parameters:
        n (int): The number of queens and the size of the chessboard.

        Returns:
        int: The number of valid ways to place the queens.
        """
        # Initialize variables to store the count of solutions and sets for
        # columns and diagonals to track attacked positions
        self.res = 0
        self.n = n
        self.col = set()   # Track columns that are occupied
        self.pos_diag = set()  # Track positive diagonals (r + c)
        self.neg_diag = set()  # Track negative diagonals (r - c)

        def backtrack(row: int):
            """
            Backtracking function to explore each possible position for 
            queens in a row.

            Parameters:
            row (int): The current row to place the queen.
            """
            # If we have placed queens in all rows, increment the result count
            if row == self.n:
                self.res += 1
                return
            
            # Try placing a queen in every column for the current row
            for col in range(self.n):
                # Skip if the column or diagonals are under attack
                if col in self.col or (row + col) in self.pos_diag or (row - col) in self.neg_diag:
                    continue

                # Mark the column and diagonals as occupied
                self.col.add(col)
                self.pos_diag.add(row + col)
                self.neg_diag.add(row - col)

                # Move to the next row
                backtrack(row + 1)

                # Backtrack: unmark the current position
                self.col.remove(col)
                self.pos_diag.remove(row + col)
                self.neg_diag.remove(row - col)

        # Start the backtracking process from the first row
        backtrack(0)

        # Return the total number of valid solutions
        return self.res


# Unit Test

def test_totalNQueens():
    sol = Solution()

    # Test case 1: 4 Queens problem, known result is 2 solutions
    assert sol.totalNQueens(4) == 2, "Test case 1 failed"

    # Test case 2: 8 Queens problem, known result is 92 solutions
    assert sol.totalNQueens(8) == 92, "Test case 2 failed"

    # Test case 3: 1 Queen problem, only 1 solution
    assert sol.totalNQueens(1) == 1, "Test case 3 failed"

    # Test case 4: 2 Queens problem, no valid solutions
    assert sol.totalNQueens(2) == 0, "Test case 4 failed"

    # Test case 5: 3 Queens problem, no valid solutions
    assert sol.totalNQueens(3) == 0, "Test case 5 failed"

    # Test case 6: 5 Queens problem, known result is 10 solutions
    assert sol.totalNQueens(5) == 10, "Test case 6 failed"

    # Test case 7: 6 Queens problem, known result is 4 solutions
    assert sol.totalNQueens(6) == 4, "Test case 7 failed"

    print("All test cases passed!")

# Run the unit test
test_totalNQueens()

