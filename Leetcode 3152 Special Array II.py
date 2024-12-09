'''
Leetcode 3152 Special Array II

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray nums[fromi..toi] is special or not.
Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

Example 1:
        Input: nums = [3,4,1,2,6], queries = [[0,4]]
        Output: [false]
        Explanation:
                The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:
        Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
        Output: [false,true]
        Explanation:
                The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
                The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.    

Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 105
        1 <= queries.length <= 105
        queries[i].length == 2
        0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
'''
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        Determines whether the array segments between query indices are "special."
        A segment is "special" if the count of adjacent pairs with odd sums matches
        the segment length.
        
        Parameters:
        nums (List[int]): The input array of integers.
        queries (List[List[int]]): A list of queries, where each query contains two integers 
                                   [a, b], representing the start and end indices (inclusive).
        
        Returns:
        List[bool]: A list of boolean values, where each element corresponds to whether the 
                    respective query segment is "special."
        """
        n = len(nums)
        pref = [0] * n  # Prefix array to store count of odd-sum adjacent pairs
        cnt = 0
        
        # Build the prefix array
        for i in range(1, n):
            # Check if the sum of nums[i-1] and nums[i] is odd
            if (nums[i - 1] + nums[i]) % 2 == 1:
                cnt += 1
            pref[i] = cnt  # Store the count up to index i
        
        # Evaluate each query
        results = []
        for a, b in queries:
            # Check if the number of odd-sum pairs matches the segment length
            results.append(pref[b] - pref[a] == (b - a))
        
        return results



# Unit Test with Examples
if __name__ == "__main__":
    solution = Solution()
    
    # Example Test Case 1
    nums1 = [1, 2, 3, 4]
    queries1 = [[0, 2], [1, 3]]
    result1 = solution.isArraySpecial(nums1, queries1)
    print(result1)  # Expected: [False, True]
    
    # Example Test Case 2
    nums2 = [5, 6, 7, 8, 9]
    queries2 = [[0, 3], [2, 4]]
    result2 = solution.isArraySpecial(nums2, queries2)
    print(result2)  # Expected: [True, True]
    
    # Edge Case Test Case
    nums3 = [10]
    queries3 = [[0, 0]]
    result3 = solution.isArraySpecial(nums3, queries3)
    print(result3)  # Expected: [True]
