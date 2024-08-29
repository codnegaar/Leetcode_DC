'''

Leetcode 947 Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Example 1:
        Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        Output: 5
        Explanation: One way to remove 5 stones is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,1].
        2. Remove stone [2,1] because it shares the same column as [0,1].
        3. Remove stone [1,2] because it shares the same row as [1,0].
        4. Remove stone [1,0] because it shares the same column as [0,0].
        5. Remove stone [0,1] because it shares the same row as [0,0].
        Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
        Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        Output: 3
        Explanation: One way to make 3 moves is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,0].
        2. Remove stone [2,0] because it shares the same column as [0,0].
        3. Remove stone [0,2] because it shares the same row as [0,0].
        Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
        Input: stones = [[0,0]]
        Output: 0
        Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 
Constraints:
        1 <= stones.length <= 1000
        0 <= xi, yi <= 104
        No two stones are at the same coordinate point.

''''

from typing import List

class Solution:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.connected_components = 0

    def removeStones(self, stones: List[List[int]]) -> int:
        for x, y in stones:
            self.union(x, ~y)  # Use bitwise NOT to distinguish between x and y coordinates.
        return len(stones) - self.connected_components

    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.connected_components += 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression.
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.connected_components -= 1


