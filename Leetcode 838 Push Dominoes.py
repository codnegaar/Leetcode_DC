'''
Leetcode 838 Push Dominoes
 
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state. 

Example 1:
        Input: dominoes = "RR.L"
        Output: "RR.L"
        Explanation: The first domino expends no additional force on the second domino.

Example 2:
        Input: dominoes = ".L.R...LR..L.."
        Output: "LL.RR.LLRRLL.."
 
Constraints:
        n == dominoes.length
        1 <= n <= 105
        dominoes[i] is either 'L', 'R', or '.'.

'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Simulate the falling of dominoes represented as a string.
        
        Parameters:
        dominoes (str): A string consisting of 'L', 'R', and '.' characters,
                        where:
                          - 'L' represents a domino falling to the left,
                          - 'R' represents a domino falling to the right,
                          - '.' represents a standing domino.
        
        Returns:
        str: The final state of dominoes after all have fallen.
        """

        # Pad the string with virtual dominoes to simplify boundary cases
        s = 'L' + dominoes + 'R'
        n = len(s)
        result = list(s)
        prev = 0  # Index of the last non-dot character (L or R)

        for curr in range(1, n):
            if s[curr] == '.':
                continue  # Skip standing dominoes

            # Range between two forces (prev and curr) has more than one domino
            if curr - prev > 1:
                if s[prev] == s[curr]:
                    # Same direction forces (e.g., R...R or L...L)
                    for i in range(prev + 1, curr):
                        result[i] = s[prev]
                elif s[prev] == 'R' and s[curr] == 'L':
                    # Opposite direction forces (R...L)
                    l, r = prev + 1, curr - 1
                    while l < r:
                        result[l] = 'R'
                        result[r] = 'L'
                        l += 1
                        r -= 1
                    # If l == r, it stays '.'

            prev = curr  # Move to the next force position

        # Strip off the padded virtual dominoes before returning
        return ''.join(result[1:-1])
