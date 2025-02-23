'''
Search for a Range

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity. 

Example 1:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
Example 2:
        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]

Example 3:
        Input: nums = [], target = 0
        Output: [-1,-1]
 
Constraints:
        0 <= nums.length <= 105
        -109 <= nums[i] <= 109
        nums is a non-decreasing array.
        -109 <= target <= 109

'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start =-1
        ending =-1
        
        high = len(nums)-1
        low = 0
        
        if len(nums)==1:
            if target in nums:
                return [0,0]
            else:
                return [-1,-1]
        
        #Binary Usage -1
		
        while(low<=high):
            
            mid =(low+high)//2
            
            if nums[mid] == target:
                start = mid
                high = mid-1   #moving left
                
            elif nums[mid] > target:
                high = mid -1 
            
            else:
                
                low = mid+1
                
        
        # Binary Usage - 2
        low =0
        high = len(nums)-1
        
        while(low<=high):
            mid = (low+high)//2
            
            if nums[mid] == target:
                ending = mid
                low = mid+1   # moving right
                
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid +1
                
                
        return [start,ending]
        
        
        
        
        
        
# second solution
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a,b,c,d = 0, len(nums)-1, 0, len(nums)-1
        
        while a<b:
            mid = a+((b-a)>>1)
            if target<=nums[mid]:
                b = mid
            else:
                a = mid+1
        
        if nums[a]!=target:
            return [-1,-1]
                
        while c<d:
            mid = c+((d-c+1)>>1)
            if target<nums[mid]:
                d = mid-1
            else:
                c = mid
                
        return [a,c]


# 3rd Solution
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the starting and ending position of a given target value in a sorted array.
        If the target is not present, returns [-1, -1].

        Parameters:
        nums (List[int]): The sorted list of integers.
        target (int): The target integer to search for.

        Returns:
        List[int]: A list with two integers representing the first and last positions of the target.
        """
        # Find the leftmost and rightmost positions of the target
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)
        return [left, right]

    def findLeft(self, nums: List[int], target: int) -> int:
        """
        Finds the leftmost (first) occurrence of the target in the sorted array.
        Returns -1 if the target is not found.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # Check if it's the first occurrence
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findRight(self, nums: List[int], target: int) -> int:
        """
        Finds the rightmost (last) occurrence of the target in the sorted array.
        Returns -1 if the target is not found.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # Check if it's the last occurrence
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# Unit tests
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print("Test Case 1:", solution.searchRange(nums1, target1))  # Expected: [3, 4]

    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print("Test Case 2:", solution.searchRange(nums2, target2))  # Expected: [-1, -1]

    nums3 = []
    target3 = 0
    print("Test Case 3:", solution.searchRange(nums3, target3))  # Expected: [-1, -1]

    nums4 = [1]
    target4 = 1
    print("Test Case 4:", solution.searchRange(nums4, target4))  # Expected: [0, 0]

    nums5 = [2, 2, 2, 2]
    target5 = 2
    print("Test Case 5:", solution.searchRange(nums5, target5))  # Expected: [0, 3]

        
# 3rd solution
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findLeft(nums, target), self.findRight(nums, target)]

    def findLeft(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findRight(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

