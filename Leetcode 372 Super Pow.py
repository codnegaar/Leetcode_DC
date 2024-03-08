'''

Leetcode 372 Super Pow

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array. 

Example 1:
        Input: a = 2, b = [3]
        Output: 8

Example 2:
        Input: a = 2, b = [1,0]
        Output: 1024

Example 3:
        Input: a = 1, b = [4,3,3,8,5,2]
        Output: 1 

Constraints:
        1 <= a <= 231 - 1
        1 <= b.length <= 2000
        0 <= b[i] <= 9
        b does not contain leading zeros.
        
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        exp=0
        for e in b:
            exp=e+10*exp
            exp%=1140
            if exp==0: exp=1140 #Add this line can save old solution
        return pow(a, exp, 1337)
        


