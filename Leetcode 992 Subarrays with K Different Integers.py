'''

Leetcode 992 Subarrays with K Different Integers

Given an integer array of nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:
        Input: nums = [1,2,1,2,3], k = 2
        Output: 7
        Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
        Input: nums = [1,2,1,3,4], k = 3
        Output: 3
        Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
         

Constraints:
        1 <= nums.length <= 2 * 104
        1 <= nums[i], k <= nums.length


approach:
        1- Dictionary for Frequency Count: Instead of a fixed-size list, a dictionary is used to count the frequency of elements. This adapts to any range of element values without needing to know the maximum element value upfront.
        2- Simplified Control Flow: The if k == 1 condition is removed, as the main logic correctly handles this case without special treatment.
        3- Directly Return Result: Computes and returns the final result in one line, removing the need for an explicit conditional check outside the helper function.
        4- Using Python's Dictionary: Utilizing dict.get for frequency lookup simplifies the frequency update logic.

'''
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            count = left = 0
            freq = {}
            for right, value in enumerate(nums):
                freq[value] = freq.get(value, 0) + 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                count += right - left + 1
            return count
        
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)



