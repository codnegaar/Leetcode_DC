'''
Leetcode 3201 Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:
(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
        Input: nums = [1,2,3,4]        
        Output: 4        
        Explanation: The longest valid subsequence is [1, 2, 3, 4].

Example 2:
        Input: nums = [1,2,1,1,2,1,2]
        Output: 6
        Explanation: The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:
        Input: nums = [1,3]
        Output: 2
        Explanation: The longest valid subsequence is [1, 3].

Constraints:
        2 <= nums.length <= 2 * 105
        1 <= nums[i] <= 107
'''
from typing import List
import unittest

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        Calculates the maximum length of a subarray where even and odd numbers alternate.
        Also considers the total count of only even or only odd numbers as potential max.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The maximum length found based on alternating patterns and total even/odd counts.
        """
        # Initialize counters
        changes = 1  # Start with 1 because the first element is the beginning of a valid sequence
        ones = 0     # Count of odd numbers
        zeroes = 0   # Count of even numbers

        # Determine the parity (odd/even) of the first number
        isOdd = nums[0] % 2 == 1
        if isOdd:
            ones += 1
        else:
            zeroes += 1

        # Loop through the array starting from index 1
        for i in range(1, len(nums)):
            currentIsOdd = nums[i] % 2 == 1

            # Count odd and even numbers
            if currentIsOdd:
                ones += 1
            else:
                zeroes += 1

            # If parity changed from previous, increment changes
            if currentIsOdd != isOdd:
                changes += 1
                isOdd = currentIsOdd  # Flip the flag

        # The maximum is either:
        # - the longest alternating sequence (changes)
        # - or all odd numbers
        # - or all even numbers
        return max(changes, ones, zeroes)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print("Result:", sol.maximumLength([1, 2, 3, 4, 5, 6]))  # Output should be 6 (fully alternating)

# Unit test
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_alternating(self):
        self.assertEqual(self.solution.maximumLength([1, 2, 3, 4, 5, 6]), 6)

    def test_all_odds(self):
        self.assertEqual(self.solution.maximumLength([1, 3, 5, 7]), 4)

    def test_all_evens(self):
        self.assertEqual(self.solution.maximumLength([2, 4, 6, 8]), 4)

    def test_mixed(self):
        self.assertEqual(self.solution.maximumLength([1, 1, 1, 2, 2, 2]), 3)

    def test_single(self):
        self.assertEqual(self.solution.maximumLength([7]), 1)

# Run unit tests
unittest.main(argv=[''], exit=False)

"""
🔧 Changes Made:
- Removed redundant branches.
- Combined parity check and counter update in one pass.
- Used a single loop with constant-time operations (O(n)).
- Added inline comments and full docstring.
- Added unit tests using unittest.
- Added example usage in __main__.

📚 Python Reference:
- List type hint: https://docs.python.org/3/library/typing.html#typing.List
- Modulo operator (%): https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
- unittest module: https://docs.python.org/3/library/unittest.html
"""
