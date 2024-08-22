'''
Leetcode 476 Number Complement

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement. 

Example 1:
        Input: num = 5
        Output: 2
        Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
        
Example 2:
        Input: num = 1
        Output: 0
        Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
         
Constraints:
        1 <= num < 231

'''
class Solution:
    def findComplement(self, num: int) -> int:
      
        # Determine the bit length of the number
        bit_length = num.bit_length()
        
        # Create a mask with all bits set to 1 of the same length as num
        mask = (1 << bit_length) - 1
        
        # XOR the number with the mask to flip its bits
        return num ^ mask
