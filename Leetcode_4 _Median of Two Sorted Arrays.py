'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        
Example 2:
        Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
 Constraints:
        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -106 <= nums1[i], nums2[i] <= 106

'''

import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # if one of the arrays is empty, 
        # return the median of the other array
        if not nums1 or not nums2:
            nums = nums1 if nums1 else nums2
            length = len(nums)
            if length % 2 == 0:
                return (nums[length // 2] + nums[length // 2 - 1]) / 2
            else:
                return nums[length // 2]
        
        target = (len(nums1) + len(nums2)) // 2
        
        # Find the item with index len(C) // 2,
        # where C is a virtual sorted array by combining A and B
        def helper(low, high, A, B):
            if low > high:
                return None
            else:
                x = low + (high - low) // 2
                y = target - x
                # len(B) cannot be 0, since we have already test this case
                if y == len(B):
                    if B[y - 1] > A[x]:
                        return helper(x + 1, high, A, B)
                elif y == 0:
                    if B[y] < A[x]:
                        return helper(low, x - 1, A, B)
                # 0 < y < len(B)
                else:
                    if B[y - 1] > A[x]:
                        return helper(x + 1, high, A, B)
                    if B[y] < A[x]:
                        return helper(low, x - 1, A, B)    
                # found one candidate for the median value
                # now return the actual median value
                if (len(A) + len(B)) % 2 == 1:
                    return A[x]
                else:
                # the length of the virtual sorted array C is even
                # thus we need to find another item with index `(len(A) + len(B)) // 2 - 1`
                    # to compute the median value
                    # this item should be the larger one of A[x - 1] and B[y - 1]
                    the_other = float('-inf')
                    if x - 1 >= 0:
                        the_other = max(A[x - 1], the_other)
                    if y - 1 >= 0:
                        the_other = max(B[y - 1], the_other)
                    return (A[x] + the_other) / 2    
                        
        res = helper(max(0, target - len(nums2)), min(len(nums1) - 1, target), nums1, nums2)
        if res:
            return res
        return helper(max(0, target - len(nums1)), min(len(nums2) - 1, target), nums2, nums1)
        
