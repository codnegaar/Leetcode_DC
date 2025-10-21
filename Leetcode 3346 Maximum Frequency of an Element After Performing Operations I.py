'''
Leetcode 3346 Maximum Frequency of an Element After Performing Operations I

You are given an integer array nums and two integers k and numOperations.
You must perform an operation numOperations times on nums, where in each operation you:
        Select an index i that was not selected in any previous operations.
        Add an integer in the range [-k, k] to nums[i].
        Return the maximum possible frequency of any element in nums after performing the operations. 

Example 1:
        Input: nums = [1,4,5], k = 1, numOperations = 2
        Output: 2
        Explanation: We can achieve a maximum frequency of two by:
        Adding 0 to nums[1]. nums becomes [1, 4, 5].
        Adding -1 to nums[2]. nums becomes [1, 4, 4].

Example 2:
        Input: nums = [5,11,20,20], k = 5, numOperations = 1
        Output: 2
        Explanation: We can achieve a maximum frequency of two by:
        Adding 0 to nums[1]. 

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 105
        0 <= k <= 105
        0 <= numOperations <= nums.length
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOps: int) -> int:
        maxVal = max(nums) + k + 2
        count = [0] * maxVal

        for v in nums:
            count[v] += 1

        for i in range(1, maxVal):
            count[i] += count[i - 1]

        res = 0
        for i in range(maxVal):
            left = max(0, i - k)
            right = min(maxVal - 1, i + k)
            total = count[right] - (count[left - 1] if left else 0)
            freq = count[i] - (count[i - 1] if i else 0)
            res = max(res, freq + min(numOps, total - freq))

        return res


