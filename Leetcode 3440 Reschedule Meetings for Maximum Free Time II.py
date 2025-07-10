'''
Leetcode 3440 Reschedule Meetings for Maximum Free Time II
 
You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays, startTime and endTime, each of length n.
These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the
ith meeting occurs during the time [startTime[i], endTime[i]].
You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping. 
to maximize the longest continuous period of free time during the event.
Return the maximum amount of free time possible after rearranging the meetings.
Note that the meetings can not be rescheduled to a time outside the event, and they should remain non-overlapping.
Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting. 

Example 1:
        Input: eventTime = 5, startTime = [1,3], endTime = [2,5]
        Output: 2
        Explanation: Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:
        Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]
        Output: 7
        Explanation: Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].

Example 3:
        Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]
        Output: 6
        Explanation: Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].

Example 4:
        Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
        Output: 0
        Explanation: There is no time during the event not occupied by meetings.
 
Constraints:
        1 <= eventTime <= 109
        n == startTime.length == endTime.length
        2 <= n <= 105
        0 <= startTime[i] < endTime[i] <= eventTime
        endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].

'''
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Calculates the maximum free time interval that can exist by possibly merging
        two adjacent gaps around an event, considering all events have fixed durations.

        Parameters:
        - eventTime (int): Total time from 0 to eventTime (timeline end)
        - startTime (List[int]): Start times of scheduled events
        - endTime (List[int]): End times of scheduled events

        Returns:
        - int: The maximum free time that can be achieved
        """
        n = len(startTime)

        # Calculate gaps between events including start of timeline and end of timeline
        gaps = [startTime[0]]  # gap before first event
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])  # gap after last event

        # Calculate durations of each event
        durations = [endTime[i] - startTime[i] for i in range(n)]

        # Track top 3 maximum gaps with their counts
        top_gaps = []  # List of (gap_value, count), always sorted descending
        gap_counts = {}

        for g in gaps:
            gap_counts[g] = gap_counts.get(g, 0) + 1

        # Extract top 3 unique gaps
        for g in sorted(gap_counts.keys(), reverse=True)[:3]:
            top_gaps.append((g, gap_counts[g]))

        # Initial max is the largest gap without merging
        max_free = top_gaps[0][0]

        # Try merging adjacent gaps with the event between them
        for i in range(n):
            left_gap = gaps[i]
            right_gap = gaps[i + 1]
            duration = durations[i]
            merged = left_gap + right_gap + duration

            # Determine best alternative max gap excluding left_gap and right_gap
            remaining_max = 0
            for val, count in top_gaps:
                exclude_count = (left_gap == val) + (right_gap == val)
                if exclude_count < count:
                    remaining_max = val
                    break

            # New max can either be the merged total (if duration blocks nothing)
            # or merged - duration (if we "slide" event over)
            if remaining_max >= duration:
                max_candidate = max(merged, remaining_max)
            else:
                max_candidate = merged - duration

            max_free = max(max_free, max_candidate)

        return max_free

