'''
Leetcode 3479 Fruits Into Baskets III
 
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
From left to right, place the fruits according to these rules:
Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

Example 1:
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:
        fruits[0] = 4 is placed in baskets[1] = 5.
        fruits[1] = 2 is placed in baskets[0] = 3.
        fruits[2] = 5 cannot be placed in baskets[2] = 4.
        Since one fruit type remains unplaced, we return 1.

Example 2:
Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
Explanation:
        fruits[0] = 3 is placed in baskets[0] = 6.
        fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
        fruits[2] = 1 is placed in baskets[1] = 4.
        Since all fruits are successfully placed, we return 0.

Constraints:
        n == fruits.length == baskets.length
        1 <= n <= 105
        1 <= fruits[i], baskets[i] <= 109
'''

from typing import List

class SegmentTree:
    def __init__(self, n: int, baskets: List[int]) -> None:
        self.seg_tree = [0] * (4 * n)
        self.build(1, 0, n - 1, baskets)

    def build(self, parent: int, left: int, right: int, baskets: List[int]) -> None:
        if left == right:
            self.seg_tree[parent] = baskets[left]
            return
        middle = (left + right) // 2
        self.build(parent << 1, left, middle, baskets)
        self.build(parent << 1 | 1, middle + 1, right, baskets)
        self.seg_tree[parent] = max(self.seg_tree[parent << 1], self.seg_tree[parent << 1 | 1])

    def query(self, parent: int, left: int, right: int, target: int) -> int:
        if self.seg_tree[parent] < target:
            return -1
        if left == right:
            return left
        middle = (left + right) // 2
        if self.seg_tree[parent << 1] >= target:
            return self.query(parent << 1, left, middle, target)
        return self.query(parent << 1 | 1, middle + 1, right, target)

    def update(self, parent: int, left: int, right: int, pos: int, val: int) -> None:
        if left == right:
            self.seg_tree[parent] = val
            return
        middle = (left + right) // 2
        if pos <= middle:
            self.update(parent << 1, left, middle, pos, val)
        else:
            self.update(parent << 1 | 1, middle + 1, right, pos, val)
        self.seg_tree[parent] = max(self.seg_tree[parent << 1], self.seg_tree[parent << 1 | 1])


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        st = SegmentTree(n, baskets)  # ✅ FIXED: pass actual number of baskets
        output = 0
        for fruit in fruits:
            pos = st.query(1, 0, n - 1, fruit)
            if pos == -1:
                output += 1
            else:
                st.update(1, 0, n - 1, pos, -1)
        return output

