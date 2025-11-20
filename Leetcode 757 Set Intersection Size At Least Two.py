'''
Leetcode 757 Set Intersection Size At Least Two
 
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.
A containing set is an array nums where each interval from intervals has at least two integers in nums.
For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

Example 1:
        Input: intervals = [[1,3],[3,7],[8,9]]
        Output: 5
        Explanation: let nums = [2, 3, 4, 8, 9].
        It can be shown that there cannot be any containing array of size 4.

Example 2:
        Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
        Output: 3
        Explanation: let nums = [2, 3, 4].
        It can be shown that there cannot be any containing array of size 2.
        
Example 3:
        Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
        Output: 5
        Explanation: let nums = [1, 2, 3, 4, 5].
        It can be shown that there cannot be any containing array of size 4.
 

Constraints:
        1 <= intervals.length <= 3000
        intervals[i].length == 2
        0 <= starti < endi <= 108

'''

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda e: (e[1], -e[0]))

        res = [intervals[0][1]-1, intervals[0][1]]

        for e in intervals[1:]:

            if res[-2] < e[0] and res[-1] >= e[0]:
                res.append(e[1])

            elif e[0] > res[-1]:
                res.extend([e[1]-1, e[1]])

        return len(res)

