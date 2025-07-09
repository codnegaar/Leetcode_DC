'''
Leetcode 3439 Reschedule Meetings for Maximum Free Time I
 
You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings,
where the ith meeting occurs during the time [startTime[i], endTime[i]].
You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
The relative order of all the meetings should stay the same and they should remain non-overlapping.
Return the maximum amount of free time possible after rearranging the meetings.
Note that the meetings can not be rescheduled to a time outside the event. 

Example 1:
        Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
        Output: 2
        Explanation: Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:
        Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
        Output: 6
        Explanation: Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

Example 3:
        Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
        Output: 0
        Explanation: There is no time during the event not occupied by meetings.
         
Constraints:
        1 <= eventTime <= 109
        n == startTime.length == endTime.length
        2 <= n <= 105
        1 <= k <= n
        0 <= startTime[i] < endTime[i] <= eventTime
        endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
'''
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Calculates the maximum total free time achievable by skipping up to 'k' activities.

        Parameters:
        - eventTime (int): Total duration of the event.
        - k (int): Maximum number of activities that can be skipped.
        - startTime (List[int]): Start times of activities in chronological order.
        - endTime (List[int]): End times of activities in chronological order.

        Returns:
        - int: Maximum free time obtainable within the constraints.
        """

        n = len(startTime)
        
        # Calculate all the 'gaps' between activities + time before first + after last
        gaps = [startTime[0]]  # Time before the first activity
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])  # Time between consecutive activities
        gaps.append(eventTime - endTime[-1])  # Time after the last activity

        # Sliding window size: max number of gaps we can keep = k+1
        window_size = min(k + 1, len(gaps))

        # Calculate initial window sum
        curr_sum = sum(gaps[:window_size])
        max_sum = curr_sum

        # Slide the window across the gap list
        for i in range(window_size, len(gaps)):
            curr_sum += gaps[i] - gaps[i - window_size]
            max_sum = max(max_sum, curr_sum)

        return max_sum
