class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()
        for i  in nums:
            if i in checkSet:
                return True
            checkSet.add(i)
        return False
        
