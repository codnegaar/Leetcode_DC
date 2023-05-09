'''
Leetcode 315 Count of Smaller Numbers After Self
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i]. 

Example 1:
        Input: nums = [5,2,6,1]
        Output: [2,1,1,0]
        Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.
        
Example 2:
        Input: nums = [-1]
        Output: [0]
        
Example 3:
        Input: nums = [-1,-1]
        Output: [0,0]
 
Constraints:
        1 <= nums.length <= 105
        -104 <= nums[i] <= 104

'''
class Item:
  def __init__(self, num: int = 0, index: int = 0):
    self.num = num
    self.index = index


class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n
    items = [Item(num, i) for i, num in enumerate(nums)]

    self._mergeSort(items, 0, n - 1, ans)
    return ans

  def _mergeSort(self, items: List[Item], l: int, r: int, ans: List[int]) -> None:
    if l >= r:
      return

    m = (l + r) // 2
    self._mergeSort(items, l, m, ans)
    self._mergeSort(items, m + 1, r, ans)
    self._merge(items, l, m, r, ans)

  def _merge(self, items: List[Item], l: int, m: int, r: int, ans: List[int]) -> None:
    sorted = [Item()] * (r - l + 1)
    k = 0           # sorted's index
    i = l           # left's index
    j = m + 1       # right's index
    rightCount = 0  # # Of nums < items[i].num

    while i <= m and j <= r:
      if items[i].num > items[j].num:
        rightCount += 1
        sorted[k] = items[j]
        k += 1
        j += 1
      else:
        ans[items[i].index] += rightCount
        sorted[k] = items[i]
        k += 1
        i += 1

    # Put possible remaining left part to the sorted array
    while i <= m:
      ans[items[i].index] += rightCount
      sorted[k] = items[i]
      k += 1
      i += 1

    # Put possible remaining right part to the sorted array
    while j <= r:
      sorted[k] = items[j]
      k += 1
      j += 1

    items[l:l + len(sorted)] = sorted
