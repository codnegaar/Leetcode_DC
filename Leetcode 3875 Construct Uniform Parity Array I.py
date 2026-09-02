'''
Leetcode 3875 Construct Uniform Parity Array I

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]
nums2[i] = nums1[i] - nums1[j], for an index j != i
Return true if it is possible to construct such an array, otherwise, return false.

 

Example 1:

Input: nums1 = [2,3]

Output: true

Explanation:

Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
Choose nums2[1] = nums1[1] = 3.
nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.
Example 2:

Input: nums1 = [4,6]

Output: true

Explanation:​​​​​​​

Choose nums2[0] = nums1[0] = 4.
Choose nums2[1] = nums1[1] = 6.
nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 

Constraints:

1 <= n == nums1.length <= 100
1 <= nums1[i] <= 100
nums1 consists of distinct integers.

'''


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        #return n
        even = 0
        odd= 0
        even_odd = [0] * n
        for i in range(n):
            if nums1[i] % 2 == 0 :
                even +=1

        for i in range(n):
            if nums1[i] % 2 == 1 :
                odd +=1

        if even == n or odd == n : 
            return True

        

        for i in range(n):
            even_odd[i] = nums1[i] % 2

        total_odd = sum(even_odd)
        total_even = n - total_odd

        other_even_count = [total_even] * n
        other_odd_count = [total_odd] * n

        for i in range(n):
            if even_odd[i] == 0 :
                other_even_count[i] = total_even- 1
           
            if even_odd[i] == 1 :
                other_odd_count[i] = total_odd- 1

        #return other_odd_count

        

        can_make_even = True
        can_make_odd = True

        for i in range(n):
            if even_odd[i] == 1 and other_odd_count[i] < 1:
                can_make_even = False
                break

        for i in range(n):
            if even_odd[i] == 0 and other_odd_count[i] < 1:
                can_make_odd = False
                break

        if can_make_even == True or can_make_odd == True :
            return True
        else:
            return False

        

        
                        
            
        #notes : even - even = even
        #notes : odd -even = odd
        # notes : even - odd = odd
        # notes : odd - odd = even 
                
        
