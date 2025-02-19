'''
Leetcode 79 Word Search

Given an m x n grid of characters board and a string word, return true if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false
 
Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
    

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)

# Second solution
class Solution:
    """
    Class to check if a given word exists in a 2D board by constructing it 
    sequentially using adjacent letters (horizontally or vertically).

    Methods:
    --------
    exist(board: List[List[str]], word: str) -> bool
        Checks if the given word can be constructed in the 2D board.
    """

    def exist(self, board, word):
        """
        Determines if the given word exists in the 2D board by navigating 
        horizontally or vertically adjacent cells.

        Parameters:
        -----------
        board : List[List[str]]
            2D grid of characters where the word must be searched.
        word : str
            Word to be searched in the board.

        Returns:
        --------
        bool
            True if the word exists in the board, False otherwise.
        """
        # Number of rows and columns in the board
        rows, cols = len(board), len(board[0])

        # Helper function to perform backtracking
        def backtrack(i, j, k):
            # Base case: if the entire word is found
            if k == len(word):
                return True
            
            # Boundary conditions or mismatch check
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # Temporarily mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore all four possible directions
            found = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i, j - 1, k + 1)
            )

            # Restore the cell's original value
            board[i][j] = temp

            return found

        # Iterate through each cell in the board to find the word
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False


# Example implementation
if __name__ == "__main__":
    solution = Solution()
    
    # Sample board and word
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"

    print("Does the word exist in the board?", solution.exist(board, word))

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_word_exists(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_word_not_exists(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))
    
    def test_empty_word(self):
        board = [['A']]
        word = ""
        self.assertTrue(self.solution.exist(board, word))
    
    def test_empty_board(self):
        board = [[]]
        word = "A"
        self.assertFalse(self.solution.exist(board, word))

if __name__ == "__main__":
    unittest.main()

"""
# Changes Made:
1. Improved the efficiency by adding boundary conditions in `backtrack` to reduce redundant checks.
2. Added clear comments to explain each step of the code.
3. Refactored the helper function for better readability.
4. Included Python unit tests to validate the solution.
5. Formatted the code for readability and maintainability.

# References:
- Python Documentation on Lists: https://docs.python.org/3/tutorial/datastructures.html
"""


from typing import List

class Solution:
    """
    Class to check if a given word exists in a 2D board by constructing it 
    sequentially using adjacent letters (horizontally or vertically).
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determines if the given word exists in the 2D board by navigating 
        horizontally or vertically adjacent cells.

        Parameters:
        -----------
        board : List[List[str]]
            2D grid of characters where the word must be searched.
        word : str
            Word to be searched in the board.

        Returns:
        --------
        bool
            True if the word exists in the board, False otherwise.
        """
        rows, cols = len(board), len(board[0])

        def backtrack(i: int, j: int, k: int) -> bool:
            """
            Backtracking function to search for the word in the board.

            Parameters:
            -----------
            i : int
                Current row index.
            j : int
                Current column index.
            k : int
                Index of the character in `word` that needs to be matched.

            Returns:
            --------
            bool
                True if the word is found, otherwise False.
            """
            # Base case: If all characters are matched
            if k == len(word):
                return True

            # Boundary checks and character mismatch check
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # Temporarily mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'  # Use '#' as a placeholder to prevent revisiting

            # Explore all four directions (up, down, left, right)
            found = (
                backtrack(i + 1, j, k + 1) or  # Down
                backtrack(i - 1, j, k + 1) or  # Up
                backtrack(i, j + 1, k + 1) or  # Right
                backtrack(i, j - 1, k + 1)     # Left
            )

            # Restore the cell's original value (backtracking)
            board[i][j] = temp

            return found

        # Iterate through each cell in the board to find the word
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):  # Start DFS from this cell
                    return True

        return False

# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCCED"
        ),  # Expected output: True

        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "SEE"
        ),  # Expected output: True

        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCB"
        ),  # Expected output: False
    ]

    for board, word in test_cases:
        print(f"Word '{word}' exists in board: {solution.exist(board, word)}")


