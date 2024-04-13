'''
Leetcode 525 Contiguous Array
 
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
        Input: nums = [0,1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
        Input: nums = [0,1,0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
         

Constraints:
        1 <= nums.length <= 105
        nums[i] is either 0 or 1.

'''

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map to store the first occurrence of each prefix sum
        sum_index_map = {0: -1}  # Initialize with sum 0 at index -1 to handle cases where subarray starts from index 0
        max_length = 0
        prefix_sum = 0

        for i in range(len(nums)):
            # Update prefix sum, treating 0 as -1
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            # Check if this prefix sum has been seen before
            if prefix_sum in sum_index_map:
                # Calculate the length of the subarray
                subarray_length = i - sum_index_map[prefix_sum]
                # Update the maximum length found
                max_length = max(max_length, subarray_length)
            else:
                # Store the first occurrence of this prefix sum
                sum_index_map[prefix_sum] = i

        return max_length
