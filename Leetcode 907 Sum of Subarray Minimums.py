'''

Leetcode 907 Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.


Example 1:
        Input: arr = [3,1,2,4]
        Output: 17
        Explanation: 
                Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
                Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
                Sum is 17.

Example 2:
        Input: arr = [11,81,94,43,3]
        Output: 444 

Constraints:
        1 <= arr.length <= 3 * 104
        1 <= arr[i] <= 3 * 104

'''

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n  # Nearest smaller element to the left
        right = [n] * n  # Nearest smaller element to the right
        stack = []

        # Calculate left boundaries
        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        # Calculate right boundaries
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Calculate the result using the left and right boundaries
        mod = 10**9 + 7
        result = 0
        for i, value in enumerate(arr):
            left_distance = i - left[i]
            right_distance = right[i] - i
            result += left_distance * right_distance * value
            result %= mod

        return result
