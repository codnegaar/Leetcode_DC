class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if min(nums)>0:
            return reduce(lambda x, y: x*y, nums)
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                temp = locMax
                locMax = max(locMin*nums[i], nums[i])
                locMin = min(temp*nums[i], nums[i])
            else:
                locMax=max(locMax*nums[i], nums[i])
                locMin=min(locMin*nums[i], nums[i])
            print(locMax, locMin)
            gloMax=max(gloMax, locMax)
        return gloMax
        
