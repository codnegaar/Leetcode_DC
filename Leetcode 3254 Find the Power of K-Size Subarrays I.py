'''
Leetcode 3254 Find the Power of K-Size Subarrays I

You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
        Its maximum element if all of its elements are consecutive and sorted in ascending order.
        -1 otherwise. You need to find the power of all subarrays of nums of size k.
         Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
        Input: nums = [1,2,3,4,3,2,5], k = 3        
        Output: [3,4,-1,-1,-1]        
        Explanation:
                    There are 5 subarrays of nums of size 3:
                            [1, 2, 3] with the maximum element 3.
                            [2, 3, 4] with the maximum element 4.
                            [3, 4, 3] whose elements are not consecutive.
                            [4, 3, 2] whose elements are not sorted.
                            [3, 2, 5] whose elements are not consecutive.

Example 2:
        Input: nums = [2,2,2,2,2], k = 4        
        Output: [-1,-1]   

Example 3:        
        Input: nums = [3,2,3,2,3,2], k = 2        
        Output: [-1,3,-1,3,-1]

 

Constraints:
        1 <= n == nums.length <= 500
        1 <= nums[i] <= 105
        1 <= k <= n

'''
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        This function returns an array representing the last element of every consecutive subsequence of length 'k'.
        
        Parameters:
        nums (List[int]): A list of integers.
        k (int): The length of the consecutive subsequence to look for.
        
        Returns:
        List[int]: A list where each element is the last element of a consecutive subsequence of length 'k'.
        """
        n = len(nums)
        
        # Edge case: if the list has only one element or k is 1, return the original list
        if n == 1 or k == 1:
            return nums
        
        ans = [-1] * (n - k + 1)  # Initialize result array with -1 values
        consecutive_length = 1  # Length of current consecutive sequence
        
        # Iterate over the list to find consecutive sequences of length 'k'
        for right in range(1, n):
            # If current element is 1 greater than previous, increase the consecutive length
            if nums[right] == nums[right - 1] + 1:
                consecutive_length += 1
            else:
                consecutive_length = 1  # Reset consecutive length if the sequence breaks
            
            # If we have a consecutive sequence of at least length 'k', update the result
            if consecutive_length >= k:
                ans[right - k + 1] = nums[right]
        
        return ans

# Example Usage
# sol = Solution()
# print(sol.resultsArray([1, 2, 3, 4, 5], 3))  # Output: [3, 4, 5]
