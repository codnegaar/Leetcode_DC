'''
Leetcode 3003 Maximize the Number of Partitions After Operations

You are given a string s and an integer k.
First, you are allowed to change at most one index in s to another lowercase English letter.
After that, do the following partitioning operation until s is empty:
        Choose the longest prefix of s containing at most k distinct characters.
        Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
        Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

Example 1:
        Input: s = "accca", k = 2
        Output: 3
        Explanation:
        The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".
        Then we perform the operations:
        The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
        Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
        Finally, we remove "a" and s becomes empty, so the procedure ends.
        Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:
        Input: s = "aabaab", k = 3
        Output: 1
        Explanation: Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:
        Input: s = "xxyz", k = 1
        Output: 4
        Explanation:
        The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.
        Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

Constraints:
        1 <= s.length <= 104
        s consists only of lowercase English letters.
        1 <= k <= 26
'''

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i, mask, remain):
            nonlocal n

            # base
            if i >= n:
                return 0

            # seen before
            if (i, mask, remain) in memo:
                return memo[(i, mask, remain)]

            # otherwise; compute memo[(i, mask, remain)]

            # pull out the current charecter and its index
            ch = s[i]
            ind = ord(ch) - ord('a')
            char_bit = 1 << ind                # convert ind to charcter bit
            
            new_mask = mask | char_bit         # include ch in the prefix
            distinct = new_mask.bit_count()    # count unique charecters

            # case1; skip doing the change at index i
            skip = 0
            # not valid; add 1 and recur from index i + 1 with char_bit
            if distinct > k:
                skip = 1 + dfs(i + 1, char_bit, remain)

            # valid; include ch into the current prefix and recur from index i + 1
            else:
                skip = dfs(i + 1, new_mask, remain)

            # case2; pick doing the change at index i
            pick = 0
            if remain > 0:
                # search for next valid charecter
                for ch in range(26):
                    char_bit = 1 << ch                 # convert ind to charcter bit
                    new_mask = mask | char_bit         # include ch in the prefix
                    distinct = new_mask.bit_count()    # count unique charecters

                    # not valid; add 1 and recur from index i + 1 with char_bit
                    if distinct > k:
                        temp = 1 + dfs(i + 1, char_bit, remain - 1)
                        pick = max(pick, temp)
                    
                    # valid; include ch into the current prefix and recur from index i + 1
                    else:
                        temp = dfs(i + 1, new_mask, remain - 1)
                        pick = max(pick, temp)

            # compare
            memo[(i, mask, remain)] = max(skip, pick)

            return memo[(i, mask, remain)]

        n = len(s)

        # memo[(i, mask, remain)] := maximum number of resulting partitions partitions starting at index i with total mask value for the prefix with remain change count
        memo = dict()

        return 1 + dfs(0, 0, 1)
