'''

Leetcode 3350 Adjacent Increasing Subarrays Detection II
 
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. 
Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:        
        Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
        The subarrays must be adjacent, meaning b = a + k.
        Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array. 

Example 1:
Input: nums = [2,5,7,8,9,2,3,4,3,1]
Output: 3
Explanation:
        The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
        The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
        These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

Example 2:
Input: nums = [1,2,3,4,4,4,4,5,6,7]
Output: 2
Explanation:
        The subarray starting at index 0 is [1, 2], which is strictly increasing.
        The subarray starting at index 2 is [3, 4], which is also strictly increasing.
        These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
         
Constraints:
        2 <= nums.length <= 2 * 105
        -109 <= nums[i] <= 109
'''
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        """
        Return the maximum k such that there exist two consecutive strictly
        increasing subarrays each of length at least k.

        Args:
            nums (list[int]): Input array of integers.

        Returns:
            int: The maximum k.

        Notes:
            - We track the current run length (curr), the previous run length (prev),
              and update the best answer at each step using:
                max(curr // 2, min(prev, curr))
              which captures both:
                • two subarrays inside one run  -> curr // 2
                • subarrays straddling a break -> min(prev, curr)
        """
        n = len(nums)
        if n <= 1:
            return 0

        curr = 1      # length of current increasing run
        prev = 0      # length of previous increasing run
        best = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            best = max(best, curr // 2, min(prev, curr))

        return best


# Tiny example
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 2, 3, 4]
    print(Solution().maxIncreasingSubarrays(arr))  # 3


