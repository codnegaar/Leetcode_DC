'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].




'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

       
       
# second solution:

class Solution(object):
    def letterCombinations(self, digits):
        
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def dfs(digits, d, l, cur, ans):
            
            if l == len(digits):
                if l > 0:
                    ans.append("".join(cur))
                    
                return
        
            for c in d[ord(digits[l]) - ord('0')]:
                cur[l] = c
                dfs(digits, d, l + 1, cur, ans)
        
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
        cur = [' ' for _ in range(len(digits))]
        ans = []
        dfs(digits, d, 0, cur, ans)
        return ans
