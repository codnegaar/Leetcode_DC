'''
Leetcode 3356 Zero Array Transformation II

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
Each queries[i] represents the following action on nums:
Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.
Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

Example 1:
        Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
        Output: 2
        Explanation:
                For i = 0 (l = 0, r = 2, val = 1):
                Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
                The array will become [1, 0, 1].
                For i = 1 (l = 0, r = 2, val = 1):
                Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
                The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:
        Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
        Output: -1
        Explanation:
                For i = 0 (l = 1, r = 3, val = 2):
                Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
                The array will become [4, 1, 0, 0].
                For i = 1 (l = 0, r = 2, val = 1):
                Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
                The array will become [3, 0, 0, 0], which is not a Zero Array.
         
Constraints:

        1 <= nums.length <= 105
        0 <= nums[i] <= 5 * 105
        1 <= queries.length <= 105
        queries[i].length == 3
        0 <= li <= ri < nums.length
        1 <= vali <= 5

'''
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Determines the minimum number of operations required to make the array `nums` zero.
        
        Parameters:
        - nums (List[int]): The initial array of integers.
        - queries (List[List[int]]): A list of operations, where each operation is represented
          as [l, r, val], meaning add `val` to elements in the range [l, r].

        Returns:
        - int: The minimum number of operations required to make all elements zero, or -1 if not possible.
        """

        def is_zero_array(k: int) -> bool:
            """
            Checks if the first `k` queries can make the entire `nums` array zero.
            
            Parameters:
            - k (int): The number of queries to consider.

            Returns:
            - bool: True if the array can be made zero using the first `k` queries, False otherwise.
            """
            n = len(nums)
            pref = [0] * (n + 1)  # Prefix difference array for range updates
            
            # Apply the first `k` queries
            for i in range(k):
                l, r, val = queries[i]
                pref[l] += val
                if r + 1 < n:
                    pref[r + 1] -= val
            
            # Compute the prefix sum and check if it covers `nums`
            running_sum = 0
            for i in range(n):
                running_sum += pref[i]
                if running_sum < nums[i]:  # If any number cannot be made zero, return False
                    return False
            return True

        # Binary search to find the minimum number of queries needed
        left, right = 0, len(queries) + 1
        while left < right:
            mid = (left + right) // 2
            if is_zero_array(mid):
                right = mid  # Try a smaller number of operations
            else:
                left = mid + 1  # Increase the number of operations
        
        return left if left <= len(queries) else -1
