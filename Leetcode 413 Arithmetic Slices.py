'''
Leetcode 413 Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.
A subarray is a contiguous subsequence of the array.

Example 1:
        Input: nums = [1,2,3,4]
        Output: 3
        Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
        Input: nums = [1]
        Output: 0 

Constraints:
        1 <= nums.length <= 5000
        -1000 <= nums[i] <= 1000

'''
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Counts the number of arithmetic slices in an array.
        An arithmetic slice is a subarray of at least 3 elements
        where the difference between consecutive elements is the same.

        Parameters:
        A (List[int]): The input list of integers.

        Returns:
        int: Total number of arithmetic slices.
        """
        n = len(A)
        if n < 3:
            return 0  # Less than 3 elements can't form any slice
        
        dp = [0] * n  # dp[i] stores number of arithmetic slices ending at index i
        total = 0  # Total count of arithmetic slices

        for i in range(2, n):
            # Check if current 3 elements form an arithmetic sequence
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1  # Extend previous slices or start a new one
                total += dp[i]  # Add to total count

        return total

# Example usage
if __name__ == "__main__":
    solution = Solution()
    A = [1, 2, 3, 4, 6, 8, 10]
    result = solution.numberOfArithmeticSlices(A)
    print(f"Total number of arithmetic slices: {result}")
