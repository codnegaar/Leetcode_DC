'''

Leetcode 3169 Count Days Without Meetings
 
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). 
You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap. 

Example 1:
        Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
        Output: 2
        Explanation: There is no meeting scheduled on the 4th and 8th days.

Example 2:
        Input: days = 5, meetings = [[2,4],[1,3]]
        Output: 1
        Explanation: There is no meeting scheduled on the 5th day.

Example 3:
        Input: days = 6, meetings = [[1,6]]
        Output: 0
        Explanation: Meetings are scheduled for all working days.

Constraints:
        1 <= days <= 109
        1 <= meetings.length <= 105
        meetings[i].length == 2
        1 <= meetings[i][0] <= meetings[i][1] <= days
'''

from typing import List

class Solution:
    """
    Solution to count the number of days without meetings,
    given a list of potentially overlapping meeting intervals.
    """

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Calculates the number of days without any meetings.

        Parameters:
        -----------
        days : int
            Total number of calendar days (from day 1 to day `days`).
        meetings : List[List[int]]
            List of meetings where each meeting is [start_day, end_day].

        Returns:
        --------
        int
            Number of days without any scheduled meetings.

        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n) for storing merged intervals
        """

        # Step 1️⃣: Sort meetings by start day
        meetings.sort()

        # Step 2️⃣: Merge overlapping or adjacent meeting intervals
        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings or meeting[0] > merged_meetings[-1][1]:
                # No overlap with the last interval, add as new
                merged_meetings.append(meeting)
            else:
                # Overlapping — merge by extending the end day
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])

        # Step 3️⃣: Count total meeting days from merged intervals
        meeting_days_count = 0
        for start, end in merged_meetings:
            meeting_days_count += (end - start + 1)

        # Step 4️⃣: Subtract meeting days from total days
        return days - meeting_days_count

