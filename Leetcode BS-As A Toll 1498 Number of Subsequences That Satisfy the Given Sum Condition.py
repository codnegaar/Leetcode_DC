'''

Leetcode BS-As A Toll 1498 Number of Subsequences That Satisfy the Given Sum Condition

You are given an array of integer nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to the target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
        Input: nums = [3,5,6,7], target = 9
        Output: 4
        Explanation: 4 subsequences satisfy the condition.
        [3] -> Min value + max value <= target (3 + 3 <= 9)
        [3,5] -> (3 + 5 <= 9)
        [3,5,6] -> (3 + 6 <= 9)
        [3,6] -> (3 + 6 <= 9)

Example 2:
        Input: nums = [3,3,6,8], target = 10
        Output: 6
        Explanation: 6 subsequences satisfy the condition. (nums can have repeated numbers).
        [3] , [3], [3,3], [3,6], [3,6], [3,3,6]

Example 3:
        Input: nums = [2,3,3,4,6,7], target = 12
        Output: 61
        Explanation: There are 63 non-empty subsequences, and two of them do not satisfy the condition ([6,7], [7]).
        Number of valid subsequences (63 - 2 = 61).
         

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 106
        1 <= target <= 106

'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        mod = 10 ** 9 + 7
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += pow(2, right - left, mod)
                left += 1
        
        return count % mod






