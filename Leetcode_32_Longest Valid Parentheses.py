'''

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

        Input: s = "(()"
        Output: 2
        Explanation: The longest valid parentheses substring is "()".
        
Example 2:

        Input: s = ")()())"
        Output: 4
        Explanation: The longest valid parentheses substring is "()()".
        
Example 3:
        Input: s = ""
        Output: 0
 
 Constraints:
        0 <= s.length <= 3 * 104
        s[i] is '(', or ')'.

'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
            s2 = ')' + s
            # dp[i] := Length of longest valid parentheses substring of s2[1..i]
            dp = [0] * len(s2)

            for i in range(1, len(s2)):
                if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

            return max(dp)
