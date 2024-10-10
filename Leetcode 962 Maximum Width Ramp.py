'''
Leetcode 962 Maximum Width Ramp

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

Example 1:
        Input: nums = [6,0,8,2,1,5]
        Output: 4
        Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:
        Input: nums = [9,8,1,0,1,9,4,0,4,1]
        Output: 7
        Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
         
Constraints:
        2 <= nums.length <= 5 * 104
        0 <= nums[i] <= 5 * 104
'''
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        # Step 1: Build a decreasing stack of indices
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        maxWidth = 0
        
        # Step 2: Traverse from the end and find maximum width ramp
        # We start from the rightmost end (to potentially maximize j - stack[-1])
        for j in range(n - 1, -1, -1):
            # Early exit: No need to check further if stack is empty
            while stack and nums[stack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - stack.pop())
                # Early exit: If the best possible width is already found
                if not stack or j <= stack[-1]:
                    break
        
        return maxWidth
