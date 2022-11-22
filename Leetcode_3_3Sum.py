
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index , value in enumerate(nums):
            if index > 0 and value == nums[index -1]:
                continue            
            left, right = index +1, len(nums) -1
            while left< right:
                threeSum = value +nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1  # derement the right pointer
                elif threeSum < 0:
                    left += 1   # increment the right pointer
                else:
                    result.append([value, nums[left], nums[right]])
        return -1
    
