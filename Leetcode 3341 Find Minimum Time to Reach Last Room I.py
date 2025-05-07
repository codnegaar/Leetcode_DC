'''
Leetcode 3341 Find Minimum Time to Reach Last Room I
 
There is a dungeon with n x m rooms arranged as a grid.
You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. 
You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
Return the minimum time to reach the room (n - 1, m - 1).
Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
        Input: moveTime = [[0,4],[4,4]]
        Output: 6
        Explanation: The minimum time required is 6 seconds.
        At time t == 4, move from room (0, 0) to room (1, 0) in one second.
        At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
        Input: moveTime = [[0,0,0],[0,0,0]]
        Output: 3
        Explanation: The minimum time required is 3 seconds.
        At time t == 0, move from room (0, 0) to room (1, 0) in one second.
        At time t == 1, move from room (1, 0) to room (1, 1) in one second.
        At time t == 2, move from room (1, 1) to room (1, 2) in one second.
        
Example 3:
        Input: moveTime = [[0,1],[1,2]]
        Output: 3

Constraints:
        2 <= n == moveTime.length <= 50
        2 <= m == moveTime[i].length <= 50
        0 <= moveTime[i][j] <= 109

'''

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum time required to reach the bottom-right cell in a grid,
        considering delays specified in each cell.

        Parameters:
        grid (List[List[int]]): A 2D grid where grid[r][c] is the minimum time 
                                before you can enter cell (r, c).

        Returns:
        int: Minimum time to reach the bottom-right cell, or -1 if unreachable.
        """

        rows, cols = len(grid), len(grid[0])

        # Each cell in the visited matrix keeps track of the earliest time visited
        visited = [[float('inf')] * cols for _ in range(rows)]

        # Movement directions: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Min-heap priority queue: (current_time, row, col)
        heap = [(0, 0, 0)]

        while heap:
            time, r, c = heapq.heappop(heap)

            # If we reached the destination cell
            if r == rows - 1 and c == cols - 1:
                return time

            # If we've already visited this cell at an earlier or equal time, skip it
            if time >= visited[r][c]:
                continue

            visited[r][c] = time  # Mark the time we visited this cell

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip invalid or out-of-bounds moves
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                # Wait until the cell becomes accessible
                wait_time = grid[nr][nc]
                next_time = max(time + 1, wait_time + 1)

                if next_time < visited[nr][nc]:
                    heapq.heappush(heap, (next_time, nr, nc))

        return -1  # If destination is unreachable
