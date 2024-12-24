'''

3203 Find Minimum Diameter After Merging Two Trees
 
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. 
You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates 
that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
You must connect one node from the first tree with another node from the second tree with an edge.
Return the minimum possible diameter of the resulting tree.
The diameter of a tree is the length of the longest path between any two nodes in the tree. 

Example 1:
        Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
        Output: 3
        Explanation:
        We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.
        
Example 2:
        Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
        Output: 5
        Explanation: We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

Constraints:
        1 <= n, m <= 105
        edges1.length == n - 1
        edges2.length == m - 1
        edges1[i].length == edges2[i].length == 2
        edges1[i] = [ai, bi]
        0 <= ai, bi < n
        edges2[i] = [ui, vi]
        0 <= ui, vi < m
        The input is generated such that edges1 and edges2 represent valid trees.

'''
from collections import defaultdict
from typing import List, Tuple

class Solution:
    """
    This class contains the method to calculate the minimum diameter of a tree
    after merging two trees by connecting one of their vertices.
    """

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
        Calculate the minimum diameter after merging two trees.

        Parameters:
        - edges1: List[List[int]]: List of edges defining the first tree.
        - edges2: List[List[int]]: List of edges defining the second tree.

        Returns:
        - int: Minimum diameter of the merged tree.
        """

        def build_graph(edges: List[List[int]]) -> defaultdict:
            """
            Build an adjacency list representation of the graph from edge list.

            Parameters:
            - edges: List[List[int]]: List of edges.

            Returns:
            - defaultdict: Adjacency list of the graph.
            """
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def find_tree_diameter_and_height(edges: List[List[int]]) -> Tuple[int, int]:
            """
            Compute the diameter and height of a tree given its edges.

            Parameters:
            - edges: List[List[int]]: List of edges.

            Returns:
            - Tuple[int, int]: The diameter and maximum height of the tree.
            """
            graph = build_graph(edges)

            def dfs(node: int, parent: int) -> Tuple[int, int]:
                """
                Depth-first search to calculate tree height and diameter.

                Parameters:
                - node: int: Current node being visited.
                - parent: int: Parent node of the current node.

                Returns:
                - Tuple[int, int]: Maximum height and diameter of the subtree.
                """
                max_height1, max_height2, diameter = 0, 0, 0

                # Explore all children
                for child in graph[node]:
                    if child != parent:  # Avoid revisiting the parent
                        child_height, child_diameter = dfs(child, node)
                        diameter = max(diameter, child_diameter)  # Update diameter

                        # Track top two maximum heights
                        if child_height + 1 > max_height1:
                            max_height2 = max_height1
                            max_height1 = child_height + 1
                        elif child_height + 1 > max_height2:
                            max_height2 = child_height + 1

                # Calculate diameter at this node
                diameter = max(diameter, max_height1 + max_height2)
                return max_height1, diameter

            # Perform DFS from an arbitrary node (assume node 0 is root)
            _, diameter = dfs(0, -1)

            # Height is the maximum single path length from the root
            height = (diameter + 1) // 2  # Approximate tree height
            return diameter, height

        # Calculate the diameter and height for both trees
        diameter1, height1 = find_tree_diameter_and_height(edges1)
        diameter2, height2 = find_tree_diameter_and_height(edges2)

        # Return the minimum diameter after merging the two trees
        return max(diameter1, diameter2, height1 + height2 + 1)

# Unit Test
if __name__ == "__main__":
    solution = Solution()

    # Example Test Cases
    edges1 = [[0, 1], [1, 2], [1, 3]]
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]

    # Call the function and print the output
    print("Test Case 1:", solution.minimumDiameterAfterMerge(edges1, edges2))  # Expected output: 5

    # Additional Test Cases
    edges3 = [[0, 1]]
    edges4 = [[0, 1], [1, 2], [2, 3]]

    print("Test Case 2:", solution.minimumDiameterAfterMerge(edges3, edges4))  # Expected output: 4

# Python documentation references:
# - `defaultdict`: https://docs.python.org/3/library/collections.html#collections.defaultdict
# - Depth-First Search (DFS): https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter
