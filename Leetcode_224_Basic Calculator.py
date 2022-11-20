'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.



'''

class Solution:
    def calculate(self, s: str) -> int:
        
        res = 0
        sign = 1
        num = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)     # get the full number
            elif c in "-+":
                res += sign * num
                num = 0                     # reset to zero after calculation
                sign = 1 if c == '+' else -1
            elif c == '(':                  # prep for calculation
                stack.append(res)           # cache previous calculation in a stack
                stack.append(sign)          # cache the sign in a stack
                sign, res = 1, 0            # reset sign and res
            elif c == ')':
                res += sign * num
                res *= stack.pop()          # calulate the sign before parentheses
                res += stack.pop()          # A sign (B)
                num = 0                     # reset to zero after calculation

        return res + num * sign

        
