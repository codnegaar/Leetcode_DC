'''

Leetcode 951 Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

Example 1:
        Flipped Trees Diagram
        Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
        Output: true
        Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
        Input: root1 = [], root2 = []
        Output: true

Example 3:
        Input: root1 = [], root2 = [1]
        Output: false
 

Constraints:
        The number of nodes in each tree is in the range [0, 100].
        Each tree will have unique node values in the range [0, 99].
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
    def flipEquiv(self, root1, root2):
        """
        Determine if two binary trees are flip equivalent.
        Flip equivalence means that the trees are either identical, 
        or one can be transformed into the other by swapping the left and right children 
        of some nodes any number of times.
        
        Parameters:
        root1 (TreeNode): The root of the first binary tree.
        root2 (TreeNode): The root of the second binary tree.
        
        Returns:
        bool: True if the two trees are flip equivalent, False otherwise.
        """
        
        def checker(node1, node2):
            """
            Recursively check if two nodes are flip equivalent.
            
            Parameters:
            node1 (TreeNode): Current node from the first tree.
            node2 (TreeNode): Current node from the second tree.
            
            Returns:
            bool: True if the subtrees rooted at node1 and node2 are flip equivalent, False otherwise.
            """
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return ((checker(node1.left, node2.left) or checker(node1.left, node2.right)) and
                    (checker(node1.right, node2.right) or checker(node1.right, node2.left)))
        
        return checker(root1, root2)
