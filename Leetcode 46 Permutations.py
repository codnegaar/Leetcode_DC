'''
Leetcode 46 Permutations.py

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]
 

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

'''
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    used = [False] * len(nums)

    def dfs(path: List[int]) -> None:
      if len(path) == len(nums):
        ans.append(path.copy())
        return

      for i, num in enumerate(nums):
        if used[i]:
          continue
        used[i] = True
        path.append(num)
        dfs(path)
        path.pop()
        used[i] = False

    dfs([])
    return ans

# Second Solution
from typing import List
from itertools import permutations
import unittest

class Solution:
    """
    Solution class for generating all permutations of a list of integers.

    Methods:
        permute(nums: List[int]) -> List[List[int]]:
            Returns all possible permutations of the input list.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all permutations of a given list using itertools.

        Args:
            nums (List[int]): List of integers to permute.

        Returns:
            List[List[int]]: A list containing all possible permutations.
        """
        # Use itertools.permutations for efficient and concise generation of permutations
        return list(permutations(nums))

# Example usage
solution = Solution()
nums = [1, 2, 3]
result = solution.permute(nums)
print("Generated permutations:", result)


# Second solution
from typing import List, Set

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of a given list of numbers.

        Parameters:
        nums (List[int]): List of distinct integers.

        Returns:
        List[List[int]]: List of all possible permutations.
        """
        res = []  # Stores all permutations

        def backtrack(curr: List[int], used_indices: Set[int]):
            """
            Backtracking function to generate permutations.

            Parameters:
            curr (List[int]): Current permutation being built.
            used_indices (Set[int]): Indices of numbers already used.
            """
            # If the current permutation has all numbers, add it to results
            if len(curr) == len(nums):
                res.append(curr[:])  # Append a copy of curr
                return
            
            for i in range(len(nums)):
                if i not in used_indices:
                    # Choose the number at index i
                    used_indices.add(i)
                    curr.append(nums[i])

                    # Recur with the updated list
                    backtrack(curr, used_indices)

                    # Backtrack - remove the last number to explore other choices
                    curr.pop()
                    used_indices.remove(i)

        backtrack([], set())  # Start backtracking with an empty list and set
        return res

# Example Usage
solution = Solution()
nums = [1, 2, 3]
result = solution.permute(nums)
print(f"All permutations of {nums}: {result}")
