'''
Leetcode 960 Delete Columns to Make Sorted III
 
You are given an array of n strings strs, all of the same length.
We may choose any deletion indices, and we delete all the characters in those indices for each string.
For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].
Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. 
(i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length. 

Example 1:
        Input: strs = ["babca","bbazb"]
        Output: 3
        Explanation: After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"].
        Both these rows are individually in lexicographic order (ie. strs[0][0] <= strs[0][1] and strs[1][0] <= strs[1][1]).
        Note that strs[0] > strs[1] - the array strs is not necessarily in lexicographic order.

Example 2:
        Input: strs = ["edcba"]
        Output: 4
        Explanation: If we delete less than 4 columns, the only row will not be lexicographically sorted.

Example 3:
        Input: strs = ["ghi","def","abc"]
        Output: 0
        Explanation: All rows are already lexicographically sorted. 

Constraints:
      n == strs.length
      1 <= n <= 100
      1 <= strs[i].length <= 100
      strs[i] consists of lowercase English letters.

'''

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # Helper function to check if column 'j' can precede column 'i'
        # without breaking the lexicographical order in any row.
        def is_ordered(col1, col2):
            for row in range(n):
                if strs[row][col1] > strs[row][col2]:
                    return False
            return True

        # dp[i] will store the maximum number of sorted columns 
        # ending with column i.
        dp = [1] * m
        max_kept_cols = 0
        
        for i in range(m):
            for j in range(i):
                if is_ordered(j, i):
                    dp[i] = max(dp[i], dp[j] + 1)
            
            # Track the maximum number of columns we can keep
            max_kept_cols = max(max_kept_cols, dp[i])
            
        # The result is the total columns minus the ones we keep.
        return m - max_kept_cols
