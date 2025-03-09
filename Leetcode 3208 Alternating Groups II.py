'''

Leetcode 3208 Alternating Groups II

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
Return the number of alternating groups.
Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

Example 1:
        Input: colors = [0,1,0,1,0], k = 3
        Output: 3

Example 2:
        Input: colors = [0,1,0,0,1,0,1], k = 6
        Output: 2

Example 3:
        Input: colors = [1,1,0,1], k = 4
        Output: 0

Constraints:
        3 <= colors.length <= 105
        0 <= colors[i] <= 1
        3 <= k <= colors.length

'''

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        Calculate the number of continuous groups of 'k' or more distinct integers 
        where each group consists of strictly alternating colors.
        
        Parameters:
        - colors (List[int]): The list of integers representing colors.
        - k (int): The minimum length of an alternating group to be counted.

        Returns:
        - int: The number of valid alternating groups of length at least 'k'.
        """
        # Append the initial part of the array to handle circular conditions
        # with a complexity of O(k) in space.
        extended_colors = colors + colors[:k-1]
        n = len(extended_colors)
        count = 0
        left = 0  # Start of the current valid group

        # Iterate over extended array to find alternating groups.
        for right in range(n):
            # Reset start if current and previous elements are the same
            if right > 0 and extended_colors[right] == extended_colors[right - 1]:
                left = right

            # Increment count if the length of the segment is at least 'k'
            if right - left + 1 >= k:
                count += 1

        return count

