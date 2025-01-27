'''
Leetcode 50 Pow(x, n)

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

# Solution
class Solution:
    """
    A class to compute the power of a number using an efficient recursive method.
    """

    def myPow(self, x: float, n: int) -> float:
        """
        Computes x raised to the power n (x^n) using a recursive approach.

        Parameters:
        - x (float): The base number.
        - n (int): The exponent, can be positive, negative, or zero.

        Returns:
        - float: The result of x raised to the power n.
        """

        # Helper function for recursive computation
        def power(base: float, exponent: int) -> float:
            if exponent == 0:  # Base case: any number to the power of 0 is 1
                return 1
            elif exponent % 2 == 0:  # If the exponent is even
                return power(base * base, exponent // 2)
            else:  # If the exponent is odd
                return base * power(base * base, (exponent - 1) // 2)

        # Compute the result using the helper function
        result = power(x, abs(n))

        # Handle positive and negative exponents
        return result if n >= 0 else 1 / result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    print("2^10 =", solution.myPow(2.0, 10))  # Output: 1024.0
    print("2^-3 =", solution.myPow(2.0, -3))  # Output: 0.125
    print("3^0 =", solution.myPow(3.0, 0))    # Output: 1.0


# Unit Tests
def test_myPow():
    solution = Solution()

    assert abs(solution.myPow(2.0, 10) - 1024.0) < 1e-6, "Test case 1 failed"
    assert abs(solution.myPow(2.0, -3) - 0.125) < 1e-6, "Test case 2 failed"
    assert abs(solution.myPow(3.0, 0) - 1.0) < 1e-6, "Test case 3 failed"
    assert abs(solution.myPow(0.0, 5) - 0.0) < 1e-6, "Test case 4 failed"
    assert abs(solution.myPow(1.0, -1000) - 1.0) < 1e-6, "Test case 5 failed"
    assert abs(solution.myPow(2.1, 3) - (2.1**3)) < 1e-6, "Test case 6 failed"
    print("All test cases passed!")


test_myPow()



