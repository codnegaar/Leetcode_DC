'''
Leetcode 77 Combinations
 
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    Explanation: There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
    Explanation: There is 1 choose 1 = 1 total combination.
     

Constraints:
     1 <= n <= 20
     1 <= k <= n

'''
class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
      if len(path) == k:
        ans.append(path.copy())
        return

      for i in range(s, n + 1):
        path.append(i)
        dfs(i + 1, path)
        path.pop()

    dfs(1, [])
    return ans


# 2nd Solution
from typing import List
import itertools
import unittest

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Generate all combinations of k numbers from the range 1 to n.

        Args:
        n (int): The upper bound of the range (inclusive).
        k (int): The number of elements in each combination.

        Returns:
        List[List[int]]: A list of all possible combinations.
        """
        return list(itertools.combinations(range(1, n + 1), k))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combine(self):
        self.assertEqual(self.solution.combine(4, 2), [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
        self.assertEqual(self.solution.combine(3, 3), [(1, 2, 3)])
        self.assertEqual(self.solution.combine(5, 1), [(1,), (2,), (3,), (4,), (5,)])
        self.assertEqual(self.solution.combine(1, 1), [(1,)])
        self.assertEqual(self.solution.combine(0, 0), [])


if __name__ == "__main__":
    import sys
    unittest.main(argv=[sys.argv[0]], exit=False)

