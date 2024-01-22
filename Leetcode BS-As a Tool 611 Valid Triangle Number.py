'''
Leetcode BS-As a Tool 611 Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:
        Input: nums = [2,2,3,4]
        Output: 3
        Explanation: Valid combinations are: 
        2,3,4 (using the first 2)
        2,3,4 (using the second 2)
        2,2,3

Example 2:
        Input: nums = [4,2,3,4]
        Output: 4
 
Constraints:
        1 <= nums.length <= 1000
        0 <= nums[i] <= 1000
        
'''

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() 
        count = 0        
     
        for i in range(len(nums) - 2):
            k = i + 2          
            if nums[i] == 0:
                continue
        
            if nums[i+1] == 0 and nums[-1] == 0:
                break
            
            for j in range(i + 1, len(nums) - 1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
        return count
