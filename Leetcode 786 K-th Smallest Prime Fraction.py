'''

Leetcode 786 K-th Smallest Prime Fraction

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:
        Input: arr = [1,2,3,5], k = 3
        Output: [2,5]
        Explanation: The fractions to be considered in sorted order are:
        1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
        The third fraction is 2/5.

Example 2:
        Input: arr = [1,7], k = 1
        Output: [1,7]
 

Constraints:
          2 <= arr.length <= 1000
          1 <= arr[i] <= 3 * 104
          arr[0] == 1
          arr[i] is a prime number for i > 0.
          All the numbers of arr are unique and sorted in strictly increasing order.
          1 <= k <= arr.length * (arr.length - 1) / 2

'''

from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Initialize binary search bounds
        left, right = 0.0, 1.0
        # Result to store the K-th smallest fraction
        result = []

        # Perform binary search
        while left < right:
            mid = (left + right) / 2
            count = 0
            max_fraction = 0.0
            num = den = 0
            j = 0

            # Iterate through each element in the array to find fractions
            for i in range(len(arr)):
                # Find the first fraction greater than or equal to 'mid'
                while j < len(arr) and arr[i] / arr[j] > mid:
                    j += 1

                # Count how many fractions are less than 'mid'
                count += len(arr) - j

                # Keep track of the largest fraction less than 'mid'
                if j < len(arr) and (num == 0 or arr[i] * den > arr[j] * num):
                    num, den = arr[i], arr[j]

            # Check if we have found the k-th smallest fraction
            if count == k:
                result = [num, den]
                break
            # Adjust binary search bounds
            if count < k:
                left = mid
            else:
                right = mid

        return result
