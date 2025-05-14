'''
Leetcode 3337 Total Characters in String After Transformations II

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:
Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo 109 + 7. 

Example 1:
Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
Output: 7
Explanation: First Transformation (t = 1):
            'a' becomes 'b' as nums[0] == 1
            'b' becomes 'c' as nums[1] == 1
            'c' becomes 'd' as nums[2] == 1
            'y' becomes 'z' as nums[24] == 1
            'y' becomes 'z' as nums[24] == 1
            String after the first transformation: "bcdzz"
            Second Transformation (t = 2):
            
            'b' becomes 'c' as nums[1] == 1
            'c' becomes 'd' as nums[2] == 1
            'd' becomes 'e' as nums[3] == 1
            'z' becomes 'ab' as nums[25] == 2
            'z' becomes 'ab' as nums[25] == 2
            String after the second transformation: "cdeabab"
            Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:
Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
Output: 8
Explanation: First Transformation (t = 1):
            'a' becomes 'bc' as nums[0] == 2
            'z' becomes 'ab' as nums[25] == 2
            'b' becomes 'cd' as nums[1] == 2
            'k' becomes 'lm' as nums[10] == 2
            String after the first transformation: "bcabcdlm"
            Final Length of the string: The string is "bcabcdlm", which has 8 characters.

Constraints:
        1 <= s.length <= 105
        s consists only of lowercase English letters.
        1 <= t <= 109
        nums.length == 26
        1 <= nums[i] <= 25
'''

from collections import Counter
from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        Calculate the total number of characters in the string  's' after `t` transformations,
        where each character can change into a set of others defined by `nums`.

        Parameters:
        - s (str): The initial lowercase alphabet string.
        - t (int): Number of times the transformation should be applied.
        - nums (List[int]): An array of 26 integers; each index `i` indicates how many characters
                            forward (circularly) character `chr(i+97)` can change into.

        Returns:
        - int: The total number of characters in the transformed string modulo 1_000_000_007.
        """
        MOD = 10**9 + 7
        ALPHABET_SIZE = 26

        # Build initial frequency vector (1x26 matrix)
        def build_initial_vector(s: str) -> List[List[int]]:
            freq_vector = [0] * ALPHABET_SIZE
            for char, count in Counter(s).items():
                freq_vector[ord(char) - ord('a')] = count
            return [freq_vector]

        # Build transformation matrix (26x26)
        def build_transformation_matrix(nums: List[int]) -> List[List[int]]:
            matrix = [[0] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
            for i, shift in enumerate(nums):
                for j in range(shift):
                    target = (i + 1 + j) % ALPHABET_SIZE
                    matrix[i][target] = 1
            return matrix

        # Matrix multiplication
        def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            result = [[0] * len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    total = 0
                    for k in range(len(A[0])):
                        total = (total + A[i][k] * B[k][j]) % MOD
                    result[i][j] = total
            return result

        # Matrix exponentiation
        def matrix_power(matrix: List[List[int]], exponent: int) -> List[List[int]]:
            if exponent == 1:
                return matrix
            half = matrix_power(matrix, exponent // 2)
            squared = multiply(half, half)
            return squared if exponent % 2 == 0 else multiply(matrix, squared)

        # Prepare matrices
        A = build_initial_vector(s)                 # 1x26
        B = build_transformation_matrix(nums)      # 26x26

        # Apply matrix exponentiation and multiply with an initial state
        B_exp = matrix_power(B, t)
        final_vector = multiply(A, B_exp)

        # Return the total number of characters after all transformations
        return sum(final_vector[0]) % MOD
