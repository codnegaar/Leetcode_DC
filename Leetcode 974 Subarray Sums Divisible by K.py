'''

Leetcode 974 Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.
 

Example 1:
        Input: nums = [4,5,0,-2,-3,1], k = 5
        Output: 7
        Explanation: There are 7 subarrays with a sum divisible by k = 5:
        [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
        Input: nums = [5], k = 9
        Output: 0
 

Constraints:
        1 <= nums.length <= 3 * 104
        -104 <= nums[i] <= 104
        2 <= k <= 104

'''

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of prefix sums modulo k
        prefix_count = {0: 1}
        count = 0
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            mod = curr_sum % k
            
            # Handle negative mods by adjusting the value to be within the range [0, k-1]
            if mod < 0:
                mod += k
            
            # If mod is already in the dictionary, it means we have found some subarrays that are divisible by k
            if mod in prefix_count:
                count += prefix_count[mod]
                prefix_count[mod] += 1
            else:
                prefix_count[mod] = 1
        
        return count
