'''
Leetcode 3445 Maximum Difference Between Even and Odd Frequency II

You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:
subs has a size of at least k.
Character a has an odd frequency in subs.
Character b has an even frequency in subs.
Return the maximum difference.
Note that subs can contain more than 2 distinct characters. 

Example 1:
        Input: s = "12233", k = 4
        Output: -1
        Explanation: For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

Example 2:
        Input: s = "1122211", k = 3
        Output: 1
        Explanation: For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

Example 3:
        Input: s = "110", k = 3
        Output: -1 

Constraints:
        3 <= s.length <= 3 * 104
        s consists only of digits '0' to '4'.
        The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
        1 <= k <= s.length
'''


# Let's verify the original logic and test correctness using the original function.

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        inf = float('inf')

        def solve(a, b):
            ca, cb = 0, 0
            res = -inf
            oo, oe, eo, ee = [], [], [], [(-1, 0, 0, 0)]  # (idx, ca, cb, min(ca-cb) before idx)

            def find(pref_arr, cur_idx, ca, cb):
                if ca == 0 or cb == 0:
                    return inf
                t_idx = cur_idx - k
                if t_idx < -1:
                    return inf
                if pref_arr[0][0] > t_idx or pref_arr[0][1] >= ca or pref_arr[0][2] >= cb:
                    return inf
                l, r = 0, len(pref_arr) - 1
                while l < r:
                    m = (l + r + 1) // 2
                    if pref_arr[m][0] <= t_idx and pref_arr[m][1] < ca and pref_arr[m][2] < cb:
                        l = m
                    else:
                        r = m - 1
                return pref_arr[l][3]

            def update(i, ca, cb, prev):
                if not prev:
                    prev.append((i, ca, cb, ca - cb))
                else:
                    prev.append((i, ca, cb, min(ca - cb, prev[-1][3])))

            n = len(s)
            for i, c in enumerate(s):
                if c == a:
                    ca += 1
                if c == b:
                    cb += 1
                if ca % 2 == 1 and cb % 2 == 0 and ee:
                    res = max(res, ca - cb - find(ee, i, ca, cb))
                if ca % 2 == 1 and cb % 2 == 1 and eo:
                    res = max(res, ca - cb - find(eo, i, ca, cb))
                if ca % 2 == 0 and cb % 2 == 0 and oe:
                    res = max(res, ca - cb - find(oe, i, ca, cb))
                if ca % 2 == 0 and cb % 2 == 1 and oo:
                    res = max(res, ca - cb - find(oo, i, ca, cb))

                if ca % 2 == 1 and cb % 2 == 0:
                    update(i, ca, cb, oe)
                if ca % 2 == 1 and cb % 2 == 1:
                    update(i, ca, cb, oo)
                if ca % 2 == 0 and cb % 2 == 0:
                    update(i, ca, cb, ee)
                if ca % 2 == 0 and cb % 2 == 1:
                    update(i, ca, cb, eo)
            return res

        chars = '01234'
        res = -inf
        for a in chars:
            for b in chars:
                if a != b:
                    res = max(res, solve(a, b))
        return res


# Test with the provided example
test_input = "0123401234"
k = 2
solution = Solution()
solution.maxDifference(test_input, k)
