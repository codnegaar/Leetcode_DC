'''

Leetcode 3264 Final Array State After K Multiplication Operations I

You are given an integer array nums, an integer k, and an integer multiplier.
You need to perform k operations on nums. In each operation:
        Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
        Replace the selected minimum value x with x * multiplier.
        Return an integer array denoting the final state of nums after performing all k operations.

Example 1:
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
Output: [8,4,6,5,6]
Explanation:
          Operation	Result
          After operation 1	[2, 2, 3, 5, 6]
          After operation 2	[4, 2, 3, 5, 6]
          After operation 3	[4, 4, 3, 5, 6]
          After operation 4	[4, 4, 6, 5, 6]
          After operation 5	[8, 4, 6, 5, 6]    
    
Example 2:
      Input: nums = [1,2], k = 3, multiplier = 4
      Output: [16,8]      
      Explanation:      
              Operation	Result
              After operation 1	[4, 2]
              After operation 2	[4, 8]
              After operation 3	[16, 8]
       
Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 100
        1 <= k <= 10
        1 <= multiplier <= 5

'''

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        from typing import List
from heapq import heapify, heapreplace

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Modify a list of integers `nums` after performing `k` multiplications
        on the smallest element in the list, each time multiplied by `multiplier`.

        Parameters:
        nums (List[int]): A list of integers to process.
        k (int): Number of iterations where the smallest element is multiplied.
        multiplier (int): The factor by which the smallest element is multiplied.

        Returns:
        List[int]: The final state of the modified list.
        """
        # Create a min-heap with values and their original indices for efficient operations
        heap = [(x, i) for i, x in enumerate(nums)]
        heapify(heap)  # Transform the list into a heap in O(n) time

        # Perform k multiplications on the smallest element in the heap
        for _ in range(k):
            x, i = heap[0]  # Get the smallest element (min-heap property)
            heapreplace(heap, (x * multiplier, i))  # Replace it with its multiplied value

        # Update the original list `nums` using modified values in the heap
        for x, i in heap:
            nums[i] = x  # Update the value at its original index

        return nums

 
