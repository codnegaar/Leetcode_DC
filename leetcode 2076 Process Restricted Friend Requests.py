'''
Leetcode 2076 Process Restricted Friend Requests

You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.
You are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.
Initially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.
A friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.
Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is not.
Note: If uj and vj are already direct friends, the request is still successful.

Example 1:
        Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
        Output: [true,false]
        Explanation:
        Request 0: Person 0 and person 2 can be friends, so they become direct friends. 
        Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).

Example 2:
        Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
        Output: [true,false]
        Explanation:
        Request 0: Person 1 and person 2 can be friends, so they become direct friends.
        Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1 would be indirect friends (0--2--1).

Example 3:
        Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]
        Output: [true,false,true,false]
        Explanation:
        Request 0: Person 0 and person 4 can be friends, so they become direct friends.
        Request 1: Person 1 and person 2 cannot be friends since they are directly restricted.
        Request 2: Person 3 and person 1 can be friends, so they become direct friends.
        Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1 would be indirect friends (0--4--3--1). 

Constraints:
        2 <= n <= 1000
        0 <= restrictions.length <= 1000
        restrictions[i].length == 2
        0 <= xi, yi <= n - 1
        xi != yi
        1 <= requests.length <= 1000
        requests[j].length == 2
        0 <= uj, vj <= n - 1
        uj != vj

'''

from typing import List

class DSU:
    """
    Disjoint Set Union (Union-Find) with restrictions on union operations.
    """

    def __init__(self, n: int):
        """
        Initialize the DSU for n elements.

        Parameters:
        n (int): Number of elements (0-indexed up to n-1)
        """
        self.parent = list(range(n))
        self.size = [1] * n
        self.restrictions = [set() for _ in range(n)]

    def find(self, x: int) -> int:
        """
        Find the root of element x with path compression.

        Parameters:
        x (int): Element to find

        Returns:
        int: Root representative of x
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def add_restriction(self, x: int, y: int):
        """
        Add a mutual restriction between x and y.

        Parameters:
        x, y (int): Elements that should not end up in the same set
        """
        px, py = self.find(x), self.find(y)
        if px != py:
            self.restrictions[px].add(py)
            self.restrictions[py].add(px)

    def can_union(self, x: int, y: int) -> bool:
        """
        Check whether x and y can be safely united without violating restrictions.

        Parameters:
        x, y (int): Elements to check

        Returns:
        bool: True if they can be united, False otherwise
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        return py not in self.restrictions[px] and px not in self.restrictions[py]

    def union(self, x: int, y: int) -> bool:
        """
        Try to unite x and y while respecting restrictions.

        Parameters:
        x, y (int): Elements to unite

        Returns:
        bool: True if union is successful, False otherwise
        """
        if not self.can_union(x, y):
            return False

        px, py = self.find(x), self.find(y)
        if px != py:
            # Union by size
            if self.size[px] < self.size[py]:
                px, py = py, px

            self.parent[py] = px
            self.size[px] += self.size[py]

            # Merge restrictions
            for r in self.restrictions[py]:
                self.restrictions[r].remove(py)
                self.restrictions[r].add(px)
            self.restrictions[px].update(self.restrictions[py])
            self.restrictions[py].clear()

        return True


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        """
        Handle friend requests under restriction constraints.

        Parameters:
        n (int): Total number of users (0 to n-1)
        restrictions (List[List[int]]): Each pair [u, v] cannot be in the same group
        requests (List[List[int]]): Each pair [u, v] is a request to be in the same group

        Returns:
        List[bool]: True if the request is accepted, False otherwise
        """
        dsu = DSU(n)

        for u, v in restrictions:
            dsu.add_restriction(u, v)

        results = []
        for u, v in requests:
            results.append(dsu.union(u, v))

        return results
