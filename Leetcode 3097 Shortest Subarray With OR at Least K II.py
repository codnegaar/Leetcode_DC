'''
Leetcode 3097 Shortest Subarray With OR at Least K II

You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty 
subarray of nums, or return -1 if no special subarray exists.

 

Example 1:
        Input: nums = [1,2,3], k = 2
        Output: 1
        Explanation:
                The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
        Input: nums = [2,1,8], k = 10
        Output: 3
        Explanation:
                The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
        Input: nums = [1,2], k = 0
        Output: 1
        Explanation:
                The subarray [1] has OR value of 1. Hence, we return 1. 

Constraints:
1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109

'''
from typing import List
from collections import Counter
from math import inf

class Solution:
    def minimumSubarrayLength(self, a: List[int], k: int) -> int:
        """
        Finds the minimum length of a subarray such that the bitwise OR of the 
        elements in that subarray is greater than or equal to a target sum `k`.

        Parameters:
        - a: List[int] - List of integers.
        - k: int - The target OR value to achieve with the subarray.

        Returns:
        - int: Minimum length of such subarray, or -1 if not possible.
        """
        res = inf  # Initialize result as infinity (for minimum search)
        bit_count = Counter()  # Tracks the frequency of bits set across the window
        left = 0  # Left pointer of the sliding window
        
        # Right pointer moves across each element in the list
        for right in range(len(a)):
            # Update bit count based on the bits set in a[right]
            bit_count.update(i for i, c in enumerate(bin(a[right])[:1:-1]) if c == '1')
            
            # Shrink the window from the left if the current OR is at least k
            while left <= right and sum(1 << i for i, f in bit_count.items() if f > 0) >= k:
                # Update the result with the current window size
                res = min(res, right - left + 1)
                
                # Remove the bits of a[left] as we move the left pointer
                bit_count.update({i: -1 for i, c in enumerate(bin(a[left])[:1:-1]) if c == '1'})
                left += 1

        # Return -1 if no valid subarray found; otherwise, return the minimum length
        return -1 if res == inf else res
