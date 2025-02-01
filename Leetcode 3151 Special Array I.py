'''
Leetcode 3151 Special Array I

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

Example 1:
        Input: nums = [1]
        Output: true
        Explanation:
        There is only one element. So the answer is true.

Example 2:
        Input: nums = [2,1,4]
        Output: true
        Explanation:
        There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:
        Input: nums = [4,3,1,6]
        Output: false
        Explanation:
        nums[1] and nums[2] are both odd. So the answer is false.

Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 100
'''

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Determines if an array is 'special', meaning no two consecutive elements have the same parity (even or odd).

        :param nums: List of integers.
        :return: True if the array is special, otherwise False.

        Example:
        >>> Solution().isArraySpecial([1, 2, 3, 4])
        False
        >>> Solution().isArraySpecial([1, 2, 3, 8, 5])
        True
        """
        return all(nums[i] % 2 != nums[i + 1] % 2 for i in range(len(nums) - 1))


# Example Implementation
if __name__ == "__main__":
    nums = [1, 2, 3, 8, 5]
    solution = Solution()
    print(f"Is array special? {solution.isArraySpecial(nums)}")  # Output: True


# Unit Tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        self.assertTrue(self.solution.isArraySpecial([1, 2, 3, 8, 5]))
        self.assertFalse(self.solution.isArraySpecial([1, 2, 3, 4]))
        self.assertTrue(self.solution.isArraySpecial([2, 1, 4, 3]))
        self.assertFalse(self.solution.isArraySpecial([2, 4, 6, 8]))
        self.assertTrue(self.solution.isArraySpecial([5]))
        self.assertTrue(self.solution.isArraySpecial([]))  # Edge case: empty list

if __name__ == "__main__":
    unittest.main()
