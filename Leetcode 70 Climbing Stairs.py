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
from typing import List
from unittest import TestCase, main

class Solution:
    """
    A class to solve the climbing stairs problem using an optimized Fibonacci approach.

    The problem follows the Fibonacci sequence since at each step, you can either take 
    one or two steps, leading to the recurrence relation: f(n) = f(n-1) + f(n-2).
    """

    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to climb `n` stairs, 
        given that you can take 1 or 2 steps at a time.

        Args:
            n (int): The number of stairs.

        Returns:
            int: The number of distinct ways to climb `n` stairs.
        """
        if n == 0:
            return 0  # Edge case: No stairs to climb
        if n <= 2:
            return n  # Directly return for n=1 (1 way) or n=2 (2 ways)

        # Initialize variables for Fibonacci computation
        first, second = 1, 2

        # Iteratively compute the number of ways up to n
        for _ in range(3, n + 1):
            first, second = second, first + second  # Efficient tuple swapping

        return second


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    stairs = 5  # Example input
    print(f"Distinct ways to climb {stairs} stairs: {solution.climbStairs(stairs)}")


# Unit Tests
class TestClimbStairs(TestCase):
    """Test cases for the climbStairs function."""

    def setUp(self):
        """Initialize the solution instance before running tests."""
        self.solution = Solution()

    def test_edge_cases(self):
        """Test edge cases, including zero stairs."""
        self.assertEqual(self.solution.climbStairs(0), 0)  # No stairs to climb
        self.assertEqual(self.solution.climbStairs(1), 1)  # Only one way for 1 stair
        self.assertEqual(self.solution.climbStairs(2), 2)  # Two ways: (1+1) or (2)

    def test_standard_cases(self):
        """Test general cases with known Fibonacci sequence values."""
        self.assertEq
