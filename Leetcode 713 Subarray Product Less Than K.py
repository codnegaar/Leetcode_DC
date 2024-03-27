'''
Leetcode 713 Subarray Product Less Than K

Given an array of integer nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 
Example 1:
        Input: nums = [10,5,2,6], k = 100
        Output: 8
        Explanation: The 8 subarrays that have product less than 100 are:
        [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
        Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
        Input: nums = [1,2,3], k = 0
        Output: 0
 
Constraints:
        1 <= nums.length <= 3 * 104
        1 <= nums[i] <= 1000
        0 <= k <= 106

'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left, right, product, count = 0, 0, 1, 0
        n = len(nums)

        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1

        return count


# Second Solution
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """Count the number of contiguous subarrays where the product of all elements is less than k."""
        if k <= 1:
            return 0

        start, end, product, count = 0, 0, 1, 0
        length = len(nums)

        while end < length:
            product *= nums[end]
            # Shrink the window from the left if the product is equal to or greater than k
            while product >= k and start <= end:
                product //= nums[start]
                start += 1
            # Count subarrays ending with nums[end]
            count += end - start + 1
            end += 1

        return count
