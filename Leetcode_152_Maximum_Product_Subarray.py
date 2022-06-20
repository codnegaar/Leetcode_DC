'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array. 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos =  nums[0]
        neg =  nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            pos = max(num, pos * num, neg * num)
            neg = min(num, pos * num, neg * num)
            result = max(result, pos)
        return result


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
