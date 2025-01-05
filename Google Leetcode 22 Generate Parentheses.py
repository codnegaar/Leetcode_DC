'''
Google Leetcode 22 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return
                
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)

        return res


# Second Solution
from typing import List, Generator

class Solution:
    """
    Generate all combinations of well-formed parentheses.

    Args:
        n (int): Number of pairs of parentheses.

    Returns:
        List[str]: All valid combinations of `n` pairs of parentheses.
    """

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid parentheses combinations using backtracking.

        The function uses a generator to build the combinations incrementally,
        ensuring minimal memory usage and avoiding unnecessary storage.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            List[str]: List of all valid parentheses combinations.
        """
        def backtrack(open_count: int, close_count: int, current: str) -> Generator[str, None, None]:
            # If the current string is complete, yield the result
            if len(current) == 2 * n:
                yield current
                return

            # Add an open parenthesis if allowed
            if open_count < n:
                yield from backtrack(open_count + 1, close_count, current + '(')

            # Add a close parenthesis if it balances an open one
            if close_count < open_count:
                yield from backtrack(open_count, close_count + 1, current + ')')

        # Return all generated combinations as a list
        return list(backtrack(0, 0, ""))

# Unit Test
def test_generateParenthesis():
    sol = Solution()

    # Test Case 1: n = 1
    assert sol.generateParenthesis(1) == ["()"], "Test Case 1 Failed"

    # Test Case 2: n = 2
    assert sol.generateParenthesis(2) == ["(())", "()()"], "Test Case 2 Failed"

    # Test Case 3: n = 3
    assert sol.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"], "Test Case 3 Failed"

    # Test Case 4: n = 4
    assert sol.generateParenthesis(4) == [
        "(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
        "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()",
        "()()(())", "()()()()"
    ], "Test Case 4 Failed"

    # Test Case 5: Edge case n = 0 (No pairs of parentheses)
    assert sol.generateParenthesis(0) == [""], "Test Case 5 Failed"

    print("All test cases passed.")

# Run unit tests
test_generateParenthesis()

