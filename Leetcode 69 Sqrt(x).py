'''
Leetcode 69 Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
    Input: x = 4
    Output: 2

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
     
Constraints:
    0 <= x <= 231 - 1

'''

class Solution:
    """
    A class to compute the square root of a non-negative integer using binary search.
    """

    def mySqrt(self, x: int) -> int:
        """
        Computes the integer part of the square root of a given non-negative integer x.
        
        Parameters:
        - x (int): The number to compute the square root of.

        Returns:
        - int: The integer part of the square root of x.
        """
        if x < 2:
            return x  # Handle cases where x is 0 or 1

        # Binary search initialization
        l, r = 1, x  # Search range between 1 and x

        while l <= r:
            mid = (l + r) >> 1  # Calculate the middle point using bitwise shift for efficiency

            # Check if mid squared equals x
            if mid * mid == x:
                return mid
            elif mid * mid < x:  # If mid squared is less than x, search the right half
                l = mid + 1
            else:  # If mid squared is greater than x, search the left half
                r = mid - 1

        # The largest mid where mid^2 <= x will be at l - 1
        return l - 1


# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_input = 8
    print("Square root of", example_input, "is:", solution.mySqrt(example_input))

# Unit Tests
def test_mySqrt():
    solution = Solution()
    assert solution.mySqrt(0) == 0, "Test case 1 failed"
    assert solution.mySqrt(1) == 1, "Test case 2 failed"
    assert solution.mySqrt(4) == 2, "Test case 3 failed"
    assert solution.mySqrt(8) == 2, "Test case 4 failed"
    assert solution.mySqrt(16) == 4, "Test case 5 failed"
    assert solution.mySqrt(27) == 5, "Test case 6 failed"
    assert solution.mySqrt(2147395599) == 46339, "Test case 7 failed"
    print("All test cases passed!")

test_mySqrt()

# Changes made:
# 1. Added a docstring to describe the method's purpose and its parameters/return values.
# 2. Added a condition to handle small inputs (x < 2) upfront.
# 3. Commented on each logical step in the binary search for clarity.
# 4. Provided an example usage for demonstration purposes.
# 5. Added a unit test suite with multiple test cases to validate functionality.


