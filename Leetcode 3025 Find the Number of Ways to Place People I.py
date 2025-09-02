'''
Leetcode 3025 Find the Number of Ways to Place People I
 
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].
Count the number of pairs of points (A, B), where A is on the upper left side of B, and
there are no other points in the rectangle (or line) they make (including the border). Return the count.

Example 1:
        Input: points = [[1,1],[2,2],[3,3]]
        Output: 0
        Explanation: There is no way to choose A and B so A is on the upper left side of B.

Example 2:
        Input: points = [[6,2],[4,4],[2,6]]
        Output: 2
        Explanation:
                The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
                The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
                The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.

Example 3:
        Input: points = [[3,1],[1,3],[1,1]]
        Output: 2
        Explanation:
                The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
                The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
                The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.
         

Constraints:
        2 <= n <= 50
        points[i].length == 2
        0 <= points[i][0], points[i][1] <= 50
        All points[i] are distinct.

'''
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        Count the number of valid pairs of points (i, j) such that:
        - points[i].x <= points[j].x
        - points[i].y >= points[j].y
        - No other point lies inside the axis-aligned rectangle defined by i (top-left) and j (bottom-right).

        Parameters
        ----------
        points : List[List[int]]
            A list of [x, y] coordinates representing the points.

        Returns
        -------
        int
            The total number of valid pairs.
        """

        # Sort points by x ascending, y descending to ensure consistent ordering
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0

        # For each left anchor point (i)
        for i in range(n):
            max_y = -float("inf")  # Track the highest y encountered so far
            # For each right anchor point (j > i)
            for j in range(i + 1, n):
                # Skip if it cannot form a valid rectangle
                if points[j][1] > points[i][1]:
                    continue

                # A pair (i, j) is valid only if no point in between has y inside rectangle
                # Instead of checking all k, we track the maximum y seen so far
                if points[j][1] > max_y:
                    count += 1
                    max_y = points[j][1]

        return count


