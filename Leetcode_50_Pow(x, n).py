'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
-104 <= xn <= 104



'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: 
            return 1
        if n < 0:
            div = True; n = -n
        else: 
            div = False
        stack = []
        while n != 1 and n != -1:
            if n % 2 == 0:
                stack.append(1)
            else: 
                stack.append(x)
            n //= 2
        result = x
        while len(stack) != 0:
            result = result * result * stack.pop()
        if div:
            return 1.0 / result
        else:
            return result
        
# new solution

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res




