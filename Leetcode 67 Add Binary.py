'''
67  Add Binary
 
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
