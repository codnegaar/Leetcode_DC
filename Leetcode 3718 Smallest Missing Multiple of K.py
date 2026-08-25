'''
Leetcode 3718 Smallest Missing Multiple of K

Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.

A multiple of k is any positive integer divisible by k.

 

Example 1:

Input: nums = [8,2,3,4,6], k = 2

Output: 10

Explanation:

The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

Example 2:

Input: nums = [1,4,7,10,15], k = 5

Output: 5

Explanation:

The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 100

'''

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hasQ, qMax=0, 0
        for x in nums:
            q, r=divmod(x, k)
            if r==0:
                hasQ|=(1<<q)
                qMax=max(q, qMax)
        for q in range(1, qMax+1):
            if (hasQ>>q)&1==0:
                return q*k
        return (qMax+1)*k
