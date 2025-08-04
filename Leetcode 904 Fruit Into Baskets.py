'''

Leetcode 904 Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
        Input: fruits = [1,2,1]
        Output: 3
        Explanation: We can pick from all 3 trees.

Example 2:
        Input: fruits = [0,1,2,2]
        Output: 3
        Explanation: We can pick from trees [1,2,2].
        If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
        Input: fruits = [1,2,3,2,2]
        Output: 4
        Explanation: We can pick from trees [2,3,2,2].
        If we had started at the first tree, we would only pick from trees [1,2].
         
Constraints:
        1 <= fruits.length <= 105
        0 <= fruits[i] < fruits.length
'''
from typing import List
from collections import defaultdict
import unittest

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Finds the length of the longest subarray with at most two distinct types of fruits.
        Uses the sliding window technique with a dictionary to track fruit counts.

        Parameters:
        fruits (List[int]): A list where each element represents a type of fruit on a tree.

        Returns:
        int: Maximum number of fruits that can be picked with two baskets.
        """
        type_counts = defaultdict(int)
        left = 0
        max_picked = 0

        for right, fruit in enumerate(fruits):
            type_counts[fruit] += 1

            # Shrink the window if more than two types are in the basket
            while len(type_counts) > 2:
                type_counts[fruits[left]] -= 1
                if type_counts[fruits[left]] == 0:
                    del type_counts[fruits[left]]
                left += 1

            max_picked = max(max_picked, right - left + 1)

        return max_picked

