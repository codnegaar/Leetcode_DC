'''
Leetcode 1128 Number of Equivalent Domino Pairs
 
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, 
one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j]. 

Example 1:
        Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
        Output: 1

Example 2:
        Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
        Output: 3
 
Constraints:
        1 <= dominoes.length <= 4 * 104
        dominoes[i].length == 2
        1 <= dominoes[i][j] <= 9
'''

class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        return sum(f*(f-1)//2 for f in Counter(map(tuple,map(sorted,a))).values())
