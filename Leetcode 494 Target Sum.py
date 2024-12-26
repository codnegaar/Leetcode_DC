'''

Leetcode 494 Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
        Input: nums = [1,1,1,1,1], target = 3
        Output: 5
        Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
        -1 + 1 + 1 + 1 + 1 = 3
        +1 - 1 + 1 + 1 + 1 = 3
        +1 + 1 - 1 + 1 + 1 = 3
        +1 + 1 + 1 - 1 + 1 = 3
        +1 + 1 + 1 + 1 - 1 = 3

Example 2:        
        Input: nums = [1], target = 1
        Output: 1 

Constraints:
        1 <= nums.length <= 20
        0 <= nums[i] <= 1000
        0 <= sum(nums[i]) <= 1000
        -1000 <= target <= 1000

'''

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Find the number of ways to assign '+' or '-' to elements in nums such that
        the resulting sum equals the target.

        Parameters:
        - nums: List[int]: List of integers.
        - target: int: The target sum.

        Returns:
        - int: Number of ways to achieve the target sum.
        """

        dp = {}  # Dictionary to store intermediate results for memoization.

        def recursion(idx: int, cur_sum: int) -> int:
            """
            Recursive helper function to explore all combinations of '+' and '-' for each number.

            Parameters:
            - idx: int: Current index in the nums list.
            - cur_sum: int: Current cumulative sum.

            Returns:
            - int: Number of ways to achieve the target from the current state.
            """
            # Base case: If all numbers are used, check if the current sum matches the target.
            if idx == len(nums):
                return 1 if cur_sum == target else 0

            # Check if the current state has already been computed.
            if (idx, cur_sum) in dp:
                return dp[(idx, cur_sum)]

            # Recursive calls for adding and subtracting the current number.
            add = recursion(idx + 1, cur_sum + nums[idx])
            subtract = recursion(idx + 1, cur_sum - nums[idx])

            # Store the result in the memoization dictionary.
            dp[(idx, cur_sum)] = add + subtract
            return dp[(idx, cur_sum)]

        # Start the recursion from the first index and a sum of 0.
        return recursion(0, 0)

# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [1, 1, 1, 1, 1]
    target = 3
    print("Test Case 1:", solution.findTargetSumWays(nums, target))  # Expected output: 5

    # Test case 2
    nums = [1]
    target = 1
    print("Test Case 2:", solution.findTargetSumWays(nums, target))  # Expected output: 1

    # Test case 3
    nums = [1, 2, 3]
    target = 4
    print("Test Case 3:", solution.findTargetSumWays(nums, target))  # Expected output: 2
