'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

Example 1:
        Input: s = "bcabc"
        Output: "abc"
        
Example 2:
        Input: s = "cbacdcbc"
        Output: "acdb"

Constraints:
        1 <= s.length <= 104
        s consists of lowercase English letters.
'''

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    ans = []
    count = collections.Counter(s)
    used = [False] * 26

    for c in s:
      count[c] -= 1
      if used[ord(c) - ord('a')]:
        continue
      while ans and ans[-1] > c and count[ans[-1]] > 0:
        used[ord(ans[-1]) - ord('a')] = False
        ans.pop()
      ans.append(c)
      used[ord(ans[-1]) - ord('a')] = True

    return ''.join(ans)
