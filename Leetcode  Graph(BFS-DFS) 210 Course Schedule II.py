'''
Leetcode 210 Course Schedule II
 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.


'''

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    ans = []
    graph = [[] for _ in range(numCourses)]
    inDegree = [0] * numCourses
    q = collections.deque()

    # Build graph
    for v, u in prerequisites:
      graph[u].append(v)
      inDegree[v] += 1

    # Topology
    for i, degree in enumerate(inDegree):
      if degree == 0:
        q.append(i)

    while q:
      u = q.popleft()
      ans.append(u)
      for v in graph[u]:
        inDegree[v] -= 1
        if inDegree[v] == 0:
          q.append(v)

    return ans if len(ans) == numCourses else []


# Second Solution
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Determines the order of courses to finish all given the prerequisites.

        Parameters:
        - numCourses (int): Total number of courses labeled from 0 to numCourses-1.
        - prerequisites (List[List[int]]): List of prerequisite pairs where [a, b]
          means course `a` depends on course `b`.

        Returns:
        - List[int]: A list of course numbers in the order they should be taken.
          If it is impossible to complete all courses, return an empty list.
        """
        # Step 1: Create adjacency list and initialize data structures
        adj = [[] for _ in range(numCourses)]  # Adjacency list for graph representation
        indeg = [0] * numCourses  # Array to store in-degrees of nodes (courses)
        result = []  # To store the topological order
        queue = deque()  # Queue for BFS traversal

        # Step 2: Build the adjacency list and in-degree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)  # Add edge prereq -> course
            indeg[course] += 1         # Increment in-degree of course

        # Step 3: Add all courses with 0 in-degree to the queue
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)

        # Step 4: Process nodes with BFS
        while queue:
            course = queue.popleft()  # Remove a course with 0 in-degree
            result.append(course)     # Add it to the result (topological order)

            # Reduce in-degree of neighboring courses
            for neighbor in adj[course]:
                indeg[neighbor] -= 1  # Reduce in-degree by 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)  # If in-degree becomes 0, add to queue

        # Step 5: Check if topological sorting is possible
        if len(result) == numCourses:
            return result  # All courses can be completed
        else:
            return []  # Cycle detected or not all courses can be completed

