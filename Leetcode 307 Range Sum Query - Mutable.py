'''
Given an integer array nums, handle multiple queries of the following types:
        Update the value of an element in nums.
        Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
        
Implement the NumArray class:
        NumArray(int[] nums) Initializes the object with the integer array nums.
        void update(int index, int val) Updates the value of nums[index] to be val.
        int sumRange(int left, int right) Returns the sum of the elements of nums between
        indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:
        Input
        ["NumArray", "sumRange", "update", "sumRange"]
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
        Output
        [null, 9, null, 8]

        Explanation;
                NumArray numArray = new NumArray([1, 3, 5]);
                numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
                numArray.update(1, 2);   // nums = [1, 2, 5]
                numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:
        1 <= nums.length <= 3 * 104
        -100 <= nums[i] <= 100
        0 <= index < nums.length
        -100 <= val <= 100
        0 <= left <= right < nums.length
        At most 3 * 104 calls will be made to update and sumRange.


'''
class FenwickTree:
  def __init__(self, n: int):
    self.sums = [0] * (n + 1)

  def update(self, i: int, delta: int) -> None:
    while i < len(self.sums):
      self.sums[i] += delta
      i += FenwickTree.lowbit(i)

  def get(self, i: int) -> int:
    summ = 0
    while i > 0:
      summ += self.sums[i]
      i -= FenwickTree.lowbit(i)
    return summ

  @staticmethod
  def lowbit(i: int) -> int:
    return i & -i


class NumArray:
  def __init__(self, nums: List[int]):
    self.nums = nums
    self.tree = FenwickTree(len(nums))
    for i, num in enumerate(nums):
      self.tree.update(i + 1, num)

  def update(self, index: int, val: int) -> None:
    self.tree.update(index + 1, val - self.nums[index])
    self.nums[index] = val

  def sumRange(self, left: int, right: int) -> int:
    return self.tree.get(right + 1) - self.tree.get(left)




