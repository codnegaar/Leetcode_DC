'''
Leetcode 3480 Maximize Subarrays After Removing One Conflicting Pair
 
You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, 
where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.
Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].
Return the maximum number of subarrays possible after removing exactly one conflicting pair. 

Example 1:
        Input: n = 4, conflictingPairs = [[2,3],[1,4]]
        Output: 9
        Explanation: Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
                     There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
                     The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.

Example 2:
        Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]
        Output: 12        
        Explanation:      
                    Remove [1, 2] from conflictingPairs. Now, conflictingPairs = [[2, 5], [3, 5]].
                    There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together.
                    The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 12.
 
Constraints:
        2 <= n <= 105
        1 <= conflictingPairs.length <= 2 * n
        conflictingPairs[i].length == 2
        1 <= conflictingPairs[i][j] <= n
        conflictingPairs[i][0] != conflictingPairs[i][1]

'''
from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        # Group all `u` values by their `v` endpoint
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        # Base score
        ans = 0 
        # `left` stores [top1, top2] `u` values seen so far, where top1 >= top2.
        # `left[0]` acts as our running `forbidden_start`.
        left = [0, 0] 
        # `bonus[u]` accumulates the total gain if the critical conflict involving `u` is removed.
        bonus = [0] * (n + 1)
        
        # Single pass from r = 1 to n
        for r in range(1, n + 1):
            # Check for new conflicts ending at `r` and update `left`
            for l in right[r]:
                # This is a concise trick to update the top two seen values
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
            # Add the count for this endpoint to the base score
            ans += r - left[0]

            # The gain at this step is the difference between the top two forbidden starts.
            # We add this gain to the tally for the `u` value causing the restriction (`left[0]`).
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        # The final result is the base score plus the maximum possible gain.
        return ans + max(bonus)
