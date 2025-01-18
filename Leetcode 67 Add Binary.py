'''
Leetcode 67  Add Binary
 
Given two binary strings a and b, return their sum as a binary string. 

Example 1:
        Input: a = "11", b = "1"
        Output: "100"
        
Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"
 

Constraints:
        1 <= a.length, b.length <= 104
        a and b consist only of '0' or '1' characters.
        Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))


# Second solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return their sum as a binary string.

        Parameters:
        a (str): The first binary string.
        b (str): The second binary string.

        Returns:
        str: The binary string representing the sum of `a` and `b`.
        """
        result = []  # List to store the binary digits of the result
        carry = 0  # Variable to store the carry during addition
        i, j = len(a) - 1, len(b) - 1  # Pointers to traverse the strings from the end

        # Loop through both strings and the carry
        while i >= 0 or j >= 0 or carry:
            if i >= 0:  # Add digit from string `a` if within bounds
                carry += int(a[i])
                i -= 1
            if j >= 0:  # Add digit from string `b` if within bounds
                carry += int(b[j])
                j -= 1
            
            result.append(str(carry % 2))  # Append the current binary digit to the result
            carry //= 2  # Update the carry

        return ''.join(reversed(result))  # Reverse the result list and return it as a string


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    a = "1010"
    b = "1011"
    print(f"Sum of {a} and {b} in binary: {solution.addBinary(a, b)}")  # Expected output: "10101"


# Unit Tests
import unittest

class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")

    def test_case2(self):
        self.assertEqual(self.solution.addBinary("0", "0"), "0")

    def test_case3(self):
        self.assertEqual(self.solution.addBinary("1", "1"), "10")

    def test_case4(self):
        self.assertEqual(self.solution.addBinary("111", "111"), "1110")

    def test_case5(self):
        self.assertEqual(self.solution.addBinary("110", "1"), "111")

if __name__ == "__main__":
    # Run the test suite
    unittest.main()

