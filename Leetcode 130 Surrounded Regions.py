'''
130 Surrounded Regions 
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        Explanation: Notice that an 'O' should not be flipped if:
        - It is on the border, or
        - It is adjacent to an 'O' that should not be flipped.
        The bottom 'O' is on the border, so it is not flipped.
        The other three 'O' form a surrounded region, so they are flipped.

Example 2:
        Input: board = [["X"]]
        Output: [["X"]]
 

Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 200
        board[i][j] is 'X' or 'O'.
'''
class Solution:
  def solve(self, board: List[List[str]]) -> None:
      #Do not return anything, modify board in-place instead.
    if not board:
      return

    m = len(board)
    n = len(board[0])
    dirs = [0, 1, 0, -1, 0]
    q = collections.deque()

    for i in range(m):
      for j in range(n):
        if i * j == 0 or i == m - 1 or j == n - 1:
          if board[i][j] == 'O':
            q.append((i, j))
            board[i][j] = '*'

    # Mark grids that stretch from four sides with '*'
    while q:
      i, j = q.popleft()
      for k in range(4):
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if x < 0 or x == m or y < 0 or y == n:
          continue
        if board[x][y] != 'O':
          continue
        q.append((x, y))
        board[x][y] = '*'

    for row in board:
      for i, c in enumerate(row):
        row[i] = 'O' if c == '*' else 'X'
