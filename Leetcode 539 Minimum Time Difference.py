'''
Leetcode 539 Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list. 

Example 1:
        Input: timePoints = ["23:59","00:00"]
        Output: 1
        
Example 2:
        Input: timePoints = ["00:00","23:59","00:00"]
        Output: 0
 

Constraints:
        2 <= timePoints.length <= 2 * 104
        timePoints[i] is in the format "HH:MM".
        
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert timePoints to minutes and sort them
        minutes = sorted(int(h) * 60 + int(m) for h, m in (tp.split(':') for tp in timePoints))
        
        # Find the minimum difference between adjacent time points
        min_diff = min(b - a for a, b in zip(minutes, minutes[1:]))
        
        # Handle the circular case (difference between first and last time points)
        return min(min_diff, 1440 + minutes[0] - minutes[-1])


# solution 2
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Step 1: Convert all time points to minutes and store in a list
        minutes = [0] * len(timePoints)
        for i, timePoint in enumerate(timePoints):
            h, m = map(int, timePoint.split(':'))
            minutes[i] = h * 60 + m
        
        # Step 2: Sort the time points
        minutes.sort()
        
        # Step 3: Calculate the minimum difference
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Step 4: Handle the circular case (difference between the first and last time points)
        return min(min_diff, 1440 + minutes[0] - minutes[-1])
