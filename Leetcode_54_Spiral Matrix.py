'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
      Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
      Output: [1,2,3,6,9,8,7,4,5]
      
Example 2:
      Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
      Output: [1,2,3,4,8,12,11,10,9,5,6,7] 

Constraints:
      m == matrix.length
      n == matrix[i].length
      1 <= m, n <= 10
      -100 <= matrix[i][j] <= 100
'''

# first solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
      
      
  # second solution
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix:
      return []

    m = len(matrix)
    n = len(matrix[0])
    ans = []
    r1 = 0
    c1 = 0
    r2 = m - 1
    c2 = n - 1

    # Repeatedly add matrix[r1..r2][c1..c2] to ans
    while len(ans) < m * n:
      j = c1
      while j <= c2 and len(ans) < m * n:
        ans.append(matrix[r1][j])
        j += 1
      i = r1 + 1
      while i <= r2 - 1 and len(ans) < m * n:
        ans.append(matrix[i][c2])
        i += 1
      j = c2
      while j >= c1 and len(ans) < m * n:
        ans.append(matrix[r2][j])
        j -= 1
      i = r2 - 1
      while i >= r1 + 1 and len(ans) < m * n:
        ans.append(matrix[i][c1])
        i -= 1
      r1 += 1
      c1 += 1
      r2 -= 1
      c2 -= 1

    return ans
