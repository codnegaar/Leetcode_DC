'''
Leetcode 3333 Find the Original Typed String II

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.
Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
        Input: word = "aabbccdd", k = 7
        Output: 5
        Explanation: The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

Example 2:
        Input: word = "aabbccdd", k = 8
        Output: 1
        Explanation: The only possible string is "aabbccdd".

Example 3:
        Input: word = "aaabbb", k = 3
        Output: 8 

Constraints:
        1 <= word.length <= 5 * 105
        word consists only of lowercase English letters.
        1 <= k <= 2000
'''

class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Count the number of ways to construct the original string such that
        the number of same-character groups does not exceed k.

        Parameters:
        word (str): The input string with contiguous repeated characters.
        k (int): Maximum allowed number of same-character segments.

        Returns:
        int: Valid construction count modulo 1e9+7.
        """
        if not word:
            return 0

        # Step 1: Compress word into group sizes
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # Step 2: Total base ways: multiply group sizes
        total = 1
        for num in groups:
            total = (total * num) % self.MOD

        # If number of groups <= k, all are valid
        if k <= len(groups):
            return total

        # Step 3: DP to count invalid group combinations
        dp = [0] * k
        dp[0] = 1

        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp

        # Step 4: Subtract invalid configurations
        invalid = sum(dp[len(groups):k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD
