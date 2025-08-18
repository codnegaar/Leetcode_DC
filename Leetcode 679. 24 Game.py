'''
Leetcode 679. 24 Game
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical
expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:
        The division operator '/' represents real division, not integer division.
        For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
        Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
        For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
        You cannot concatenate numbers together
        For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
        Return true if you can get such expression that evaluates to 24, and false otherwise. 

Example 1:
        Input: cards = [4,1,8,7]
        Output: true
        Explanation: (8-4) * (7-1) = 24

Example 2:
        Input: cards = [1,2,1,2]
        Output: false 

Constraints:
        cards.length == 4
        1 <= cards[i] <= 9
'''

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(arr):
            nonlocal res

            # action; process the left index to see if it matches with 24
            if len(arr) == 1:
                temp = abs(arr[0] - 24) < 1e-6 
                res = res or temp
                return res

            # build pairs in arr
            n = len(arr)

            # select first value in the pair
            for i in range(n):

                # select the second value in pair
                for j in range(i + 1, n):
                    n1, n2 = arr[i], arr[j]

                    # remove n1 and n2 from arr
                    new_arr = [arr[k] for k in range(n) if k != i and k != j]

                    # case1; generate possible val from pairing n1 & n2
                    # covers +, -, * cases
                    for val in [n1 + n2, n1 - n2, n2 - n1, n1 * n2]:
                        # append val to new_arr and recur
                        dfs(new_arr + [val])

                    # case2; covers division over n1
                    if n1:
                        dfs(new_arr + [n2/n1])

                    # case3; covers division over n2
                    if n2:
                        dfs(new_arr + [n1/n2])

        res = False

        # run dfs with current cards array
        dfs(cards)

        return res
