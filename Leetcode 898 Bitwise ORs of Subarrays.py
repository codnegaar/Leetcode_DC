'''
Leetcode 898 Bitwise ORs of Subarrays

Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
A subarray is a contiguous, non-empty sequence of elements within an array. 

Example 1:
        Input: arr = [0]
        Output: 1
        Explanation: There is only one possible result: 0.

Example 2:
        Input: arr = [1,1,2]
        Output: 3
        Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
        These yield the results 1, 1, 2, 1, 3, 3.
        There are 3 unique values, so the answer is 3.

Example 3:
        Input: arr = [1,2,4]
        Output: 6
        Explanation: The possible results are 1, 2, 3, 4, 6, and 7.        

Constraints:
        1 <= arr.length <= 5 * 104
        0 <= arr[i] <= 109
'''
from typing import List

class Solution:
    """
    A class that contains a method to compute the number of distinct bitwise ORs
    of all subarrays of a given integer array.
    """

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        Computes the number of distinct results obtained by performing bitwise OR
        on every possible contiguous subarray of the input list.

        Parameters:
        arr (List[int]): A list of non-negative integers.

        Returns:
        int: The count of unique bitwise OR results.
        """
        # 'ans' stores all distinct OR results
        ans = set()
        
        # 'current' stores all OR results ending at current index
        current = set()
        
        for num in arr:
            # Generate new OR combinations using the current number and previous results
            current = {num | x for x in current} | {num}
            ans |= current  # Update the global set of results
        
        return len(ans)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    example = [1, 2, 4]
    print("Distinct ORs:", sol.subarrayBitwiseORs(example))  # Output should be 6
 
