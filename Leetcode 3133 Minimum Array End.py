'''
Leetcode 3133 Minimum Array End

You are given two integers n and x. You have to construct an array of positive integers nums of size n where for
every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.
Return the minimum possible value of nums[n - 1].

Example 1:
Input: n = 3, x = 4
Output: 6
Explanation:
nums can be [4,5,6] and its last element is 6.

Example 2:
        Input: n = 2, x = 7
        Output: 15
        Explanation:
        nums can be [7,15] and its last element is 15.

Constraints:
        1 <= n, x <= 108
'''

class Solution:
    def minEnd(self, n: int, x: int) -> int:

        result = 0
        # Reducing n by 1 to exclude x from the iteration
        n -= 1

        # Step 1: Initialize lists to hold the binary representation of x and n-1
        binaryX = [0] * 64  # Binary representation of x
        binaryN = [0] * 64  # Binary representation of n-1

        # Step 2: Build binary representations of x and n-1
        for i in range(64):
            bit = (x >> i) & 1  # Extract i-th bit of x
            binaryX[i] = bit

            bit = (n >> i) & 1  # Extract i-th bit of n-1
            binaryN[i] = bit

        posX = 0
        posN = 0

        # Step 3: Combine binary representation of x and n-1
        while posX < 63:
            # Traverse binaryX until we find a 0 bit
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            # Copy bits from binaryN (n-1) into binaryX (x) starting from the first 0
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        # Step 4: Rebuild the final result from the combined binary representation
        for i in range(64):
            if binaryX[i] == 1:
                # convert binary bit to decimal value
                result += pow(2, i)

        return result
