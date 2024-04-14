'''
Leetcode 930 Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array. 

Example 1:
      Input: nums = [1,0,1,0,1], goal = 2
      Output: 4
      Explanation:  The 4 subarrays are bolded and underlined below:
                    [1,0,1,0,1]
                    [1,0,1,0,1]
                    [1,0,1,0,1]
                    [1,0,1,0,1]

Example 2:
        Input: nums = [0,0,0,0,0], goal = 0
        Output: 15

Constraints:
      1 <= nums.length <= 3 * 104
      nums[i] is either 0 or 1.
      0 <= goal <= nums.length


----------------------------------------------------------------------------solution strategy----------------------
To solve the problem of finding the number of non-empty subarrays with a sum equal to a given goal in a binary array,
you can employ a technique known as the "Prefix Sum" combined with a hashmap to efficiently count subarrays that meet the condition.

Explanation
Prefix Sum: This is a technique where you keep a running sum of elements of the array as you iterate through it. 
This allows you to quickly calculate the sum of any subarray by subtracting two prefix sums.

Hashmap (or Dictionary in Python): This is used to store the number of times each prefix sum occurs. 
This is crucial because to find a subarray that sums to the goal, you want to find how many times you have seen a prefix sum that is current_prefix_sum - goal.

Steps
1- Initialize Variables:

- prefix_sum to keep the running sum.
- count to count the number of valid subarrays.
- A hashmap prefix_count to keep track of how many times each prefix_sum value has occurred, initialized with {0: 1} to handle the case where a subarray starts from index 0.

2- Iterate through the Array:
       - For each element, add it to prefix_sum.
       - To find the number of subarrays ending at the current index that have a sum equal to the goal, check prefix_sum - goal in prefix_count.
       - Add the number of times prefix_sum - the goal has been seen to count.
       - Update the hashmap with the current prefix_sum.
       
3- Return the result which is stored in count.

'''

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num  # Update the prefix sum
            # Check if there's a prefix_sum - goal in the dictionary
            count += prefix_count.get(prefix_sum - goal, 0)
            # Update the dictionary with the current prefix sum
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count

# Example usage
sol = Solution()
print(sol.numSubarraysWithSum([1,0,1,0,1], 2))  # Output: 4
print(sol.numSubarraysWithSum([0,0,0,0,0], 0))  # Output: 15

