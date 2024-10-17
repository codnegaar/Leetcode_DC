'''
Leetcode 670 Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
        Input: num = 2736
        Output: 7236
        Explanation: Swap the number 2 and the number 7.

Example 2:
        Input: num = 9973
        Output: 9973
        Explanation: No swap.
 
Constraints:
  0 <= num <= 108
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits (as integers)
        num_list = [int(digit) for digit in str(num)]
        
        # Track the last occurrence of each digit (0-9)
        last = {digit: i for i, digit in enumerate(num_list)}
        
        # Traverse the digits from left to right
        for i in range(len(num_list)):
            current_digit = num_list[i]
            
            # Look for a larger digit that appears later in the number
            for d in range(9, current_digit, -1):
                # Check if the digit `d` exists in the last occurrence dictionary
                if d in last and last[d] > i:
                    # Swap the current digit with the larger digit found later
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    # Return the new number after the swap
                    return int(''.join(map(str, num_list)))
        
        # If no swap occurred, return the original number
        return num
