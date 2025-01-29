'''

Leetcode 648 Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. 
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with
the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.

Example 1:        
        Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"
        
Example 2:
        Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
        Output: "a a b c"
 

Constraints:
        1 <= dictionary.length <= 1000
        1 <= dictionary[i].length <= 100
        dictionary[i] consists of only lower-case letters.
        1 <= sentence.length <= 106
        sentence consists of only lower-case letters and spaces.
        The number of words in sentence is in the range [1, 1000]
        The length of each word in sentence is in the range [1, 1000]
        Every two consecutive words in sentence will be separated by exactly one space.
        sentence does not have leading or trailing spaces.

'''

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.endOfWord = True

    def getRoot(self, word: str) -> str:
        curr = self.root
        prefix = []
        for c in word:
            if c not in curr.children:
                break
            curr = curr.children[c]
            prefix.append(c)
            if curr.endOfWord:
                return ''.join(prefix)
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.addWord(word)

        words = sentence.split()
        replaced_words = [self.getRoot(word) for word in words]

        return ' '.join(replaced_words)

# Secons solution
from typing import List

class UnionFind:
    """
    Union-Find with path compression and union by rank.
    Used to detect cycles in an undirected graph.
    """

    def __init__(self, n: int):
        """
        Initializes the Union-Find structure.

        Parameters:
        ----------
        n : int
            The number of elements/nodes in the Union-Find.
        """
        self.id = list(range(n))  # Each node is its own parent initially.
        self.rank = [0] * n       # Rank is initialized to 0 for all nodes.

    def unionByRank(self, u: int, v: int) -> bool:
        """
        Tries to union two nodes u and v.

        Parameters:
        ----------
        u : int
            First node.
        v : int
            Second node.

        Returns:
        -------
        bool
            True if union is successful, False if u and v are already connected (cycle).
        """
        i = self._find(u)  # Find root of u.
        j = self._find(v)  # Find root of v.

        if i == j:
            return False  # A cycle is detected.

        # Union by rank to keep the tree shallow.
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[i] = j
            self.rank[j] += 1

        return True

    def _find(self, u: int) -> int:
        """
        Finds the root of a node u with path compression.

        Parameters:
        ----------
        u : int
            Node to find the root of.

        Returns:
        -------
        int
            The root of the node u.
        """
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])  # Path compression
        return self.id[u]


class Solution:
    """
    Solution to find the redundant connection in a graph.
    """

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds the redundant edge in a graph.

        Parameters:
        ----------
        edges : List[List[int]]
            List of edges in the graph, where each edge is a pair of integers [u, v].

        Returns:
        -------
        List[int]
            The redundant edge that forms a cycle.
        """
        # Initialize Union-Find for n+1 nodes (1-based indexing).
        uf = UnionFind(len(edges) + 1)

        # Iterate through all edges.
        for edge in edges:
            # If union fails, the edge is redundant.
            if not uf.unionByRank(edge[0], edge[1]):
                return edge


# Example Usage
if __name__ == "__main__":
    edges = [[1, 2], [1, 3], [2, 3]]
    solution = Solution()
    print("Redundant edge:", solution.findRedundantConnection(edges))  # Output: [2, 3]


# Unit Tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [2, 3])

    def test_case_2(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [1, 4])

    def test_case_3(self):
        edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
        self.assertEqual(self.solution.findRedundantConnection(edges), [1, 4])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)


"""
### Key Changes Made:
1. **Docstrings:** Added detailed explanations for each class, method, and function.
2. **Comments:** Added comments for every significant line to improve readability.
3. **Optimized Union-Find:** Used path compression and union by rank for efficiency.
4. **Example Implementation:** Provided a practical example with the graph edges.
5. **Unit Tests:** Added `unittest` cases to verify correctness across different scenarios.
6. **Formatting:** Clean and PEP8-compliant code.

### Time Complexity:
- **Union-Find Operations (`find`, `union`):** Nearly O(1) (amortized using path compression and union by rank).
- **Overall Complexity:** O(E) where E is the number of edges.

### Space Complexity:
- O(N) for storing `id` and `rank` arrays.

### Reference:
For Union-Find details, refer to:
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


