class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1 for i in range(len(nums))]
        
        post = [1 for i in range(len(nums))]
        
        
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

            
        ans = []
        
        for p1, p2 in zip(pre, post):
            ans.append(p1 * p2)
            
        return ans 
