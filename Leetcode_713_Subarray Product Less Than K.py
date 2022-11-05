'''
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements 
in the subarray is strictly less than k. 

Example 1:
        Input: nums = [10,5,2,6], k = 100
        Output: 8
        Explanation: The 8 subarrays that have product less than 100 are:
        [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
        Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
        
Example 2:
        Input: nums = [1,2,3], k = 0
        Output: 0

Constraints:
          1 <= nums.length <= 3 * 104
          1 <= nums[i] <= 1000
          0 <= k <= 106


'''

# First Solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans
      
      
# Secind solution

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans
        

