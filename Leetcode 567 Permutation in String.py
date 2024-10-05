'''
Leetcode 567 Permutation in String

Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false 

Constraints:
        1 <= s1.length, s2.length <= 104
        s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        # Initialize frequency counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # Check how many characters initially match between s1Count and s2Count
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Slide the window over s2
        for i in range(len(s2) - len(s1)):
            if matches == 26:  # All characters match
                return True

            # Right end of the window (incoming character)
            right_char = ord(s2[i + len(s1)]) - ord('a')
            # Left end of the window (outgoing character)
            left_char = ord(s2[i]) - ord('a')

            # Update the right end of the window
            s2Count[right_char] += 1
            if s2Count[right_char] == s1Count[right_char]:
                matches += 1
            elif s2Count[right_char] == s1Count[right_char] + 1:
                matches -= 1

            # Update the left end of the window
            s2Count[left_char] -= 1
            if s2Count[left_char] == s1Count[left_char]:
                matches += 1
            elif s2Count[left_char] == s1Count[left_char] - 1:
                matches -= 1

        # Final check for the last window
        return matches == 26
