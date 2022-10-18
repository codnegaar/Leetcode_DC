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
        

