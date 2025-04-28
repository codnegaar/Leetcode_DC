'''
Leetcode 391 Perfect Rectangle
 
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. 
The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).
Return true if all the rectangles together form an exact cover of a rectangular region. 

Example 1:
        Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
        Output: true
        Explanation: All 5 rectangles together form an exact cover of a rectangular region.

Example 2:
        Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
        Output: false
        Explanation: Because there is a gap between the two rectangular regions.

Example 3:
        Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
        Output: false
        Explanation: Because two of the rectangles overlap with each other.         

Constraints:
        1 <= rectangles.length <= 2 * 104
        rectangles[i].length == 4
        -105 <= xi < ai <= 105
        -105 <= yi < bi <= 105
        
'''

from typing import List
import itertools

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Determines if a set of small rectangles perfectly covers a larger rectangle
        without any overlaps or gaps.

        Parameters:
        rectangles (List[List[int]]): A list where each rectangle is represented 
                                      by [x1, y1, x2, y2] coordinates.

        Returns:
        bool: True if the rectangles form a perfect cover, False otherwise.
        """
        # Initialize boundary coordinates
        min_x = min_y = 10 ** 5 + 1
        max_x = max_y = -10 ** 5 - 1
        total_area = 0
        points_set = set()

        for x1, y1, x2, y2 in rectangles:
            # Update boundaries for the overall rectangle
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Accumulate the area of each small rectangle
            total_area += (x2 - x1) * (y2 - y1)

            # Track corners using set and XOR (add if not exist, remove if exist)
            for corner in itertools.product([x1, x2], [y1, y2]):
                if corner in points_set:
                    points_set.remove(corner)
                else:
                    points_set.add(corner)

        # After processing all rectangles, only four corners should remain
        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        # Verify the remaining points and total area
        return points_set == expected_corners and total_area == (max_x - min_x) * (max_y - min_y)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    rectangles = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]
    result = solution.isRectangleCover(rectangles)
    print(f"Do the rectangles form a perfect cover? {result}")
