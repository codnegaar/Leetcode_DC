'''
Leetcode 3234 Count the Number of Substrings With Dominant Ones

You are given a binary string s.
Return the number of substrings with dominant ones.
A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

Example 1:
        Input: s = "00011"
        Output: 5
        Explanation:
        The substrings with dominant ones are shown in the table below.
        
                i	j	s[i..j]	Number of Zeros	Number of Ones
                3	3	1	0	1
                4	4	1	0	1
                2	3	01	1	1
                3	4	11	0	2
                2	4	011	1	2

Example 2:        
        Input: s = "101101"        
        Output: 16
        Explanation:
        The substrings with non-dominant ones are shown in the table below.
        Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
 

Constraints:
      1 <= s.length <= 4 * 104
      s consists only of characters '0' and '1'.

'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i+1] = pref[i] + (ch == '1')

        Z = [i for i, ch in enumerate(s) if ch == '0']
        m = len(Z)

        ans = 0

        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            j = i
            while j < n and s[j] == '1':
                j += 1
            L = j - i
            ans += L * (L + 1) // 2
            i = j

        B = isqrt(n) + 2

        def ones(l, r):
            return pref[r+1] - pref[l]

        for a in range(m):
            Lmin = 0 if a == 0 else Z[a-1] + 1
            Lmax = Z[a]
            if Lmin > Lmax:
                continue

            for z in range(1, B + 1):
                b = a + z - 1
                if b >= m:
                    break

                Rmin = Z[b]
                Rmax = Z[b + 1] - 1 if b + 1 < m else n - 1
                if Rmin > Rmax:
                    continue

                need = z * z
                r = Rmin

                for l in range(Lmin, Lmax + 1):
                    if pref[Rmax + 1] - pref[l] < need:
                        continue
                    while r <= Rmax and ones(l, r) < need:
                        r += 1
                    if r > Rmax:
                        break
                    ans += (Rmax - r + 1)

        return ans
