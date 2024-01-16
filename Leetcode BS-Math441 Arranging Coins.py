'''
Leetcode BS-Math441 Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
 

Example 1:
        Input: n = 5
        Output: 2
        Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
        Input: n = 8
        Output: 3
        Explanation: Because the 4th row is incomplete, we return 3.
         
Constraints:      
      1 <= n <= 231 - 1

'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize pointers to first and last possible row lengths
        left, right = 1, n
        
        while left <= right:
            # Compute the midpoint between left and right
            mid = left + (right - left) // 2
            
            # Compute the total number of coins needed for mid complete rows
            coins = (mid * (mid + 1)) // 2
            
            # If we have enough coins, look for a smaller number of rows
            if coins <= n:
                left = mid + 1
            # Otherwise, look for a larger number of rows
            else:
                right = mid - 1
                
        # Return the number of complete rows (i.e., right pointer)
        return right
