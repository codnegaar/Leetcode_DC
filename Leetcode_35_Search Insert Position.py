'''
Leetcode 35 Search Insert Position.py

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order. You must write an algorithm with O(log n)
runtime complexity.

Example 1:
        Input: nums = [1,3,5,6], target = 5
        Output: 2
        
Example 2:
        Input: nums = [1,3,5,6], target = 2
        Output: 1
        
Example 3:
        Input: nums = [1,3,5,6], target = 7
        Output: 4


'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = m
                    id + 1
            else:
                right = mid - 1
        
        return left


#Second Solution
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Find the index at which the target should be inserted into the sorted list.
        
        Parameters:
        nums (List[int]): A sorted list of distinct integers.
        target (int): The target value to find or insert.
        
        Returns:
        int: The index where the target should be inserted.
        """
        # Initialize the binary search boundaries
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If target is found, return its index
            if nums[mid] == target:
                return mid
            # If target is less than the middle value, search in the left half
            elif target < nums[mid]:
                right = mid - 1
            # If target is greater than the middle value, search in the right half
            else:
                left = mid + 1
        
        # If not found, return the insertion point
        return left


# Unit tests
def test_searchInsert():
    solution = Solution()
    # Example 1: Target found in the list
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2, "Test Case 1 Failed"
    # Example 2: Target should be inserted at the start
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0, "Test Case 2 Failed"
    # Example 3: Target should be inserted in the middle
    assert solution.searchInsert([1, 3, 5, 6], 4) == 2, "Test Case 3 Failed"
    # Example 4: Target should be inserted at the end
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4, "Test Case 4 Failed"
    # Example 5: Single-element list
    assert solution.searchInsert([10], 10) == 0, "Test Case 5 Failed"
    assert solution.searchInsert([10], 5) == 0, "Test Case 6 Failed"
    assert solution.searchInsert([10], 15) == 1, "Test Case 7 Failed"
    # Example 6: Empty list
    assert solution.searchInsert([], 1) == 0, "Test Case 8 Failed"
    print("All test cases pass.")

# Run the unit tests
test_searchInsert()

        
