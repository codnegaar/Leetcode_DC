'''
Lettcode BS-Tricky Invariant  852. Peak Index in a Mountain Array

An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
        Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

 

Example 1:
        Input: arr = [0,1,0]
        Output: 1
        
Example 2:
        Input: arr = [0,2,1,0]
        Output: 1
        
Example 3:
        Input: arr = [0,10,5,2]
        Output: 1

Constraints:
        3 <= arr.length <= 105
        0 <= arr[i] <= 106
        arr is guaranteed to be a mountain array.

'''
# Solution one(builtin function)
class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
      return arr.index(max(arr))



# solution 2
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                return mid + 1
            if mid == len(arr) - 1:
                return mid - 1
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
         

