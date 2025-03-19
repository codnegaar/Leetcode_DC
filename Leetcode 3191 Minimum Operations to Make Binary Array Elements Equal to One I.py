'''
Leetcode 3191 Minimum Operations to Make Binary Array Elements Equal to One I

You are given a binary array nums.
You can do the following operation on the array any number of times (possibly zero):
        Choose any 3 consecutive elements from the array and flip all of them.
        Flipping an element means changing its value from 0 to 1, and from 1 to 0.
        Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

Example 1:
        Input: nums = [0,1,1,1,0,0]
        Output: 3
        Explanation:
                We can do the following operations:
                Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
                Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
                Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

Example 2:
        Input: nums = [0,1,1,1]
        Output: -1
        Explanation:
                It is impossible to make all elements equal to 1. 

Constraints:
        3 <= nums.length <= 105
        0 <= nums[i] <= 1

'''

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Finds the minimum number of operations required to convert all elements of nums to 1.
        Each operation allows flipping at most the next 3 consecutive elements.

        Parameters:
        nums (List[int]): A list of integers (0s and 1s).

        Returns:
        int: The minimum number of operations needed, or -1 if it's not possible.
        """

        n = len(nums)  # Get the length of the list
        count = 0  # Counter for the number of operations
        i = 0  # Pointer to traverse the list

        while i < n:
            if nums[i] == 0:  # If current element is 0, flip the next 3 elements
                count += 1  # Increment operation count
                
                if i + 2 >= n:  # If there aren't enough elements left to flip, return -1
                    return -1
                
                # Flip the next 3 elements
                for j in range(i, i + 3):
                    nums[j] = 1 - nums[j]

            i += 1  # Move to the next element
        
        return count if sum(nums) == n else -1  # Ensure all elements are 1 before returning
