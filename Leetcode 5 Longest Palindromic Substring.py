'''
Leetcode 5 Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
A string is called a palindrome string if the reverse of that string is the same as the original string. 

Example 1:
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.
Example 2:
        Input: s = "cbbd"
        Output: "bb"

Constraints:
        1 <= s.length <= 1000
        s consist of only digits and English letters.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 0 or len(s) == 1):
            return s

        table = [[False]*len(s) for j in range(len(s))]
        # m stores the starting index of the palindrome
        m = None
        length = 1
        # strings of length 1 are always palindrome
        for i in range(len(s)):
            table[i][i] = True
            m = i
        # strings of length 2
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                table[i][i+1] = True
                m = i
                length = 2
        # strings of length 3 and greater
        for l in range(3, len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1
                # current string is palindrome if the starting character = ending character 
                # and the string in between is a palindrome which we check from the table constructed
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    m = i
                    length = l
        return s[m:m+length]
 
        
