'''
Leetcode 862 Shortest Subarray with Sum at Least K
 
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
A subarray is a contiguous part of an array. 

Example 1:
    Input: nums = [1], k = 1
    Output: 1

Example 2:
    Input: nums = [1,2], k = 4
    Output: -1

Example 3:
    Input: nums = [2,-1,2], k = 3
    Output: 3
 
Constraints:
    1 <= nums.length <= 105
    -105 <= nums[i] <= 105
    1 <= k <= 109

'''

from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        Finds the length of the shortest subarray with a sum of at least k.

        Parameters:
        nums (List[int]): List of integers representing the array.
        k (int): The target sum.

        Returns:
        int: The length of the shortest subarray with a sum of at least k, or -1 if no such subarray exists.
        """
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        # Compute prefix sums
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        dq = deque()
        min_length = float('inf')

        # Process prefix sums
        for i in range(n + 1):
            # Maintain the deque to find the shortest subarray
            while dq and prefix_sums[i] - prefix_sums[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())

            # Maintain the deque to keep prefix sums in increasing order
            while dq and prefix_sums[i] <= prefix_sums[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_length if min_length != float('inf') else -1

        # Time complexity: O(n)
        # Space complexity: O(n)


