'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        all_numbers_set = set(range(1, length_nums + 1))

        for num in nums:
            if num in all_numbers_set:
                all_numbers_set.remove(num)

        return list(all_numbers_set)
