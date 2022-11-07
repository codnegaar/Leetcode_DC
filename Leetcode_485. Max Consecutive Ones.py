'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
        Input: nums = [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
        Input: nums = [1,0,1,1,0,1]
        Output: 2
Constraints:

        1 <= nums.length <= 105
        nums[i] is either 0 or 1.
        
 Hint #1  
You need to think about two things as far as any window is concerned. One is the starting point for the window. 
How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window.
How do you detect the ending point for an existing window? If you figure these two things out, you will be able to
detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count_ones = 0         # initialize count
        n = len(nums)     # inumber of item in list
        Max_ones = 0        # initialize max

        for i in range(0, n):
            if (nums[i] == 0):
                count_ones = 0     # Reset the count
            else:                
                count_ones += 1   # increase count
                Max_ones = max(Max_ones, count_ones)

        return Max_ones
 
