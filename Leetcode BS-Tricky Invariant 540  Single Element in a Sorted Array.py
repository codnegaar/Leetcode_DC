'''
Leetcode BS-Tricky Invariant 540  Single Element in a Sorted Array
 
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
        Input: nums = [1,1,2,3,3,4,4,8,8]
        Output: 2

Example 2:
        Input: nums = [3,3,7,7,10,11,11]
        Output: 10

Constraints:
        1 <= nums.length <= 105
        0 <= nums[i] <= 105
'''

class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1
        while i < j:
            m = (i+j) // 2
            if m < j and arr[m] == arr[m+1]:
                m = m + 1
            if arr[m] != arr[m-1] and arr[m] != arr[m+1]:
                return arr[m]
            elif abs(m-i) % 2 == 0:
                j = m - 1
            else:
                i = m + 1 
        return arr[i]
