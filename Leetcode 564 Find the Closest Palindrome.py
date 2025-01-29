'''
Leetcode 564 Find the Closest Palindrome

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
The closest is defined as the absolute difference minimized between two integers. 

Example 1:
        Input: n = "123"
        Output: "121"
      
Example 2:
        Input: n = "1"
        Output: "0"
        Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
         
Constraints:
        1 <= n.length <= 18
        n consists of only digits.
        n does not have leading zeros.
        n is representing an integer in the range [1, 1018 - 1].
'''
class Solution:
    def nearestPalindromic(self, numberStr: str) -> str:
        number = int(numberStr)
        length = len(numberStr)
        leftHalf = int(numberStr[:(length + 1) // 2])

        # Generate candidate palindromes by tweaking the left half
        candidates = [
            self.createPalindrome(leftHalf - 1, length % 2 == 0),
            self.createPalindrome(leftHalf, length % 2 == 0),
            self.createPalindrome(leftHalf + 1, length % 2 == 0),
            10**(length - 1) - 1,  # Edge case: one digit less
            10**length + 1         # Edge case: one digit more
        ]

        # Exclude the original number if it's a palindrome
        candidates = [c for c in candidates if c != number]

        # Return the closest palindrome (smallest difference and smallest value if tied)
        return str(min(candidates, key=lambda x: (abs(x - number), x)))

    def createPalindrome(self, leftHalf: int, even: bool) -> int:
        halfStr = str(leftHalf)
        return int(halfStr + halfStr[:-1][::-1] if not even else halfStr + halfStr[::-1])

