'''

Leetcode 335 Self Crossing

You are given an array of integers distance.

You start at the point (0, 0) on an X-Y plane, and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south,
distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return true if your path crosses itself or false if it does not.

 

Example 1:
        Input: distance = [2,1,1,2]
        Output: true
        Explanation: The path crosses itself at the point (0, 1).

Example 2:
        Input: distance = [1,2,3,4]
        Output: false
        Explanation: The path does not cross itself at any point.

Example 3:
        Input: distance = [1,1,1,2,1]
        Output: true
        Explanation: The path crosses itself at the point (0, 0).
 

Constraints:
        1 <= distance.length <= 105
        1 <= distance[i] <= 105

Problem Description
This problem presents a scenario where you are simulating movement on an X-Y plane starting at the origin (0, 0). You're given an array of integers called distance that dictates
how far you move in each direction. The movement is in a cycle: north, west, south, east, and then repeats - north, west, and so on. The question asks whether, at any point during
this movement, you cross your own path.

Think of it as drawing a zigzag line on a piece of paper without lifting your pen. The task is to figure out if your line touches or crosses itself at any point. A self-crossing
path would imply that you end up at a point on the plane that you have previously visited.

The sequence of the movement is important here – after each move, you change your direction in a counter-clockwise manner. This means if you start by going north, the next move 
will be west, followed by south, then east, and this pattern will continue in this order for each subsequent move.

Intuition
To solve the problem, we must understand the conditions that can cause the path to cross itself. There are generally three cases where crossing can happen:

Case 1: Fourth Line Crosses the First - This case happens when the current step overshoots the first step. More specifically, the path crosses if the current distance is greater
than or equal to the distance two steps back, and the distance a step before is less than or equal to the distance three steps back.

Case 2: Fifth Line Meets the First - Here, the path's fifth segment overlaps with the first segment if the current step is equal to the step three steps back, and the sum of
the current step and the step four steps back is greater than or equal to the step two steps back.

Case 3: Sixth Line Crosses the First - This is a more complex scenario where the sixth line crosses over the first. For this to happen, several conditions need to match: the
fourth step is greater than or equal to the second step, the fifth step is less than or equal to the third step, the sum of the third and the sixth steps is greater than or
equal to the first step, and the sixth step is greater than or equal to the difference between the second and fourth steps.

The provided solution checks for these three cases while iterating through the distance array starting from the third index, as cases for self-crossing only become possible from 
the fourth step onwards. If any of these conditions are satisfied at any point during the iteration, it confirms that the path has crossed itself and the function immediately 
returns True. If none of these cases are satisfied by the end of the iteration, we can confidently say the path does not cross itself, and the function returns False.

Overall, the code solution relies on understanding the geometry of movement and identifying cases where a line segment could intersect with non-adjacent segments of the path 
based on the distances traveled.

Solution Approach
To implement the solution, we follow a straightforward iteration through the distance array and apply condition checks based on the three cases that could result in crossing.
The code does not use any complex data structures or algorithms, but instead relies on logical conditions and comparisons to determine if a crossing has occurred.

The solution iterates through the distance array starting from index 3, because the first three steps (to the north, west, and south) cannot result in a crossing. It is only 
from the fourth step onwards we might have a crossing situation.

The implementation is based on the following checks corresponding to the cases illustrated in the Reference Solution Approach:

Case 1 Check: This is when the current step (d[i]) crosses the path of the first step (d[i - 2]). In code terms, we are checking if d[i] >= d[i - 2] and simultaneously, 
if d[i - 1] <= d[i - 3]. If both conditions are true, the path crosses itself.

Case 2 Check: This occurs when the fifth step exactly meets with the first step. The condition includes a check for equality, d[i - 1] == d[i - 3], and also checks if the sum 
of the current step (d[i]) and four steps back (d[i - 4]) is greater than or equal to the distance two steps back (d[i - 2]).

Case 3 Check: This deals with the potential crossing caused by the sixth line, which is the most complex case and has the most conditions. Here we must ensure the following:

        The fourth step is greater than or equal to the second, d[i - 2] >= d[i - 4].
        The fifth step is less than or equal to the third, d[i - 1] <= d[i - 3].
        The sixth step (d[i]) is greater than or equal to the second step (d[i - 2]) minus the fourth (d[i - 4]), d[i] >= d[i - 2] - d[i - 4].
        Plus, the sum of the fifth (d[i - 1]) and first steps (d[i - 5]) is greater than or equal to the third step (d[i - 3]).
These checks are evaluated using a for-loop that proceeds to the end of the array, or until a crossing is detected. If none of the conditions is met, the loop finishes and 
the function returns False, indicating that no crossing occurred.

The algorithm's complexity is O(n), where n is the length of the distance array. This is because it involves iterating through the array once and performing constant-time 
checks in each iteration.

In summary, the solution applies a systematic check for each case of self-crossing at every step after the third step, immediately ceases the iteration, and returns the
result once self-crossing is detected. If the iteration completes without finding a crossing, the path does not cross itself, and False is returned as the final result.


'''

from typing import List

class Solution:
    def isSelfCrossing(self, distances: List[int]) -> bool:
        """
        Check if the given path crosses itself.
      
        Args:
        distances: A list of integers representing the lengths of consecutive moves.
      
        Returns:
        True if the path crosses itself, otherwise False.
        """
      
        # Iterate over the distances, starting from the fourth move
        for i in range(3, len(distances)):
            # Case 1: Current line crosses the line 3 steps behind
            if distances[i] >= distances[i - 2] and distances[i - 1] <= distances[i - 3]:
                return True
          
            # Case 2: Current line overlaps with the line 4 steps behind
            if i >= 4 and distances[i - 1] == distances[i - 3] and distances[i] + distances[i - 4] >= distances[i - 2]:
                return True
          
            # Case 3: Current line crosses the line 5 steps behind
            if (i >= 5
                and distances[i - 2] >= distances[i - 4]
                and distances[i - 1] <= distances[i - 3]
                and distances[i] >= distances[i - 2] - distances[i - 4]
                and distances[i - 1] + distances[i - 5] >= distances[i - 3]):
                return True
      
        # If none of the cases cause a cross, the path does not cross itself
        return False
