'''

Leetcode 3487 Maximum Unique Subarray Sum After Deletion

You are given an integer array nums.
You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:
All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray. 

Example 1:
        Input: nums = [1,2,3,4,5]
        Output: 15
        Explanation: Select the entire array without deleting any element to obtain the maximum sum.

Example 2:
        Input: nums = [1,1,0,1,1]
        Output: 1
        Explanation: Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

Example 3:
        Input: nums = [1,2,-1,-2,1,0,-1]
        Output: 3
        Explanation: Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

Constraints:
        1 <= nums.length <= 100
        -100 <= nums[i] <= 100
'''

from typing import List

class Solution:
    """
    A class that provides an algorithm to compute the maximum sum
    of unique positive integers from a given list.

    Methods:
        maxSum(nums: List[int]) -> int
            Returns the sum of all unique positive integers in the list.
            If all numbers are negative, returns the maximum number.
    """

    def maxSum(self, nums: List[int]) -> int:
        """
        Calculates the sum of all unique positive integers in the list.
        If all numbers are negative, returns the single largest number.

        Parameters:
            nums (List[int]): A list of integers (can include duplicates and negatives)

        Returns:
            int: The maximum possible sum of unique positive integers,
                 or the largest negative integer if no positives exist.
        """

        # If all numbers are negative, return the highest (least negative)
        if all(n < 0 for n in nums):
            return max(nums)

        # Use a set to eliminate duplicates and sum only positive values
        return sum(n for n in set(nums) if n > 0)
