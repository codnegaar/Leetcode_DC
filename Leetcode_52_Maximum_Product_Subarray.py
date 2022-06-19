'''

Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6

'''

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
        
 

'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos =  nums[0]
        neg =  nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            pos = max(num, pos * num, neg * num)
            neg = min(num, pos * num, neg * num)
            result = max(result, pos)
        return result


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6

'''
