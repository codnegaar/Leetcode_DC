'''
Leetcode 3405 Count the Number of Arrays with K Matching Adjacent Elements
 
You are given three integers n, m, k. A good array arr of size n is defined as follows:
        Each element in arr is in the inclusive range [1, m].
        Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
        Return the number of good arrays that can be formed.
Since the answer may be very large, return it modulo 109 + 7. 

Example 1:
        Input: n = 3, m = 2, k = 1
        Output: 4
        Explanation: There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
        Hence, the answer is 4.

Example 2:
        Input: n = 4, m = 2, k = 2
        Output: 6
        Explanation: The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
        Hence, the answer is 6.

Example 3:
        Input: n = 5, m = 2, k = 0
        Output: 2
        Explanation: The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.         

Constraints:
        1 <= n <= 105
        1 <= m <= 105
        0 <= k <= n - 1
'''

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Count the number of 'good' arrays of length `n` using integers from `1` to `m`,
        such that there are exactly `k` positions where adjacent elements are equal.

        Parameters:
        - n (int): Length of the array (n >= 1)
        - m (int): Number of distinct values (m >= 1)
        - k (int): Number of positions where adjacent values are equal (0 <= k < n)

        Returns:
        - int: Number of good arrays under modulo 10^9 + 7
        """
        MOD = 10**9 + 7

        # Edge case: can't have more than n - 1 equal adjacent positions
        if k > n - 1:
            return 0

        d = n - 1  # Total adjacent positions
        r = min(k, d - k)  # Use symmetry to reduce computation
        comb = 1  # Initial combination value C(d, k)

        if r > 0:
            # Precompute modular inverses for 1..r using Fermat's little theorem
            inv = [0] * (r + 1)
            inv[1] = 1
            for i in range(2, r + 1):
                inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

            for i in range(1, r + 1):
                comb = comb * (d - r + i) % MOD * inv[i] % MOD

        # Total good arrays = m * C(d, k) * (m-1)^(d-k)
        return m * comb % MOD * pow(m - 1, d - k, MOD) % MOD

