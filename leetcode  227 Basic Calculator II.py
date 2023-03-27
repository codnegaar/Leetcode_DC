'''
227 Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:
      Input: s = "3+2*2"
      Output: 7
      
Example 2:
      Input: s = " 3/2 "
      Output: 1
      
Example 3:
      Input: s = " 3+5 / 2 "
      Output: 5 

Constraints:
        1 <= s.length <= 3 * 105
        s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
        s represents a valid expression.
        All the integers in the expression are non-negative integers in the range [0, 231 - 1].
        The answer is guaranteed to fit in a 32-bit integer.

'''

class Solution:
  def calculate(self, s: str) -> int:
    ans = 0
    prevNum = 0
    currNum = 0
    op = '+'

    for i, c in enumerate(s):
      if c.isdigit():
        currNum = currNum * 10 + int(c)
      if not c.isdigit() and c != ' ' or i == len(s) - 1:
        if op == '+' or op == '-':
          ans += prevNum
          prevNum = (currNum if op == '+' else -currNum)
        elif op == '*':
          prevNum *= currNum
        elif op == '/':
          prevNum = int(prevNum / currNum)
        op = c
        currNum = 0

    return ans + prevNum


