'''
Leetcode 3335 Total Characters in String After Transformations I

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:
If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
        Input: s = "abcyy", t = 2
        Output: 7
        Explanation:
                    First Transformation (t = 1):
                    'a' becomes 'b'
                    'b' becomes 'c'
                    'c' becomes 'd'
                    'y' becomes 'z'
                    'y' becomes 'z'
                    String after the first transformation: "bcdzz"
                    Second Transformation (t = 2):
                    'b' becomes 'c'
                    'c' becomes 'd'
                    'd' becomes 'e'
                    'z' becomes "ab"
                    'z' becomes "ab"
                    String after the second transformation: "cdeabab"
                    Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:
        Input: s = "azbk", t = 1
        Output: 5
        Explanation:
          First Transformation (t = 1):
          'a' becomes 'b'
          'z' becomes "ab"
          'b' becomes 'c'
          'k' becomes 'l'
          String after the first transformation: "babcl"
          Final Length of the string: The string is "babcl", which has 5 characters.
           

Constraints:
        1 <= s.length <= 105
        s consists only of lowercase English letters.
        1 <= t <= 105

'''
from collections import Counter
from string import ascii_lowercase

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        Applies a custom transformation `t` times on the frequency tuple of characters from 'a' to 'z'.

        Transformation rule:
        - At each step, the new sequence becomes:
          (last_element, first + last, middle_elements excluding first and last)

        Parameters:
        - s (str): Input lowercase string.
        - t (int): Number of transformation iterations.

        Returns:
        - int: Sum of transformed frequency values modulo 10^9 + 7.
        """

        # Get frequency list of all lowercase letters
        freq_map = Counter(s)
        freq = [freq_map.get(c, 0) for c in ascii_lowercase]  # List of 26 elements

        # Perform t transformations
        for _ in range(t):
            first = freq[0]
            last = freq[-1]
            middle = freq[1:-1]
            freq = [last, first + last] + middle  # Apply the transformation

        return sum(freq) % (10**9 + 7)
