'''
Leetcode 628 Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
      Input: nums = [1,2,3]
      Output: 6

Example 2:
        Input: nums = [1,2,3,4]
        Output: 24

Example 3:
        Input: nums = [-1,-2,-3]
        Output: -6 

Constraints:
        3 <= nums.length <= 104
        -1000 <= nums[i] <= 1000
'''


class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        A.sort()
        
        return max(
            A[-1] * A[-2] * A[-3],
            A[-1] * A[0] * A[1]
        )
