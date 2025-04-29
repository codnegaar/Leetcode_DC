'''
Leetcode 438 Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
        Input: s = "cbaebabacd", p = "abc"
        Output: [0,6]
        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "ABC".

Example 2:
        Input: s = "abab", p = "ab"
        Output: [0,1,2]
        Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".
         
Constraints:
        1 <= s.length, p.length <= 3 * 104
        s and p consist of lowercase English letters.

'''

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find all starting indices of p's anagrams in s.
        
        Parameters:
        s (str): The main input string.
        p (str): The pattern string whose anagrams we need to find.
        
        Returns:
        List[int]: List of starting indices where anagrams of p are found in s.
        """
        
        res = []
        len_p, len_s = len(p), len(s)
        
        # Early exit if pattern is longer than string
        if len_p > len_s:
            return res
        
        # Initialize frequency counters for p and the first window in s
        p_count = Counter(p)
        s_count = Counter(s[:len_p])
        
        # If first window matches, add index 0
        if s_count == p_count:
            res.append(0)
        
        # Slide the window over s
        for i in range(len_p, len_s):
            # Add one character (right side of the window)
            s_count[s[i]] += 1
            # Remove one character (left side of the window)
            s_count[s[i - len_p]] -= 1
            
            # Clean up zero-counts to keep counters light
            if s_count[s[i - len_p]] == 0:
                del s_count[s[i - len_p]]
            
            # Check if current window matches the pattern
            if s_count == p_count:
                res.append(i - len_p + 1)
        
        return res
