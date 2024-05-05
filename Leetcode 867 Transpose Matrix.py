'''

Leetcode 867 Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
        Input: matrix = [[1,2,3],[4,5,6]]
        Output: [[1,4],[2,5],[3,6]]
 

Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 1000
        1 <= m * n <= 105
        -109 <= matrix[i][j] <= 109

'''
class Solution:
    """
    A class to perform operations on matrices.
    """
    def transpose(self, matrix):
        """
        Transposes a given 2D matrix, swapping its rows with columns.

        :param matrix: A list of lists representing the matrix to be transposed.
        :type matrix: List[List[int]]
        :return: A new transposed matrix.
        :rtype: List[List[int]]
        """
        # Determine the number of rows and columns in the input matrix.
        row_count = len(matrix)
        col_count = len(matrix[0])
        
        # Create a new matrix with dimensions inverted from the original.
        transposed_matrix = [[0] * row_count for _ in range(col_count)]
        
        # Fill the transposed matrix with elements swapped from rows to columns.
        for i in range(col_count):
            for j in range(row_count):
                transposed_matrix[i][j] = matrix[j][i]

        return transposed_matrix
