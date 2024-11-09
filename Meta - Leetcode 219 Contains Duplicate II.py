'''

Meta - Leetcode 219 Contains Duplicate II
 
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
 

Constraints:
     1 <= nums.length <= 105
     -109 <= nums[i] <= 109
     0 <= k <= 105
'''
class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    seen = set()

    for i, num in enumerate(nums):
      if i > k:
        seen.remove(nums[i - k - 1])
      if num in seen:
        return True
      seen.add(num)

    return False
# Sliding windows

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # Set to maintain the sliding window of elements
        L = 0  # Left pointer to manage the window

        for R in range(len(nums)):
            # Ensure the window size does not exceed k
            if R - L > k:
                window.remove(nums[L])  # Remove the oldest element from the window
                L += 1  # Move the left pointer to the right
            
            # If the current element is already in the window, a duplicate is found
            if nums[R] in window:
                return True

            # Add the current element to the window
            window.add(nums[R])

        # If no duplicates found within the distance 'k', return False
        return False

# Example usage:
# sol = Solution()
# print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
