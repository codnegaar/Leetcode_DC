'''
Leetcode 3373 Maximize the Number of Target Nodes After Connecting Trees II

There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between 
nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one 
node from the first tree to another node in the second tree.
Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

Example 1:
        Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
        Output: [8,7,7,8,8]
        Explanation:
                For i = 0, connect node 0 from the first tree to node 0 from the second tree.
                For i = 1, connect node 1 from the first tree to node 4 from the second tree.
                For i = 2, connect node 2 from the first tree to node 7 from the second tree.
                For i = 3, connect node 3 from the first tree to node 0 from the second tree.
                For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:
        Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]
        Output: [3,6,6,6,6]
        Explanation: For every i, connect node i of the first tree with any node of the second tree.   
 
Constraints:
        2 <= n, m <= 105
        edges1.length == n - 1
        edges2.length == m - 1
        edges1[i].length == edges2[i].length == 2
        edges1[i] = [ai, bi]
        0 <= ai, bi < n
        edges2[i] = [ui, vi]
        0 <= ui, vi < m
        The input is generated such that edges1 and edges2 represent valid trees.

'''

from typing import List

class Solution:
    def dfs(
        self, 
        node: int, 
        color: int, 
        graph: List[List[int]], 
        component: List[int], 
        bipartite: List[int]
    ) -> None:
        """
        Depth-First Search to color nodes and count bipartite group sizes.
        
        Parameters:
        - node (int): Current node being visited.
        - color (int): Current color (0 or 1).
        - graph (List[List[int]]): Adjacency list representation of the graph.
        - component (List[int]): Node color assignments (-1 if unvisited).
        - bipartite (List[int]): Counter for nodes in each color group.
        """
        bipartite[color] += 1
        component[node] = color
        for neighbor in graph[node]:
            if component[neighbor] == -1:
                self.dfs(neighbor, 1 - color, graph, component, bipartite)

    def build_graph(self, edges: List[List[int]], n: int) -> List[List[int]]:
        """
        Constructs an adjacency list for a graph with n nodes.

        Parameters:
        - edges (List[List[int]]): List of undirected edges.
        - n (int): Number of nodes.

        Returns:
        - List[List[int]]: Adjacency list of the graph.
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """
        Calculates the maximum target values based on bipartite group sizes 
        in two graphs.

        Parameters:
        - edges1 (List[List[int]]): Edge list for first graph (tree).
        - edges2 (List[List[int]]): Edge list for second graph (tree).

        Returns:
        - List[int]: Computed values based on corresponding node colors and group sizes.
        """
        n1, n2 = len(edges1) + 1, len(edges2) + 1

        # Build graphs from edge lists
        graph1 = self.build_graph(edges1, n1)
        graph2 = self.build_graph(edges2, n2)

        # DFS on first graph to color nodes and count partitions
        component1 = [-1] * n1
        bipartite1 = [0, 0]
        self.dfs(0, 0, graph1, component1, bipartite1)

        # Precompute the bipartite group size for each node in graph1
        ans = [bipartite1[component1[i]] for i in range(n1)]

        # DFS on second graph to count group sizes
        component2 = [-1] * n2
        bipartite2 = [0, 0]
        self.dfs(0, 0, graph2, component2, bipartite2)

        # Add the max group size from graph2 to each node’s value from graph1
        max_bipartite2 = max(bipartite2)
        return [val + max_bipartite2 for val in ans]


# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Define two simple tree structures
    edges1 = [[0, 1], [1, 2], [1, 3]]
    edges2 = [[0, 1], [0, 2]]

    result = solution.maxTargetNodes(edges1, edges2)
    print("Result:", result)
