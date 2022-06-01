class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        checked = set()
      
        for i in nums:
            checked.add(i)
        
        for j in range(0, l + 1):
            if j not in checked:
                return j
              
              
  ''''
// Java solution:

class Solution {   
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int  expected = (n*(n+1))/2;
        int numsSum = 0;
        for ( int i: nums){
            numsSum += i;       
        }        
         return expected - numsSum ;
    }
}
  
  
  .'''
