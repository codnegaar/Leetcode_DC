'''
Leetcode 3348 Smallest Divisible Digit Product II
 
You are given a string num which represents a positive integer, and an integer t.
A number is called zero-free if none of its digits are 0.
Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible
by t. If no such number exists, return "-1".

Example 1:
        Input: num = "1234", t = 256
        Output: "1488"
        Explanation: The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:
        Input: num = "12355", t = 50
        Output: "12355"
        Explanation: 12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:
          Input: num = "11111", t = 26
          Output: "-1"
          Explanation:No number greater than 11111 has the product of its digits divisible by 26.

Constraints:
        2 <= num.length <= 2 * 105
        num consists only of digits in the range ['0', '9'].
        num does not contain leading zeros.
        1 <= t <= 1014

'''

import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        counts = [0, 0, 0, 0]
        for i, p in enumerate([2, 3, 5, 7]):
            while temp % p == 0:
                counts[i] += 1
                temp //= p
                
        if temp > 1:
            return "-1"
            
        divs = []
        for a in range(counts[0] + 1):
            for b in range(counts[1] + 1):
                for c in range(counts[2] + 1):
                    for d in range(counts[3] + 1):
                        divs.append((2**a) * (3**b) * (5**c) * (7**d))
        divs.sort()
        
        trans = {v: [v] * 10 for v in divs}
        for v in divs:
            for d in range(1, 10):
                trans[v][d] = v // math.gcd(v, d)
                
        dp = {v: float('inf') for v in divs}
        dp[1] = 0
        
        for v in divs:
            if v == 1:
                continue
            best = float('inf')
            for d in range(2, 10):
                nxt = trans[v][d]
                if dp[nxt] + 1 < best:
                    best = dp[nxt] + 1
            dp[v] = best
            
        n = len(num)
        first_zero = num.find('0')
        
        if first_zero == -1:
            max_i_allowed = n - 1
        else:
            max_i_allowed = first_zero
            
        prefix_t = [t]
        for i in range(max_i_allowed):
            prefix_t.append(trans[prefix_t[-1]][int(num[i])])
            
        if first_zero == -1:
            full_t = trans[prefix_t[-1]][int(num[-1])]
            if full_t == 1:
                return num
                
        for i in range(max_i_allowed, -1, -1):
            p_t = prefix_t[i]
            rem = n - 1 - i
            
            for d in range(int(num[i]) + 1, 10):
                t_req = trans[p_t][d]
                if dp[t_req] <= rem:
                    ans = [num[:i], str(d)]
                    curr_t = t_req
                    for step in range(rem):
                        for nxt_d in range(1, 10):
                            next_t = trans[curr_t][nxt_d]
                            if dp[next_t] <= rem - 1 - step:
                                ans.append(str(nxt_d))
                                curr_t = next_t
                                break
                    return "".join(ans)
                    
        length = max(n + 1, dp[t])
        ans = []
        curr_t = t
        for step in range(length):
            for nxt_d in range(1, 10):
                next_t = trans[curr_t][nxt_d]
                if dp[next_t] <= length - 1 - step:
                    ans.append(str(nxt_d))
                    curr_t = next_t
                    break
        return "".join(ans)
