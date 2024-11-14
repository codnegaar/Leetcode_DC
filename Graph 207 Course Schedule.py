'''

207 Course Schedule
 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. So it is possible.

Example 2:
        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.


'''

from enum import Enum

class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    state = [State.kInit] * numCourses

    for a, b in prerequisites:
      graph[b].append(a)

    def hasCycle(u: int) -> bool:
      if state[u] == State.kVisiting:
        return True
      if state[u] == State.kVisited:
        return False

      state[u] = State.kVisiting
      if any(hasCycle(v) for v in graph[u]):
        return True
      state[u] = State.kVisited

      return False

    return not any(hasCycle(i) for i in range(numCourses))


# second solution:

from enum import Enum
from typing import List

class State(Enum):
    kInit = 0
    kVisiting = 1
    kVisited = 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given the prerequisites.
        
        Args:
            numCourses (int): The total number of courses.
            prerequisites (List[List[int]]): A list of prerequisite pairs where 
                                             each pair [a, b] indicates that course b 
                                             must be taken before course a.
        
        Returns:
            bool: True if it is possible to complete all courses, False otherwise.
        """
        # Create a graph represented as an adjacency list for the courses
        graph = [[] for _ in range(numCourses)]
        # Create an array to store the state of each course (initial, visiting, visited)
        state = [State.kInit] * numCourses

        # Build the graph from prerequisites list
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Function to check if there is a cycle starting from a given course
        def hasCycle(course: int) -> bool:
            if state[course] == State.kVisiting:
                return True  # A cycle is detected
            if state[course] == State.kVisited:
                return False  # Course has already been processed
            
            # Mark the course as currently being visited
            state[course] = State.kVisiting
            # Recursively visit all the adjacent courses
            for next_course in graph[course]:
                if hasCycle(next_course):
                    return True  # Cycle detected

            # Mark the course as completely processed
            state[course] = State.kVisited
            return False

        # Check each course for cycles
        for course in range(numCourses):
            if hasCycle(course):
                return False

        # If no cycle is detected for any course, return True
        return True

# Example usage:
# solution = Solution()
# print(solution.canFinish(2, [[1, 0]]))  # Should return True
# print(solution.canFinish(2, [[1, 0], [0, 1]]))  # Should return False

