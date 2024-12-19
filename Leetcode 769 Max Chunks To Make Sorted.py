'''
Leetcode 769 Max Chunks To Make Sorted

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
Return the largest number of chunks we can make to sort the array.
 
Example 1:
        Input: arr = [4,3,2,1,0]
        Output: 1
        Explanation:
        Splitting into two or more chunks will not return the required result.
        For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
        Input: arr = [1,0,2,3,4]
        Output: 4
        Explanation:
        We can split into two chunks, such as [1, 0], [2, 3, 4].
        However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
         
Constraints:
        n == arr.length
        1 <= n <= 10
        0 <= arr[i] < n
        All the elements of arr are unique.

'''

class Solution:
    """
    A class to solve the problem of finding the maximum number of chunks
    the array can be split into such that after sorting each chunk, 
    the resulting array is sorted.

    Methods
    -------
    maxChunksToSorted(arr: list[int]) -> int:
        Returns the maximum number of chunks the array can be split into
        to make the entire array sorted after sorting each chunk.
    """
    
    def maxChunksToSorted(self, arr):
        """
        This method finds the maximum number of chunks to split the array
        into, such that after sorting each chunk individually, the entire 
        array will be sorted.

        Parameters
        ----------
        arr : list[int]
            A list of integers to be partitioned into chunks.

        Returns
        -------
        int
            The maximum number of chunks into which the array can be split.
        """
        
        # Variable to keep track of the current maximum value encountered in the array
        max_val = -float('inf')  
        
        # Initialize the count of chunks to 0
        cnt = 0
        
        # Iterate through the array to check the chunks
        for i in range(len(arr)):
            # Update the max_val as the maximum of current value and previous max
            max_val = max(max_val, arr[i])
            
            # If max_val is equal to the index, we can split at this point
            if max_val == i:
                cnt += 1
        
        return cnt

# Unit Tests and Examples
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic Example
    arr1 = [1, 0, 2, 3, 4]
    print(solution.maxChunksToSorted(arr1))  # Output: 4

    # Test Case 2: Already sorted array
    arr2 = [0, 1, 2, 3, 4]
    print(solution.maxChunksToSorted(arr2))  # Output: 5

    # Test Case 3: Array that is fully reversed
    arr3 = [5, 4, 3, 2, 1]
    print(solution.maxChunksToSorted(arr3))  # Output: 1

    # Test Case 4: Another random example
    arr4 = [2, 1, 3, 4, 5]
    print(solution.maxChunksToSorted(arr4))  # Output: 3

