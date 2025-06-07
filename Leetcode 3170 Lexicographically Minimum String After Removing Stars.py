'''
Leetcode 3170 Lexicographically Minimum String After Removing Stars

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:
Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.
 
Example 1:
        Input: s = "aaba*"
        Output: "aab"
        Explanation:We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:
        Input: s = "abc"
        Output: "abc"
        Explanation: There is no '*' in the string.

Constraints:
        1 <= s.length <= 105
        s consists only of lowercase English letters and '*'.
        The input is generated such that it is possible to delete all '*' characters.

'''
import heapq
from collections import defaultdict, deque

class Solution(object):
    def clearStars(self, s):
        n = len(s)
        pq = []  # Min-heap to store characters
        m = defaultdict(deque)  # Map character -> deque of indices
        keep = [True] * n  # Marks whether to keep character at index

        for i in range(n):
            if s[i] == '*':
                smallest = heapq.heappop(pq)  # Get smallest character
                idx = m[smallest].pop()      # Remove last occurrence index
                keep[i] = False              # Mark '*' for removal
                keep[idx] = False            # Mark smallest char for removal
            else:
                heapq.heappush(pq, s[i])
                m[s[i]].append(i)

        # Build result from characters not marked for removal
        return ''.join(s[i] for i in range(n) if keep[i])
