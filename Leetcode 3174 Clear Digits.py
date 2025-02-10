'''
Leetcode 3174 Clear Digits
 
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
        Delete the first digit and the closest non-digit character to its left.
        Return the resulting string after removing all digits.

Example 1:
        Input: s = "abc"
        Output: "abc"
        Explanation: There is no digit in the string.

Example 2:
        Input: s = "cb34"
        Output: ""
        Explanation: First, we apply the operation on s[2], and s becomes "c4".
        
        Then we apply the operation on s[1], and s becomes "".

Constraints:
        1 <= s.length <= 100
        s consists only of lowercase English letters and digits.
        The input is generated such that it is possible to delete all digits.

'''


class Solution:
    def clearDigits(self, s: str) -> str:
        """
        Removes the character preceding each digit in the input string.

        Parameters:
        s (str): The input string containing alphanumeric characters.

        Returns:
        str: The modified string after removing preceding characters of digits.
        """
        if not s:
            return ""  # Edge case: empty string input

        stack = []  # Stack to store non-digit characters
        
        for char in s:
            if char.isdigit():  
                if stack:  # Ensure stack is not empty before popping
                    stack.pop()  # Remove the last added character
            else:
                stack.append(char)  # Add non-digit characters to stack
        
        return "".join(stack)  # Convert list back to string


# Example Implementation
if __name__ == "__main__":
    solution = Solution()
    test_string = "abc1d2e3f4g5h"
    print("Output:", solution.clearDigits(test_string))  # Expected: "h"

