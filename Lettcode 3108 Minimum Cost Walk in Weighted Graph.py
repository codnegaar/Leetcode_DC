'''
Lettcode 3108 Minimum Cost Walk in Weighted Graph

There is an undirected weighted graph with n vertices labeled from 0 to n - 1.
You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.
walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the 
vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.
The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, 
if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the 
bitwise AND operator.
You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending 
at vertex ti. If there exists no such walk, the answer is -1.
Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

Example 1:
        Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]
        Output: [1,-1]
        Explanation:
        To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).
        In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:
        Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]
        Output: [0]
        Explanation:
        To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

Constraints:        
        2 <= n <= 105
        0 <= edges.length <= 105
        edges[i].length == 3
        0 <= ui, vi <= n - 1
        ui != vi
        0 <= wi <= 105
        1 <= query.length <= 105
        query[i].length == 2
        0 <= si, ti <= n - 1
        si != ti
'''

from typing import List

class UnionFind:
    """
    Disjoint Set Union (DSU) with Path Compression and Union by Rank.
    Also maintains a component-wise bitwise AND value.
    """
    def __init__(self, size: int):
        """
        Initializes the Union-Find data structure.

        :param size: Number of nodes in the graph.
        """
        self.parent = list(range(size))  # Parent array for union-find
        self.rank = [1] * size  # Rank array for union-by-rank
        self.component_and = [~0] * size  # Initialize with all bits set (equivalent to -1)

    def find(self, x: int) -> int:
        """
        Finds the root representative of a set with path compression.

        :param x: Node whose root is to be found.
        :return: Root representative of the set.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int, w: int):
        """
        Unites two disjoint sets using union by rank and updates component-wise AND.

        :param x: First node.
        :param y: Second node.
        :param w: Weight of the edge connecting x and y.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # Already connected, just update the AND value
            self.component_and[root_x] &= w
            return

        # Union by rank to keep tree shallow
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x  # Ensure root_x is the deeper root

        self.parent[root_y] = root_x  # Attach root_y to root_x
        self.component_and[root_x] &= self.component_and[root_y] & w  # Update component AND

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1  # Increase rank if necessary


class Solution:
    """
    Solution class to find the minimum cost between queried nodes in a weighted graph.
    """
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Computes the minimum cost (bitwise AND of edges) for each query.

        :param n: Number of nodes in the graph.
        :param edges: List of edges [u, v, weight].
        :param queries: List of queries [s, e].
        :return: List of results, where each element is the minimum cost for a query.
        """
        uf = UnionFind(n)  # Initialize Union-Find structure

        # Process edges to create connected components
        for u, v, w in edges:
            uf.union(u, v, w)

        # Answer each query
        result = []
        for s, e in queries:
            root_s = uf.find(s)
            root_e = uf.find(e)
            if root_s == root_e:
                result.append(uf.component_and[root_s])  # Minimum cost if connected
            else:
                result.append(-1)  # Not connected, return -1

        return result
