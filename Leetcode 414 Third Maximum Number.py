'''
Leetcode 414 Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

    Input: nums = [3,2,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
    Input: nums = [1,2]
    Output: 2
    Explanation:
    The first distinct maximum is 2.
    The second distinct maximum is 1.
    The third distinct maximum does not exist, so the maximum (2) is returned instead.
    
Example 3:
    Input: nums = [2,2,3,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
    The third distinct maximum is 1.
     

Constraints:
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1 
 
 '''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Sort the array.
        nums.sort(reverse = True)
        
        elem_counted = 1
        prev_elem = nums[0]
        
        for index in range(len(nums)):
            # Current element is different from previous.
            if nums[index] != prev_elem:
                elem_counted += 1
                prev_elem = nums[index]
            
            # If we have counted 3 numbers then return current number.
            if elem_counted == 3:
                return nums[index]
        


# second solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_heap = []
        taken = set()
        
        for index in range(len(nums)):
            # If current number was already taken, skip it.
            if nums[index] in taken:
                continue
            
            # If min heap already has three numbers in it.
            # Pop the smallest if current number is bigger than it.
            if len(min_heap) == 3:
                if min_heap[0] < nums[index]:
                    taken.remove(min_heap[0])
                    heappop(min_heap)
                    
                    heappush(min_heap, nums[index])
                    taken.add(nums[index])
                    
            # If min heap does not have three number we can push it.
            else:
                heappush(min_heap, nums[index])
                taken.add(nums[index])
        
        # 'nums' has only one distinct element it will be the maximum.
        if len(min_heap) == 1:
            return min_heap[0]
        
        # 'nums' has two distinct elements.
        elif len(min_heap) == 2:
            first_num = min_heap[0]
            heappop(min_heap)
            return max(first_num, min_heap[0])
        
        return min_heap[0]
        


