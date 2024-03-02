'''

Leetcode 357 Count Numbers with Unique Digits

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:
        Input: n = 2
        Output: 91
        Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
        Input: n = 0
        Output: 1

Constraints:
        0 <= n <= 8

'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        # The maximum number of unique digits we can have is 10, since we have 10 digits in base 10
        # For n > 10, there will be repetition, so the count will be the same as countNumbersWithUniqueDigits(10)
        n = min(n, 10)
        
        # Start with a base count of 10, since we can always have 0 to 9 as the first digit
        count = 10
        
        # For the second digit, we can have 9 choices, since 0 is already used
        # For the third digit, we can have 9 choices again, since we cannot repeat the first or second digit
        # For the fourth digit, we can have 8 choices, and so on
        # The total count is the product of the number of choices for each digit
        for i in range(2, n + 1):
            choices = 9
            for j in range(i - 1):
                choices *= 9 - j
            count += choices
        
        return count
