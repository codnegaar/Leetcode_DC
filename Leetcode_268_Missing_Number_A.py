class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        checked = set()
      
        for i in nums:
            checked.add(i)
        
        for j in range(0, l + 1):
            if j not in checked:
                return j
              
 
