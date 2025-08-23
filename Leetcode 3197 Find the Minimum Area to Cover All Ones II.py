'''
Leetcode 3197 Find the Minimum Area to Cover All Ones II
 
You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.
Return the minimum possible sum of the area of these rectangles.
Note that the rectangles are allowed to touch. 

Example 1:
        Input: grid = [[1,0,1],[1,1,1]]
        Output: 5
        Explanation:
                The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
                The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
                The 1 at (1, 1) is covered by a rectangle of area 1.

Example 2:
        Input: grid = [[1,0,1,0],[0,1,0,1]]
        Output: 5
        Explanation:
                The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
                The 1 at (1, 1) is covered by a rectangle of area 1.
                The 1 at (1, 3) is covered by a rectangle of area 1.
 

Constraints:
        1 <= grid.length, grid[i].length <= 30
        grid[i][j] is either 0 or 1.
        The input is generated such that there are at least three 1's in grid.

'''
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def get_area(rect):
            a, b, c, d = rect
            x1, y1, x2, y2 = inf,inf, -1, -1
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    if grid[i][j]:
                        x1 = min(x1, i)
                        y1 = min(y1, j)
                        x2 = max(x2, i)
                        y2 = max(y2, j)
            if x1 ==inf:
                return 0
            return (x2 - x1 + 1) * (y2 - y1 + 1)
        
        def iter_splits(rect):
            x1, y1, x2, y2 = rect
            for i in range(x1, x2):
                rect1 = (x1, y1, i, y2)
                rect2 = (i + 1, y1, x2, y2)
                yield rect1, rect2
            for j in range(y1, y2):
                rect1 = (x1, y1, x2, j)
                rect2 = (x1, j + 1, x2, y2)
                yield rect1, rect2
        
        def solve(rect, splits=2):
            if splits == 0:
                return get_area(rect)
            ans =inf
            for rect1, rect2 in iter_splits(rect):
                for i in range(splits):
                    ans = min(ans, solve(rect1, i) + solve(rect2, splits -1 - i))
            return ans
        
        return solve((0, 0, n - 1, m - 1))
