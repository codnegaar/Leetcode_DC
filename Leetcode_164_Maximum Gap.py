'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

'''

# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
class Bucket:
  def __init__(self, mini: int, maxi: int):
    self.mini = mini
    self.maxi = maxi


class Solution:
  def maximumGap(self, nums: List[int]) -> int:
    if len(nums) < 2:
      return 0

    mini = min(nums)
    maxi = max(nums)
    if mini == maxi:
      return 0

    gap = ceil((maxi - mini) / (len(nums) - 1))
    bucketSize = (maxi - mini) // gap + 1
    buckets = [Bucket(math.inf, -math.inf) for _ in range(bucketSize)]

    for num in nums:
      i = (num - mini) // gap
      buckets[i].mini = min(buckets[i].mini, num)
      buckets[i].maxi = max(buckets[i].maxi, num)

    ans = 0
    prevMax = mini

    for bucket in buckets:
      if bucket.mini == math.inf:
        continue  # Empty bucket
      ans = max(ans, bucket.mini - prevMax)
      prevMax = bucket.maxi

    return ans
