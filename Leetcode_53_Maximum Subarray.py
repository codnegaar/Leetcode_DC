'''
53. Maximum Subarray
 
Given an integer array nums, find the 
subarray
 which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    # dp[i] := max sum subarray ending w// i.
    dp = [0] * len(nums)

    dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)


# Second solution
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

        :param nums: List[int] - A list of integers representing the array.
        :return: int - The maximum sum of a contiguous subarray.
        """
        # Initialize the result with the first element and a total sum as 0.
        max_sum = nums[0]
        current_sum = 0

        # Iterate through each number in the array.
        for num in nums:
            # Reset the current sum to 0 if it is negative.
            if current_sum < 0:
                current_sum = 0
            
            # Add the current number to the current sum.
            current_sum += num
            
            # Update the maximum sum if the current sum exceeds it.
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Unit Tests
def test_maxSubArray():
    sol = Solution()

    # Test case 1: Example with mixed positive and negative numbers
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert sol.maxSubArray(nums1) == 6, "Test Case 1 Failed"

    # Test case 2: All negative numbers
    nums2 = [-1, -2, -3, -4]
    assert sol.maxSubArray(nums2) == -1, "Test Case 2 Failed"

    # Test case 3: All positive numbers
    nums3 = [1, 2, 3, 4, 5]
    assert sol.maxSubArray(nums3) == 15, "Test Case 3 Failed"

    # Test case 4: Single element array
    nums4 = [10]
    assert sol.maxSubArray(nums4) == 10, "Test Case 4 Failed"

    # Test case 5: Mixed numbers with maximum at the end
    nums5 = [1, 2, -1, 2, -3, 4]
    assert sol.maxSubArray(nums5) == 5, "Test Case 5 Failed"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run unit tests
    test_maxSubArray()

