'''

Leetcode 3110  Score of a String.py

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s. 

Example 1:
    Input: s = "hello"
    Output: 13
    Explanation:
            The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s 
            would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:
    Input: s = "zaz"
    Output: 50
    Explanation:
           The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
    

Constraints:
     2 <= s.length <= 100
     s consists only of lowercase English letters.

'''
class Solution:
    def scoreOfString(self, input_string: str) -> int:
        """
        Calculate and return the sum of absolute differences between the ASCII values
        of consecutive characters in the given string.

        :param input_string: The string to be processed
        :return: The calculated score as an integer
        """
        score = 0
        # Iterate over the string using a window of two characters
        for char1, char2 in zip(input_string, input_string[1:]):
            score += abs(ord(char1) - ord(char2))
        return score




