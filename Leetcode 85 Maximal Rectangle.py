'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
        Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        Output: 6
        Explanation: The maximal rectangle is shown in the above picture.
        
Example 2:
        Input: matrix = [["0"]]
        Output: 0
        
Example 3:
        Input: matrix = [["1"]]
        Output: 1
 
Constraints:
        rows == matrix.length
        cols == matrix[i].length
        1 <= row, cols <= 200

'''
class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0

    ans = 0
    hist = [0] * len(matrix[0])

    def largestRectangleArea(heights: List[int]) -> int:
      ans = 0
      stack = []

      for i in range(len(heights) + 1):
        while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
          h = heights[stack.pop()]
          w = i - stack[-1] - 1 if stack else i
          ans = max(ans, h * w)
        stack.append(i)

      return ans

    for row in matrix:
      for i, num in enumerate(row):
        hist[i] = 0 if num == '0' else hist[i] + 1
      ans = max(ans, largestRectangleArea(hist))

    return ans
