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
