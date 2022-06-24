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

