'''
Leetcode 226 - Invert Binary Tree - Depth First Search
Given the root of a binary tree, invert the tree, and return its root.

Solution
    Runtime complexity: O(N)
    Space complexity: O(N) 

      This problem is quite straightforward. For this algorithm, we will utilize a post order traversal of the binary tree.
      For each node, we will swap its left and right child.

'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None

        # swap the child Nodes
        tmp = root.left
        root.left = root.right 
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
      
