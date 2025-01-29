'''
Leetcode 70 Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

Example 2:
        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
 
Constraints:
        1 <= n <= 45

'''


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two =1,1
        for i in range(n-1):
            temp  = one
            one = one + two
            two = temp
        return one


# Solution 2 
class Solution:
    """
    A class to solve the climbing stairs problem using an optimized Fibonacci approach.

    The problem follows the Fibonacci sequence because at each step, you can either take 
    one or two steps, leading to the recurrence relation: f(n) = f(n-1) + f(n-2).
    """

    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to climb `n` stairs 
        given that you can take 1 or 2 steps at a time.

        Parameters:
        n (int): The number of stairs.

        Returns:
        int: The number of distinct ways to climb `n` stairs.
        """

        # Base cases: if n is 1 or 2, return n directly
        if n <= 2:
            return n

        # Initialize two variables for Fibonacci computation
        prev, curr = 1, 2

        # Compute Fibonacci iteratively up to n
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr  # Efficient tuple unpacking

        return curr


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    stairs = 5  # Example input
    print(f"Distinct ways to climb {stairs} stairs: {solution.climbStairs(stairs)}")


# Unit Tests
import unittest

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        """Initialize the solution instance before running tests."""
        self.solution = Solution()

    def test_cases(self):
        """Test various cases for the climbStairs function."""
        self.assertEqual(self.solution.climbStairs(1), 1)  # Only one way for 1 stair
        self.assertEqual(self.solution.climbStairs(2), 2)  # Two ways: (1+1) or (2)
        self.assertEqual(self.solution.climbStairs(3), 3)  # Three ways: (1+1+1), (1+2), (2+1)
        self.assertEqual(self.solution.climbStairs(4), 5)  # Five ways
        self.assertEqual(self.solution.climbStairs(5), 8)  # Eight ways
        self.assertEqual(self.solution.climbStairs(10), 89)  # Larger case

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""
# Improvements Made:
1. **Efficiency Improvement**: 
   - The original implementation used `O(n)` time and `O(1)` space, but used extra assignments.
   - The new implementation maintains `O(n)` time and `O(1)` space but optimizes with tuple unpacking.

2. **Code Readability**:
   - Added proper docstrings for class and function.
   - Added meaningful comments for each step.

3. **Edge Case Handling**:
   - Directly return `n` for cases where `n` is `1` or `2`, avoiding unnecessary iteration.

4. **Unit Testing**:
   - Implemented `unittest` framework to validate multiple test cases.

5. **Example Implementation**:
   - Included a real-world example for easy understanding.

# Reference:
- Python Official Documentation on Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
"""

