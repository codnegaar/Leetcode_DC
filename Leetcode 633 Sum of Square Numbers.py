'''
Leetcode 633 Sum of Square Numbers

Given a non-negative integer c, decide whether there are two integers a and b such that a2 + b2 = c.

Example 1:
        Input: c = 5
        Output: true
        Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
        Input: c = 3
        Output: false 

Constraints:
        0 <= c <= 231 - 1
'''
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # Compute the maximum possible value for `a`
        max_a = int(sqrt(c))  

        # Iterate through all possible values of `a`
        for a in range(max_a + 1): 

            # Compute `b^2` as `c - a^2`
            b_squared = c - a * a  

            # Compute `b` as the integer square root of `b^2`
            b = int(sqrt(b_squared))  

            # Check if `b^2` is exactly equal to `b_squared`
            if b * b == b_squared:  

                # If such a pair `(a, b)` is found, return True
                return True  

        # If no such pair `(a, b)` is found, return False
        return False  

# Example usage:
solution = Solution()
print(solution.judgeSquareSum(5))  # Output: True, because 1^2 + 2^2 = 5
