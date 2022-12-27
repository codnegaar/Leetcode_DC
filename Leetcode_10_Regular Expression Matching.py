'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:
      Input: s = "aa", p = "a"
      Output: false
      Explanation: "a" does not match the entire string "aa".
      
Example 2:
      Input: s = "aa", p = "a*"
      Output: true
      Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
      Input: s = "ab", p = ".*"
      Output: true
      Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''
class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    m = len(s)
    n = len(p)
    # dp[i][j] := True if s[0..i) matches p[0..j)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    def isMatch(i: int, j: int) -> bool:
      return j >= 0 and p[j] == '.' or s[i] == p[j]

    for j, c in enumerate(p):
      if c == '*' and dp[0][j - 1]:
        dp[0][j + 1] = True

    for i in range(m):
      for j in range(n):
        if p[j] == '*':
          noRepeat = dp[i + 1][j - 1]  # Min index of '*' is 1
          doRepeat = isMatch(i, j - 1) and dp[i][j + 1]
          dp[i + 1][j + 1] = noRepeat or doRepeat
        elif isMatch(i, j):
          dp[i + 1][j + 1] = dp[i][j]

    return dp[m][n]
