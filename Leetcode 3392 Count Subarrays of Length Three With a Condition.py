'''

Leetcode 3392 Count Subarrays of Length Three With a Condition

Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

Example 1:
        Input: nums = [1,2,1,4,1]
        Output: 1
        Explanation:Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:
        Input: nums = [1,1,1]
        Output: 0
        Explanation:[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

Constraints:
          3 <= nums.length <= 100
          -100 <= nums[i] <= 100

'''
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Counts the number of subarrays where the middle element is even,
        and half of the middle element equals the sum of its neighboring elements.

        Parameters:
        nums (List[int]): List of integers to check.

        Returns:
        int: Total number of qualifying subarrays.
        """
        count = 0

        # Iterate through the array, excluding the first and last elements
        for i in range(1, len(nums) - 1):
            # Check if the middle element is even
            if nums[i] % 2 == 0:
                # Check if half of the middle element equals the sum of neighbors
                if nums[i] // 2 == nums[i - 1] + nums[i + 1]:
                    count += 1

        return count

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 6, 2, 4, 2, 8, 3]
    result = solution.countSubarrays(nums)
    print(f"Total qualifying subarrays: {result}")





