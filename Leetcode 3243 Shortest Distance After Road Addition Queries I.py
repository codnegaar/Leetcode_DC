'''
Leetcode 3243 Shortest Distance After Road Addition Queries I

You are given an integer n and a 2D integer array queries.
There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.
Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

Example 1:
        Input: n = 5, queries = [[2,4],[0,2],[0,4]]
        Output: [3,2,1]
        Explanation:
                  After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
                  After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.
                  After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:
        Input: n = 4, queries = [[0,3],[0,2]]
        Output: [1,1]
        Explanation:
                After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.
                After the addition of the road from 0 to 2, the length of the shortest path remains 1. 

Constraints:
        3 <= n <= 500
        1 <= queries.length <= 500
        queries[i].length == 2
        0 <= queries[i][0] < queries[i][1] < n
        1 < queries[i][1] - queries[i][0]
        There are no repeated roads among the queries.

'''

from collections import deque

class Solution:
    def bfs(self, start, end, n, graph):
        """
        Perform BFS to find the shortest distance from start to end in the graph.

        Parameters:
        start (int): Starting node.
        end (int): Ending node.
        n (int): Number of nodes in the graph.
        graph (List[List[int]]): Adjacency list representing the graph.

        Returns:
        int: The shortest distance from start to end.
        """
        # Initialize distances as infinity for all nodes
        dist = [float('inf')] * n
        dist[start] = 0
        q = deque([start])

        # Perform BFS
        while q:
            curr = q.popleft()
            # Traverse all neighbors of the current node
            for u in graph[curr]:
                # If we find a shorter path, update and enqueue the neighbor
                if dist[u] > dist[curr] + 1:
                    dist[u] = dist[curr] + 1
                    q.append(u)

        return dist[end]

    def shortestDistanceAfterQueries(self, n, queries):
        """
        Find the shortest distance from node 0 to node n-1 after each query.

        Parameters:
        n (int): Number of nodes in the graph.
        queries (List[Tuple[int, int]]): List of queries where each query adds an edge (u, v).

        Returns:
        List[int]: List of shortest distances after each query.
        """
        answer = []
        # Initialize graph with each node pointing to the next node (linear structure)
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)

        # Process each query
        for u, v in queries:
            graph[u].append(v)  # Add the edge (u -> v)
            # Calculate shortest distance from node 0 to node n-1
            answer.append(self.bfs(0, n - 1, n, graph))

        return answer

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    n = 5  # Number of nodes
    queries = [(1, 3), (0, 4), (2, 4)]  # List of queries to add edges
    result = sol.shortestDistanceAfterQueries(n, queries)
    print(result)  # Output the shortest distances after each query
