'''
Leetcode 3163 String Compression III

Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While the word is not empty, use the following operation:
        Remove a maximum length prefix of a word made of a single character c repeating at most 9 times.
        Append the length of the prefix followed by c to comp.
        Return the string comp.

Example 1:
        Input: word = "abcde"
        Output: "1a1b1c1d1e"
        Explanation: Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
                                      For each prefix, append "1" followed by the character to comp.

Example 2:
        Input: word = "aaaaaaaaaaaaaabb"
        Output: "9a5a2b"
        Explanation: Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
        
                                      For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
                              For prefix "aaaaa", append "5" followed by "a" to comp.
                              For prefix "bb", append "2" followed by "b" to comp.
 
Constraints:
        1 <= word.length <= 2 * 105
        word consists only of lowercase English letters.

'''

class Solution:
    def compressedString(self, word: str) -> str:
        """
        Compresses a string using a basic RLE (Run Length Encoding) approach,
        where consecutive characters are represented by their count followed by
        the character, with a maximum count of 9 for any character.

        Parameters:
        - word (str): The input string to be compressed.

        Returns:
        - str: The compressed string representation.
        """
        compressed = []  # Use a list for efficient concatenation
        count = 1  # Initialize count of consecutive characters
        n = len(word)  # Length of the input string

        # Iterate through the string starting from the second character
        for i in range(1, n):
            # Check if current character is the same as the previous one
            if word[i] == word[i - 1] and count < 9:
                count += 1  # Increment count if the character is the same
            else:
                # Append count and character to the result list
                compressed.append(f"{count}{word[i - 1]}")
                count = 1  # Reset count for the new character

        # Append the last character sequence
        compressed.append(f"{count}{word[-1]}")
        
        # Join all parts of compressed list into a single string
        return ''.join(compressed)
