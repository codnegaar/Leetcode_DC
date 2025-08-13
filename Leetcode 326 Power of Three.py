'''
Leetcode 326 Power of Three
 
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x. 

Example 1:
        Input: n = 27
        Output: true
        Explanation: 27 = 33

Example 2:
        Input: n = 0
        Output: false
        Explanation: There is no x where 3x = 0.
        
Example 3:
        Input: n = -1
        Output: false
        Explanation: There is no x where 3x = (-1).
 
Constraints:
        -231 <= n <= 231 - 1
'''

import unittest
from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determine whether an integer is a power of three.

        Parameters
        ----------
        n : int
            The integer to test. Any Python int is accepted (negative, zero, or positive).

        Returns
        -------
        bool
            True if `n` is a positive power of three (1, 3, 9, 27, ...), otherwise False.

        Notes
        -----
        - Uses an O(1) divisibility trick for the 32-bit signed integer range:
          the largest power of 3 in this range is 3**19 = 1_162_261_467.
          For any positive `n` within that range, `n` is a power of three iff
          `1_162_261_467 % n == 0`.
        - For larger integers, falls back to an O(log₃ n) loop.
        """
        MAX_POWER_OF_THREE_32 = 1_162_261_467  # 3**19: largest 32-bit signed power of three

        if n <= 0:              # Negative numbers and zero are not powers of three
            return False

        if n <= MAX_POWER_OF_THREE_32:  # O(1) check for most inputs
            return MAX_POWER_OF_THREE_32 % n == 0

        # Fallback for very large integers: keep dividing by 3
        while n % 3 == 0:
            n //= 3  # integer division to avoid floats

        return n == 1

 
