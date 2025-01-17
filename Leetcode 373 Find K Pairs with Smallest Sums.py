'''
Leetcode 373 Find K Pairs with Smallest Sums
 
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length

'''

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        resV = []  # Result list to store the pairs
        pq = []  # Priority queue to store pairs with smallest sums, sorted by the sum

        # Push the initial pairs into the priority queue
        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])  # The sum and the index of the second element in nums2

        # Pop the k smallest pairs from the priority queue
        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]  # Get the smallest sum and the index of the second element in nums2

            resV.append([s - nums2[pos], nums2[pos]])  # Add the pair to the result list

            # If there are more elements in nums2, push the next pair into the priority queue
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  # Decrement k

        return resV  # Return the k smallest pairs


# Second Solution:
import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Find the k pairs with the smallest sums from two sorted arrays.

        Parameters:
        nums1 (List[int]): The first sorted array.
        nums2 (List[int]): The second sorted array.
        k (int): The number of smallest pairs to return.

        Returns:
        List[List[int]]: A list of the k pairs with the smallest sums.
        """
        if not nums1 or not nums2 or k <= 0:
            return []  # Handle edge cases where input is invalid or k is zero

        res = []  # Result list to store the pairs
        pq = []  # Priority queue (min-heap) to store pairs with their sums
        
        # Initialize the heap with the first element from nums1 paired with each element in nums2
        for i in range(min(k, len(nums1))):  # Only take up to k elements from nums1
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)

        # Extract k smallest pairs
        while k > 0 and pq:
            current_sum, i, j = heapq.heappop(pq)  # Get the smallest pair from the heap
            res.append([nums1[i], nums2[j]])  # Add the corresponding pair to the result
            
            # If there's a next element in nums2, push the next pair from nums1[i] and nums2[j+1]
            if j + 1 < len(nums2):
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1  # Decrement k

        return res


# Example of implementation
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    result = solution.kSmallestPairs(nums1, nums2, k)
    print(f"The {k} pairs with the smallest sums are: {result}")  # Expected: [[1, 2], [1, 4], [1, 6]]


# Unit Testing
import unittest

class TestKSmallestPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        self.assertEqual(self.solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])

    def test_case2(self):
        self.assertEqual(self.solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])

    def test_case3(self):
        self.assertEqual(self.solution.kSmallestPairs([], [2, 4, 6], 3), [])

    def test_case4(self):
        self.assertEqual(self.solution.kSmallestPairs([1, 2], [], 3), [])

    def test_case5(self):
        self.assertEqual(self.solution.kSmallestPairs([1, 2], [3], 5), [[1, 3], [2, 3]])

if __name__ == "__main__":
    # Run the test suite
    unittest.main()


