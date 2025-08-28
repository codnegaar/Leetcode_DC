'''

Leetcode 3446 Sort Matrix by Diagonals

You are given an n x n square matrix of integers grid. Return the matrix such that:
        The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
        The diagonals in the top-right triangle are sorted in non-decreasing order.
         
Example 1:
Input: grid = [[1,7,3],[9,8,2],[4,5,6]]
Output: [[8,2,3],[9,6,7],[4,5,1]]
Explanation:

            The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

                      [1, 8, 6] becomes [8, 6, 1].
                      [9, 5] and [4] remain unchanged.
            The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:
                      [7, 2] becomes [2, 7].
                      [3] remains unchanged.


Example 2:
        Input: grid = [[0,1],[1,2]]
        Output: [[2,1],[1,0]]
        Explanation: The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:        
        Input: grid = [[1]]
        Output: [[1]]
        Explanation:
                    Diagonals with exactly one element are already in order, so no changes are needed.

 Constraints:
        grid.length == grid[i].length == n
        1 <= n <= 10
        -105 <= grid[i][j] <= 105


'''

from collections import defaultdict
from sortedcontainers import SortedList
from itertools import product
from typing import List


class Solution:
    """
    A class to provide matrix operations.

    Methods
    -------
    sortMatrix(g: List[List[int]]) -> List[List[int]]:
        Sorts the diagonals of a square matrix in ascending order (upper diagonals)
        and descending order (lower diagonals).

    Parameters
    ----------
    g : List[List[int]]
        A square matrix represented as a list of lists of integers.

    Returns
    -------
    List[List[int]]
        The matrix with sorted diagonals.
    """

    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        """
        Sorts all diagonals in the matrix. 
        Upper triangle diagonals are sorted in ascending order, 
        while lower triangle diagonals are sorted in descending order.

        Parameters
        ----------
        g : List[List[int]]
            A square matrix represented as a list of lists of integers.

        Returns
        -------
        List[List[int]]
            Matrix with diagonals sorted.
        """
        n = len(g)
        diagonals = self._collect_diagonals(g, n)
        self._fill_sorted_diagonals(g, n, diagonals)
        return g

    # -------------------- Helper Functions -------------------- #
    
    def _collect_diagonals(self, g: List[List[int]], n: int) -> defaultdict:
        """
        Collects elements from each diagonal into a SortedList for efficient sorting.
        
        Parameters
        ----------
        g : List[List[int]]
            The square matrix.
        n : int
            Dimension of the matrix.
        
        Returns
        -------
        defaultdict(SortedList)
            Dictionary mapping diagonal key (i-j) to a sorted list of elements.
        """
        diagonals = defaultdict(SortedList)
        for i, j in product(range(n), range(n)):
            diagonals[i - j].add(g[i][j])
        return diagonals

    def _fill_sorted_diagonals(self, g: List[List[int]], n: int, diagonals: defaultdict) -> None:
        """
        Fills the matrix with sorted diagonal values from the collected diagonal dictionary.
        
        Parameters
        ----------
        g : List[List[int]]
            The square matrix to be updated.
        n : int
            Dimension of the matrix.
        diagonals : defaultdict(SortedList)
            Dictionary containing diagonals with pre-sorted elements.
        """
        for i, j in product(range(n), range(n)):
            # pop from front if upper diagonal (i < j) -> ascending
            # pop from back if lower diagonal (i >= j) -> descending
            g[i][j] = diagonals[i - j].pop(-(i >= j))

