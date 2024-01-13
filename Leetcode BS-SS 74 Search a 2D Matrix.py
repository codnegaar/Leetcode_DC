'''
Leetcode BS-SS 74 Search a 2D Matrix


You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true
        
Example 2:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false

Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -104 <= matrix[i][j], target <= 10

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left<=right:
            mid = (left+right)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                break
            elif target>matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid-1

        left = 0
        new_list = matrix[mid]
        right = len(new_list)-1
        
        while left<=right:
            mid = (left+right)//2
            if target == new_list[mid]:
                return True
            elif target>new_list[mid]:
                left = mid + 1

            else:
                right = mid-1

        return False

