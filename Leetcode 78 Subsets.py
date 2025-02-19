'''
78 Subsets
 
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
      ans.append(path)

      for i in range(s, len(nums)):
        dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return ans

# second solution
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (power set) of the given list of numbers.

        Parameters:
        nums (List[int]): List of unique integers.

        Returns:
        List[List[int]]: List containing all subsets.
        """
        result = []  # Stores all subsets

        def backtrack(start: int, path: List[int]) -> None:
            """
            Backtracking function to generate subsets.

            Parameters:
            start (int): Current index in the input list.
            path (List[int]): Current subset being constructed.
            """
            result.append(path[:])  # Store a copy of the current subset

            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])

                # Recur to add more elements to the subset
                backtrack(i + 1, path)

                # Backtrack: Remove last element to explore other possibilities
                path.pop()

        backtrack(0, [])
        return result

# Example Usage
solution = Solution()

# Test cases
test_cases = [
    [1, 2, 3],   # Expected: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    [0],         # Expected: [[], [0]]
    []           # Expected: [[]]
]

for nums in test_cases:
    print(f"Subsets of {nums}: {solution.subsets(nums)}")



