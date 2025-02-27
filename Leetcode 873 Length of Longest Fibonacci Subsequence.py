'''
Leetcode 873 Length of Longest Fibonacci Subsequence
 
A sequence x1, x2, ..., xn is Fibonacci-like if:
n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, 
[3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

Example 1:
        Input: arr = [1,2,3,4,5,6,7,8]
        Output: 5
        Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
        Input: arr = [1,3,7,11,12,14,18]
        Output: 3
        Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].         

Constraints:
        3 <= arr.length <= 1000
        1 <= arr[i] < arr[i + 1] <= 109
'''

class Solution:
    """
    This class provides a solution to find the length of the longest Fibonacci-like subsequence in a given list.
    """

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """
        Finds the length of the longest Fibonacci-like subsequence in an array.

        Parameters:
        arr (list[int]): A list of distinct positive integers.

        Returns:
        int: The length of the longest Fibonacci-like subsequence.
        """
        index_map = {num: i for i, num in enumerate(arr)}  # Map number to its index for quick lookup
        dp = {}  # Dictionary to store the length of Fibonacci-like subsequence ending at (i, j)
        max_len = 0  # Variable to track the longest subsequence length

        # Iterate through all pairs (j, i) where j < i
        for i in range(len(arr)):
            for j in range(i):
                # Find the potential previous Fibonacci number
                prev = arr[i] - arr[j]

                # Ensure it's a valid Fibonacci sequence (prev should be in array and before j)
                if prev in index_map and index_map[prev] < j:
                    k = index_map[prev]  # Index of the previous number
                    dp[(j, i)] = dp.get((k, j), 2) + 1  # Update sequence length
                    max_len = max(max_len, dp[(j, i)])  # Update max length found

        return max_len if max_len >= 3 else 0  # Return max length (0 if no valid sequence found)


# Example Usage
solution = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(solution.lenLongestFibSubseq(arr))  # Output: 5 (Sequence: [1, 2, 3, 5, 8])
