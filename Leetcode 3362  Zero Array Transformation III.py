'''
Leetcode 3362  Zero Array Transformation III
 
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].
Each queries[i] represents the following action on nums:
Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.
Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array 
using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

Example 1:
        Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
        Output: 1
        Explanation: After removing queries[2], nums can still be converted to a zero array.
        Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
        Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.

Example 2:
        Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]
        Output: 2
        Explanation: We can remove queries[2] and queries[3].
        Example 3: Input: nums = [1,2,3,4], queries = [[0,3]]
        Output: -1
        Explanation: nums cannot be converted to a zero array even after using all the queries.
     
Constraints:
        1 <= nums.length <= 105
        0 <= nums[i] <= 105
        1 <= queries.length <= 105
        queries[i].length == 2
        0 <= li <= ri < nums.length
'''

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Determines the maximum number of queries that can be *not* chosen such that
        at each position `i` in the array, there are at least `nums[i]` active queries
        covering index `i`.

        Parameters:
        - nums: List[int] - Required number of active queries at each position i.
        - queries: List[List[int]] - Each query is a range [l, r].

        Returns:
        - int: Maximum number of queries that can be removed (i.e., not chosen),
               or -1 if the requirement cannot be satisfied.
        """

        n = len(nums)
        start_map = defaultdict(list)

        # Group the queries by their start index
        for l, r in queries:
            start_map[l].append(r)

        max_heap = []   # Max-heap (store negative values for max behavior)
        min_heap = []   # Min-heap for active query ends
        chosen = 0      # Count of queries chosen to satisfy coverage

        for i in range(n):
            # Push the end of queries starting at i into max-heap
            for r in start_map[i]:
                heapq.heappush(max_heap, -r)

            # Remove expired queries from the active list
            while min_heap and min_heap[0] < i:
                heapq.heappop(min_heap)

            # Calculate how many more queries are needed at position i
            required = nums[i] - len(min_heap)

            # Choose additional queries from available ones
            for _ in range(required):
                # Remove expired entries from max-heap
                while max_heap and -max_heap[0] < i:
                    heapq.heappop(max_heap)

                if not max_heap:
                    return -1  # Not enough valid queries available

                r = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, r)
                chosen += 1

        return len(queries) - chosen
