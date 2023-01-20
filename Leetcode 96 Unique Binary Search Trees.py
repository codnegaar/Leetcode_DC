'''


Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n. 

Example 1:
        Input: n = 3
        Output: 5
        
Example 2:
        Input: n = 1
        Output: 1

Constraints:
         1 <= n <= 19

'''
class Solution:
  def numTrees(self, n: int) -> int:
    # G[i] := # Of unique BST's that store values 1..i
    G = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
      for j in range(i):
        G[i] += G[j] * G[i - j - 1]

    return G[n]
