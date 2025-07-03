'''
Leetcode 3304 Find the K-th Character in String Game I

Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k.
Now Bob will ask Alice to perform the following operation forever:
Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
Note that the character 'z' can be changed to 'a' in the operation. 

Example 1:
        Input: k = 5
        Output: "b"
        Explanation: Initially, word = "a". We need to do the operation three times:        
                Generated string is "b", word becomes "ab".
                Generated string is "bc", word becomes "abbc".
                Generated string is "bccd", word becomes "abbcbccd".

Example 2:
        Input: k = 10
        Output: "c" 

Constraints:
        1 <= k <= 500

'''

import string

class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Returns the k-th character in a recursively defined string where:
        - Start with 'a'
        - Each character c expands to c + next_letter(c), recursively
        - next_letter wraps from 'z' to 'a'

        Parameters:
        k (int): The 1-based index of the character to retrieve

        Returns:
        str: The k-th character in the infinite expansion
        """
        next_char = {c: string.ascii_lowercase[(i + 1) % 26] for i, c in enumerate(string.ascii_lowercase)}

        def get_kth(c: str, depth: int, target: int) -> str:
            """
            Simulate expansion tree without building full string.
            Returns the target-th character starting from character c,
            assuming each character expands into 2 at each level.

            c: current character
            depth: current depth in expansion tree
            target: index we are trying to find (1-based)
            """
            if depth == 0:
                return c

            mid = 2 ** (depth - 1)
            if target <= mid:
                return get_kth(c, depth - 1, target)
            else:
                return get_kth(next_char[c], depth - 1, target - mid)

        # Determine how many expansion steps are needed to reach at least k characters
        depth = 0
        while 2 ** depth < k:
            depth += 1

        return get_kth('a', depth, k)
