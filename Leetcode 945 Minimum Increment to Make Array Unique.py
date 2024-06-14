'''

Leetcode 945 Minimum Increment to Make Array Unique

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
        Input: nums = [1,2,2]
        Output: 1
        Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
        Input: nums = [3,2,1,2,1,7]
        Output: 6
        Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
        It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Constraints:        
        1 <= nums.length <= 105
        0 <= nums[i] <= 105

'''


from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Sort the input array to bring duplicate elements together
        nums.sort()
        
        # Variable to track the next unique value needed
        next_unique = 0
        
        # Variable to count the total increments needed
        total_increments = 0

        # Iterate through each number in the sorted list
        for num in nums:
            # Update next_unique to be the maximum of its current value or the current number
            next_unique = max(next_unique, num)
            
            # Increment the total number of moves by the difference between next_unique and num
            total_increments += next_unique - num
            
            # Move to the next possible unique number
            next_unique += 1
        
        return total_increments
