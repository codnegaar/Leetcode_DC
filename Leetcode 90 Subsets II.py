'''
Given an integer array nums that may contain duplicates, return all possible subsets
 (the power set). The solution set must not contain duplicate subsets. Return the 
 solution in any order.

 Example 1:
        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        
Example 2:
        Input: nums = [0]
        Output: [[],[0]]
 
Constraints:
        1 <= nums.length <= 10
        -10 <= nums[i] <= 10
'''
class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
      ans.append(path)
      if s == len(nums):
        return

      for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i - 1]:
          continue
        dfs(i + 1, path + [nums[i]])

    nums.sort()
    dfs(0, [])
    return ans
