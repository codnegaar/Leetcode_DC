'''
Leetcode 3342 Find Minimum Time to Reach Last Room II
 
There is a dungeon with n x m rooms arranged as a grid.
You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. 
You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two 
seconds for the next, alternating between the two.
Return the minimum time to reach the room (n - 1, m - 1).
Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
        Input: moveTime = [[0,4],[4,4]]
        Output: 7
        Explanation: The minimum time required is 7 seconds.
        At time t == 4, move from room (0, 0) to room (1, 0) in one second.
        At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

Example 2:
        Input: moveTime = [[0,0,0,0],[0,0,0,0]]
        Output: 6
        Explanation: The minimum time required is 6 seconds.
        At time t == 0, move from room (0, 0) to room (1, 0) in one second.
        At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
        At time t == 3, move from room (1, 1) to room (1, 2) in one second.
        At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.

Example 3:
        Input: moveTime = [[0,1],[1,2]]
        Output: 4 

Constraints:
        2 <= n == moveTime.length <= 750
        2 <= m == moveTime[i].length <= 750
        0 <= moveTime[i][j] <= 109
'''

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Calculates the minimum time required to reach the bottom-right cell of the grid.
        
        Each cell contains a time constraint, and movement between cells alternates in cost
        (between 1 and 2). The goal is to reach the destination in the minimum possible time
        without revisiting any cell.
        
        Parameters:
        - moveTime (List[List[int]]): A 2D grid representing time constraints for each cell.
        
        Returns:
        - int: Minimum time to reach the bottom-right cell. Returns -1 if unreachable.
        """
        n, m = len(moveTime), len(moveTime[0])
        
        # Priority queue: (current_time, row, col, move_cost)
        pq = [(0, 0, 0, 1)]
        
        # Movement directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Visited set to avoid revisiting the same cell
        visited = set()
        visited.add((0, 0))

        while pq:
            time, i, j, cost = heapq.heappop(pq)

            # If bottom-right is reached, return the time
            if i == n - 1 and j == m - 1:
                return time

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                    # Wait if arrival is before allowed time
                    wait_time = max(time, moveTime[x][y])
                    total_time = wait_time + cost

                    # Alternate cost between 1 and 2
                    next_cost = 3 - cost

                    heapq.heappush(pq, (total_time, x, y, next_cost))
                    visited.add((x, y))

        return -1  # If destination is not reachable

