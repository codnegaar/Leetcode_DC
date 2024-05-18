'''
Leetcode 979 Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin. 

Example 1:
        Input: root = [3,0,0]
        Output: 2
        Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
        Input: root = [0,3,0]
        Output: 3
        Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
         

Constraints:
        The number of nodes in the tree is n.
        1 <= n <= 100
        0 <= Node.val <= n
        The sum of all Node.val is n.

'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def moveCoins(node: Optional[TreeNode], parent: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            # Recursively calculate moves for left and right children
            left_moves = moveCoins(node.left, node)
            right_moves = moveCoins(node.right, node)
            
            # Total moves from both subtrees
            total_moves = left_moves + right_moves
            
            # Excess coins at this node
            excess_coins = node.val - 1
            
            # Pass excess coins to parent
            if parent is not None:
                parent.val += excess_coins
            
            # Add absolute value of excess coins to total moves
            total_moves += abs(excess_coins)
            
            return total_moves
        
        return moveCoins(root, None)
