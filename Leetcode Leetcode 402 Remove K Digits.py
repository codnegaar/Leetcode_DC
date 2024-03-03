'''
Leetcode 402 Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
        Input: num = "1432219", k = 3
        Output: "1219"
        Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
        Input: num = "10200", k = 1
        Output: "200"
        Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
        Input: num = "10", k = 2
        Output: "0"
        Explanation: Remove all the digits from the number and it is left with nothing which is 0.      

Constraints:
        1 <= k <= num.length <= 105
        num consists of only digits.
        num does not have any leading zeros except for the zero itself
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # Use a stack to keep track of the digits
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:  # Pop digits from the stack until the top digit is smaller than the current digit or k becomes 0
                stack.pop()
                k -= 1
            stack.append(digit)  # Append the current digit to the stack
        while k > 0:  # If there are still digits to be removed, pop them from the stack
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")  # Convert the remaining digits to a string and remove any leading zeroes
        return result if result else "0"  # Return the resulting string, or "0" if there are no remaining digits
