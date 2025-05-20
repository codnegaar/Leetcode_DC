'''
Leetcode 3355 Zero Array Transformation I

You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].
For each queries[i]:
        Select a subset of indices within the range [li, ri] in nums.
        Decrement the values at the selected indices by 1.
        A Zero Array is an array where all elements are equal to 0.
        Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

Example 1:
        Input: nums = [1,0,1], queries = [[0,2]]
        Output: true
        Explanation:
                For i = 0:
                          Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
                          The array will become [0, 0, 0], which is a Zero Array.

Example 2:
        Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
        Output: false
        Explanation:        
                For i = 0:
                          Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
                          The array will become [4, 2, 1, 0].
                          For i = 1:
                          Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
                          The array will become [3, 1, 0, 0], which is not a Zero Array.
                 
Constraints:
        1 <= nums.length <= 105
        0 <= nums[i] <= 105
        1 <= queries.length <= 105
        queries[i].length == 2
        0 <= li <= ri < nums.length

'''

class Solution:
    def isZeroArray(self, nums, queries):
        """
        Determines whether the array `nums` can be reduced to all zeros or less
        using a set of increment operations defined by `queries`.

        Each query [l, r] means increment all elements in the range nums[l] to nums[r] by 1.
        This function checks whether after applying all operations in reverse (interpreting
        them as 'removal capability'), all elements in nums can be reduced to zero or less.

        Parameters:
        - nums (List[int]): The original list of integers.
        - queries (List[List[int]]): A list of operations, each given by a range [l, r].

        Returns:
        - bool: True if all elements can be reduced to zero or less, False otherwise.
        """

        n = len(nums)
        # Initialize difference array to efficiently apply range updates
        diff = [0] * (n + 1)

        # Mark the start and end+1 for each increment operation
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        # Accumulate the diff array to get the effective increments at each index
        current_add = 0
        for i in range(n):
            current_add += diff[i]
            # If any value in nums is greater than the applied increment, return False
            if nums[i] > current_add:
                return False

        return True
