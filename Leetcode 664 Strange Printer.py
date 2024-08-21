'''
Leetcode 664 Strange Printer

There is a strange printer with the following two special properties:
The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:
        Input: s = "aaabbb"
        Output: 2
        Explanation: Print "aaa" first and then print "bbb".

Example 2:
        Input: s = "aba"
        Output: 2
        Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.         

Constraints:
        1 <= s.length <= 100
        s consists of lowercase English letters.

'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self._calculate(0, n - 1, s, dp)

    def _calculate(self, i: int, j: int, s: str, dp: list) -> int:
        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        # Start with the assumption that the first character requires a print operation
        answer = 1 + self._calculate(i + 1, j, s, dp)
        
        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                # Try splitting the problem into subproblems and combining their results
                possible_answer = self._calculate(i, k - 1, s, dp) + self._calculate(k + 1, j, s, dp)
                answer = min(answer, possible_answer)
                
        dp[i][j] = answer
        return answer



