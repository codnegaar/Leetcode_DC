'''
59. Spiral Matrix II
 
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20

'''
class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    ans = [[0] * n for _ in range(n)]
    count = 1

    for min in range(n // 2):
      max = n - min - 1
      for i in range(min, max):
        ans[min][i] = count
        count += 1
      for i in range(min, max):
        ans[i][max] = count
        count += 1
      for i in range(max, min, -1):
        ans[max][i] = count
        count += 1
      for i in range(max, min, -1):
        ans[i][min] = count
        count += 1

    if n & 1:
      ans[n // 2][n // 2] = count

    return ans
