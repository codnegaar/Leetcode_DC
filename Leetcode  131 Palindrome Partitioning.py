'''
131 Palindrome Partitioning
 
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

class Solution:
  def partition(self, s: str) -> List[List[str]]:
    ans = []

    def isPalindrome(s: str) -> bool:
      return s == s[::-1]

    def dfs(s: str, j: int, path: List[str], ans: List[List[str]]) -> None:
      if j == len(s):
        ans.append(path)
        return

      for i in range(j, len(s)):
        if isPalindrome(s[j: i + 1]):
          dfs(s, i + 1, path + [s[j: i + 1]], ans)

    dfs(s, 0, [], ans)
    return ans
