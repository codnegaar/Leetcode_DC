'''
Leetcode 42 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
    In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9
 
Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


# Second solution
class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall=right_wall= 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        for i in range(n):
            j = -i -1

            max_left[i]= left_wall
            max_right[j] = right_wall

            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])
            
        summ = 0
        for i in range(n):
            pottential = min(max_left[i], max_right[i])
            summ += max(0, pottential - height[i])
        return summ
            
        
        
            
        
        
        
        
