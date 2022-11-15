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
 
        
        
        
