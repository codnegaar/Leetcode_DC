'''
Leetcode 827 Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s. 

Example 1:
        Input: grid = [[1,0],[0,1]]
        Output: 3
        Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
        Input: grid = [[1,1],[1,0]]
        Output: 4
        Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
        
Example 3:
        Input: grid = [[1,1],[1,1]]
        Output: 4
        Explanation: Can't change any 0 to 1, only one island with area = 4.         

Constraints:
        n == grid.length
        n == grid[i].length
        1 <= n <= 500
        grid[i][j] is either 0 or 1.
'''
class DisjointSet:
    """Disjoint Set Union (DSU) / Union-Find with path compression and union by size."""

    def __init__(self, n: int):
        """
        Initialize DSU with n elements.

        :param n: Total number of nodes.
        """
        self.parent = list(range(n))  # Each node is its own parent initially
        self.size = [1] * n  # Each set has size 1 initially

    def find(self, node: int) -> int:
        """
        Find the root of the node with path compression.

        :param node: Node to find the root for.
        :return: Root of the node.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node_a: int, node_b: int):
        """
        Union two sets by size.

        :param node_a: First node.
        :param node_b: Second node.
        """
        root_a, root_b = self.find(node_a), self.find(node_b)

        if root_a != root_b:
            # Attach the smaller tree to the larger one
            if self.size[root_a] < self.size[root_b]:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            else:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]


class Solution:
    """Finds the largest island size in a binary grid when flipping at most one '0' to '1'."""

    def largestIsland(self, grid: list[list[int]]) -> int:
        """
        Calculate the largest possible island by flipping a single '0' to '1'.

        :param grid: 2D list representing the binary grid.
        :return: Size of the largest possible island.
        """
        rows, cols = len(grid), len(grid[0])
        ds = DisjointSet(rows * cols)  # Initialize DSU

        # Direction vectors for 4-way connectivity (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 1: Union adjacent '1's in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    node = r * cols + c  # Convert 2D index to 1D
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            ds.union(node, nr * cols + nc)

        # Step 2: Find the largest possible island size
        max_island_size = max(ds.size) if ds.size else 0  # Track largest existing island
        has_zero = False  # Flag to check if we have any zeros

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # Try flipping this '0' to '1'
                    has_zero = True
                    unique_roots = set()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            unique_roots.add(ds.find(nr * cols + nc))

                    # Sum up the sizes of unique neighboring islands and add one for the flipped cell
                    new_island_size = 1 + sum(ds.size[root] for root in unique_roots)
                    max_island_size = max(max_island_size, new_island_size)

        # If there were no zeros, return the entire grid size
        return max_island_size if has_zero else rows * cols


 
