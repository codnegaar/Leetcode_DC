'''

An additive number is a string whose digits can form an additive sequence.
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent 
number in the sequence must be the sum of the preceding two.
Given a string containing only digits, return true if it is an additive number or false otherwise.
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.


Example 1:
        Input: "112358"
        Output: true
        Explanation: 
        The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
        1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
        
Example 2:
        Input: "199100199"
        Output: true
        Explanation: 
        The additive sequence is: 1, 99, 100, 199. 
        1 + 99 = 100, 99 + 100 = 199

Constraints:
        1 <= num.length <= 35
        num consists only of digits.

'''

class Solution:
  def isAdditiveNumber(self, num: str) -> bool:
    n = len(num)

    def dfs(firstNum: int, secondNum: int, s: int) -> bool:
      if s == len(num):
        return True

      thirdNum = firstNum + secondNum
      thirdNumStr = str(thirdNum)

      return num.find(thirdNumStr, s) == s and dfs(secondNum, thirdNum, s + len(thirdNumStr))

    # num[0..i] = firstNum
    for i in range(n // 2):
      if i > 0 and num[0] == '0':
        return False
      firstNum = int(num[:i + 1])
      # num[i + 1..j] = secondNum
      # Len(thirdNum) >= max(len(firstNum), len(secondNum))
      j = i + 1
      while max(i, j - i) < n - j:
        if j > i + 1 and num[i + 1] == '0':
          break
        secondNum = int(num[i + 1:j + 1])
        if dfs(firstNum, secondNum, j + 1):
          return True
        j += 1

    return False

