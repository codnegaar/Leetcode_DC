'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
        Each of the digits 1-9 must occur exactly once in each row.
        Each of the digits 1-9 must occur exactly once in each column.
        Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
        The '.' character indicates empty cells.

 

Example 1:
        Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        
        Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:
        board.length == 9
        board[i].length == 9
        board[i][j] is a digit or '.'.
        It is guaranteed that the input board has only one solution.

'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid_move(r, c, n):
            for i in range(9):
                if board[i][c]==n:
                    return False
                if board[r][i]==n: 
                    return False
                if board[3*(r//3)+i//3][3*(c//3)+i%3]==n: 
                    return False
            return True
        
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c]!=".": continue
                    for n in "123456789":
                        if valid_move(r, c, n):
                            board[r][c] = n
                            if backtrack():
                                return True
                            board[r][c] = "."
                    return False
            return True
        backtrack()
        
 # second solution
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        n, N = 3, 9
        rows = [[0] * (N + 1) for _ in range(N)]
        cols = [[0] * (N + 1) for _ in range(N)]
        boxes = [[0] * (N + 1) for _ in range(N)]
        sudokuSolved = False

        def couldPlace(d, row, col):
            idx = (row // n) * n + col // n
            return rows[row][d] + cols[col][d] + boxes[idx][d] == 0

        def placeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[idx][d] += 1
            board[row][col] = str(d)

        def removeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] -= 1
            cols[col][d] -= 1
            boxes[idx][d] -= 1
            board[row][col] = '.'

        def placeNextNumbers(row, col):
            nonlocal sudokuSolved
            if row == N - 1 and col == N - 1:
                sudokuSolved = True
            elif col == N - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)

        def backtrack(row, col):
            nonlocal sudokuSolved
            if board[row][col] == '.':
                for d in range(1, 10):
                    if couldPlace(d, row, col):
                        placeNumber(d, row, col)
                        placeNextNumbers(row, col)
                        if not sudokuSolved:
                            removeNumber(d, row, col)
            else:
                placeNextNumbers(row, col)

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)
        backtrack(0, 0)
