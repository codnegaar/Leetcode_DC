class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # Create an empty array to be filled by sorted numbers
        sorted_nums = [0 for i in range(0,len(nums))] 
        even = 0
        odd = 1
        for i in nums:
            if i % 2 == 0:
                sorted_nums[even] = i
                even +=2
            else:
                sorted_nums[odd] = i
                odd += 2
        return sorted_nums
                
