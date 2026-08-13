'''

Leetcode 2213 Longest Substring of One Repeating Character
 
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
k == queryCharacters.length == queryIndices.length
1 <= k <= 105
queryCharacters consists of lowercase English letters.
0 <= queryIndices[i] < s.length

'''


from typing import List

class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        s = list(s)

        # Segment tree node stores:
        # left_char, right_char
        # prefix length of same char
        # suffix length of same char
        # maximum repeating substring length
        size = 4 * n

        left_char = [""] * size
        right_char = [""] * size
        prefix = [0] * size
        suffix = [0] * size
        best = [0] * size
        seg_len = [0] * size

        def pull(node):
            L = node * 2
            R = node * 2 + 1

            seg_len[node] = seg_len[L] + seg_len[R]
            left_char[node] = left_char[L]
            right_char[node] = right_char[R]

            prefix[node] = prefix[L]
            suffix[node] = suffix[R]
            best[node] = max(best[L], best[R])

            # The runs can connect across the middle.
            if right_char[L] == left_char[R]:
                combined = suffix[L] + prefix[R]
                best[node] = max(best[node], combined)

                # Entire left segment is one repeating run,
                # so prefix can extend into right segment.
                if prefix[L] == seg_len[L]:
                    prefix[node] = seg_len[L] + prefix[R]

                # Entire right segment is one repeating run,
                # so suffix can extend into left segment.
                if suffix[R] == seg_len[R]:
                    suffix[node] = seg_len[R] + suffix[L]

        def build(node, l, r):
            if l == r:
                left_char[node] = right_char[node] = s[l]
                prefix[node] = suffix[node] = best[node] = 1
                seg_len[node] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node)

        def update(node, l, r, idx, ch):
            if l == r:
                left_char[node] = right_char[node] = ch
                # lengths stay 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            pull(node)

        build(1, 0, n - 1)

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            # Updating to the same character changes nothing.
            if s[idx] != ch:
                s[idx] = ch
                update(1, 0, n - 1, idx, ch)

            ans.append(best[1])

        return ans
