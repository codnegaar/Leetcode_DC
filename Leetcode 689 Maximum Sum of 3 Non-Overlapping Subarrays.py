'''
689 Maximum Sum of 3 Non-Overlapping Subarrays
 
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)


'''
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Find three non-overlapping subarrays of length `k` with the maximum sum.
        
        Parameters:
        - nums (List[int]): The input array.
        - k (int): The fixed length of each subarray.

        Returns:
        - List[int]: The starting indices of the three subarrays.
        """
        N = len(nums)

        # Compute the sum of all k-length windows
        window_sums = [0] * (N - k + 1)
        current_sum = sum(nums[:k])
        window_sums[0] = current_sum
        for i in range(1, N - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = current_sum

        # Initialize arrays to store the best indices for left and right subarrays
        left = [0] * len(window_sums)
        right = [0] * len(window_sums)

        # Compute the best starting index for the left subarray
        best_left = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_left]:
                best_left = i
            left[i] = best_left

        # Compute the best starting index for the right subarray
        best_right = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_right]:
                best_right = i
            right[i] = best_right

        # Find the best middle subarray and calculate the maximum sum
        max_sum = float('-inf')
        result = []
        for mid in range(k, len(window_sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            current_sum = window_sums[l] + window_sums[mid] + window_sums[r]
            if current_sum > max_sum:
                max_sum = current_sum
                result = [l, mid, r]

        return result

# Unit Test
def test_maxSumOfThreeSubarrays():
    solution = Solution()

    # Test cases
    assert solution.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2) == [0, 3, 5]
    assert solution.maxSumOfThreeSubarrays([4, 5, 10, 6, 11, 17, 12, 13, 5], 2) == [3, 5, 7]
    assert solution.maxSumOfThreeSubarrays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == [0, 1, 2]
    assert solution.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1, 2, 8], 2) == [0, 3, 8]

    print("All tests passed.")

# Example usage
if __name__ == "__main__":
    test_maxSumOfThreeSubarrays()
