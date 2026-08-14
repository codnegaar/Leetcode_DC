'''
Leetcode 3090 Maximum Length Substring With Two Occurrences

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character. 

Example 1:
        Input: s = "bcbbbcba"
        Output: 4
        Explanation: The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:
        Input: s = "aaaa"
        Output: 2
        Explanation: The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
         
Constraints:
        2 <= s.length <= 100
        s consists only of lowercase English letters.
'''




class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        i = res = 0
        for j, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while count[c] > 2:
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
