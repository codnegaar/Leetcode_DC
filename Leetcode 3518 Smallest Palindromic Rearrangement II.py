'''
Leetcode 3518 Smallest Palindromic Rearrangement II

You are given a palindromic string s and an integer k.
Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.
Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once. 

Example 1:
          Input: s = "abba", k = 2
          Output: "baab"
          Explanation:
          The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
          Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".

Example 2:
        Input: s = "aa", k = 2
        Output: ""
        Explanation:
        There is only one palindromic rearrangement: "aa".
        The output is an empty string since k = 2 exceeds the number of possible rearrangements.

Example 3:
        Input: s = "bacab", k = 1
        Output: "abcba"
        Explanation:
        The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
        Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
 
Constraints:
        1 <= s.length <= 104
        s consists of lowercase English letters.
        s is guaranteed to be palindromic.
        1 <= k <= 106
'''

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def comb(n: int, m: int, k_limit: int) -> int:
            res = 1
            m = min(m, n - m)

            for i in range(1, m + 1):
                res = res * (n - i + 1) // i
                if res > k_limit:
                    return k_limit + 1
            return res

        partition = len(s) // 2
        bucket = [0] * 26

        for i in range(partition):
            bucket[ord(s[i]) - 97] += 1

        def permutations(rem: int) -> int:
            ways = 1
            for i in range(26):
                if bucket[i] == 0:
                    continue

                ways *= comb(rem, bucket[i], k)
                if ways > k:
                    break
                rem -= bucket[i]
            return ways

        left_chars = []
        start_index = 1

        for pos in range(partition):
            for i in range(26):
                if bucket[i] == 0:
                    continue

                bucket[i] -= 1

                ways = permutations(partition - pos - 1)
                if start_index + ways > k:
                    left_chars.append(chr(i + 97))
                    break

                bucket[i] += 1
                start_index += ways

        if len(left_chars) < partition:
            return ""

        mid = s[partition] if len(s) % 2 != 0 else ""
        left_str = "".join(left_chars)
        right_str = left_str[::-1]

        return left_str + mid + right_str
