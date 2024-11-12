'''
Leetcode - 56 - Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

Example 1:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.  
Constraints:
        1 <= intervals.length <= 104
        intervals[i].length == 2
        0 <= starti <= endi <= 104
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in sorted(intervals):
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return and


# Second solution
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals in a list and returns the merged list.

        Parameters:
        - intervals (List[List[int]]): A list of intervals, each represented as [start, end].

        Returns:
        - List[List[int]]: A list of merged intervals where all overlapping intervals are combined.
        """
        
        # Sort intervals by their start time to allow sequential merging
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for interval in intervals:
            # If merged is empty or current interval does not overlap with last in merged, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge by extending the end of the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

