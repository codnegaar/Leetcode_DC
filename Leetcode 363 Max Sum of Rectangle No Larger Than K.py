'''
363 Max Sum of Rectangle No Larger Than K
Given an m x n matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
It is guaranteed that there will be a rectangle with a sum no larger than k. 

Example 1:
        Input: matrix = [[1,0,1],[0,-2,3]], k = 2
        Output: 2
        Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
        
Example 2:
        Input: matrix = [[2,2,-1]], k = 3
        Output: 3
 
Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -100 <= matrix[i][j] <= 100
        -105 <= k <= 105
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def lower_bound(self, value):
        node = self.root
        ret = None
        while node is not None:
            if value < node.val:
                ret = node.val
                node = node.left
            elif value == node.val:
                ret = node.val
                return ret
            else:
                node = node.right
        return ret

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        last_node = None
        node = self.root
        while node is not None:
            last_node = node
            if value < node.val:
                node = node.left
            else:
                node = node.right
        if value < last_node.val:
            last_node.left = Node(value)
        else:
            last_node.right = Node(value)

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) > len(matrix[0]):
            new_matrix = []
            for i in range(len(matrix[0])):
                new_matrix.append([])
                for j in range(len(matrix)):
                    new_matrix[i].append(matrix[j][i])
            matrix = new_matrix
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        sum_matrix = [[0 for j in range(num_cols + 1)] for i in range(num_rows + 1)]
        for i in range(num_rows):
            for j in range(num_cols):
                sum_matrix[i + 1][j + 1] = matrix[i][j] + sum_matrix[i + 1][j] + sum_matrix[i][j + 1] - sum_matrix[i][j]

        ret = - int(1 << 30)
        for height in range(1, num_rows + 1):
            for top in range(1, num_rows - height + 1 + 1):
                bottom = top + height - 1
                bst = BinarySearchTree()
                bst.insert(0)
                for right in range(1, num_cols + 1):
                    current_sum = sum_matrix[bottom][right] - sum_matrix[top - 1][right]
                    left_sum = bst.lower_bound(current_sum - k)
                    # print(right, current_sum, left_sum)
                    if left_sum is not None:
                        ret = max(ret, current_sum - left_sum)
                    bst.insert(current_sum)
        return ret
