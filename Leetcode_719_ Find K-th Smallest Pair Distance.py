'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
   Show Hint #1  
Python3	
     def possible(guess, nums, k):
            count, left = 0, 0
            for right, num in enumerate(nums):
                while num-nums[left] > guess:
                    left += 1
                count += right-left
            return count >= k

        nums.sort()
        left, right = 0, nums[-1]-nums[0]+1
        while left < right:
            mid = left + (right-left)/2
            if possible(mid, nums, k):
                right = mid
            else:
                left = mid+1
        return left
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def count(arr, val):
            res = 0
            for i in range(len(arr)):
                res += bisect.bisect_right(arr, arr[i] + val, lo=i) - i - 1
            return res

        nums.sort()
        lo = min(abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1))
        hi = abs(nums[0] - nums[~0])
        while lo < hi:
            mid = (lo + hi) // 2
            if count(nums, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
