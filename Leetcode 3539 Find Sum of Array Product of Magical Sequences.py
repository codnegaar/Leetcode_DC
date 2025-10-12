'''

Leetcode 3539 Find Sum of Array Product of Magical Sequences
 
You are given two integers, m and k, and an integer array nums.

A sequence of integers seq is called magical if:
        seq has a size of m.
        0 <= seq[i] < nums.length
        The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
        The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).
        Return the sum of the array products for all valid magical sequences.
        Since the answer may be large, return it modulo 109 + 7.
A set bit refers to a bit in the binary representation of a number that has a value of 1.

Example 1:
Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]
Output: 991600007
Explanation: All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.

Example 2:
          Input: m = 2, k = 2, nums = [5,4,3,2,1]
          Output: 170
          Explanation: The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].

Example 3:
        Input: m = 1, k = 1, nums = [28]        
        Output: 28        
        Explanation: The only magical sequence is [0].

Constraints:
        1 <= k <= m <= 30
        1 <= nums.length <= 50
        1 <= nums[i] <= 108

'''

from collections import defaultdict
from typing import List

class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # factorials and inverse factorials
        f = [1] * (M + 1)
        for i in range(1, M + 1):
            f[i] = f[i - 1] * i % MOD

        inv_f = [1] * (M + 1)
        inv_f[M] = pow(f[M], MOD - 2, MOD)
        for i in range(M, 0, -1):
            inv_f[i - 1] = inv_f[i] * i % MOD

        # dp[m1][k] = dict: m2 -> ways
        # Start: i = 0, m1 = 0, k = 0, m2 = 0 has 1 way.
        dp = [ [defaultdict(int) for _ in range(K + 1)] for __ in range(M + 1) ]
        dp[0][0][0] = 1

        for i in range(n):
            x = nums[i] % MOD

            # pow_c[c] = x^c mod for c = 0..M
            pow_c = [1] * (M + 1)
            for c in range(1, M + 1):
                pow_c[c] = (pow_c[c - 1] * x) % MOD

            # next layer
            next_dp = [ [defaultdict(int) for _ in range(K + 1)] for __ in range(M + 1) ]

            # iterate states
            for m1 in range(M + 1):
                max_c = M - m1  # we cannot exceed M in total
                if max_c < 0:
                    continue
                rows_k = dp[m1]
                for k in range(K + 1):
                    row = rows_k[k]
                    if not row:
                        continue

                    # For each current m2 state
                    for m2, val in row.items():
                        base = val  # keep local
                        # try all counts c we assign to nums[i]
                        # (transition: s = c + m2, k' += (s & 1), m2' = s >> 1)
                        for c in range(max_c + 1):
                            s = c + m2
                            k2 = k + (s & 1)
                            if k2 > K:
                                continue
                            m12 = m1 + c
                            m22 = s >> 1

                            add = base * inv_f[c] % MOD
                            add = add * pow_c[c] % MOD

                            bucket = next_dp[m12][k2]
                            bucket[m22] = (bucket[m22] + add) % MOD

            dp = next_dp  # roll

        # gather answer
        ans = 0
        for k in range(K + 1):
            for m2, val in dp[M][k].items():
                # Python 3.8+: int.bit_count()
                bits = m2.bit_count()
                if k + bits == K:
                    ans = (ans + val) % MOD

        ans = ans * f[M] % MOD
        return ans
