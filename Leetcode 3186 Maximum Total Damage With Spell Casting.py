'''
Leetcode 3186 Maximum Total Damage With Spell Casting

A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
Each spell can be cast only once.
Return the maximum possible total damage that a magician can cast. 

Example 1:
        Input: power = [1,1,3,4]
        Output: 6
        Explanation: The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:
        Input: power = [7,1,6,6]        
        Output: 13        
        Explanation: The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

Constraints:
        1 <= power.length <= 105
        1 <= power[i] <= 109
'''
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]
        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            l, r, ans = 0, i - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if keys[mid] <= keys[i] - 3:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if ans >= 0:
                take += dp[ans]
            dp[i] = max(dp[i - 1], take)
        return dp[-1]
