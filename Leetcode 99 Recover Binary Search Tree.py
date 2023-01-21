'''
99 Recover Binary Search Tree
 
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Example 1:
        Input: root = [1,3,null,null,2]
        Output: [3,1,null,null,2]
        Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
        Input: root = [3,1,4,null,null,2]
        Output: [2,1,4,null,null,3]
        Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:
        The number of nodes in the tree is in the range [2, 1000].
        -231 <= Node.val <= 231 - 1
'''
class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    pred = None
    x = None  # 1st wrong node
    y = None  # 2nd wrong node
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      if pred and root.val < pred.val:
        y = root
        if not x:
          x = pred
      pred = root
      root = root.right

    def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
      temp = x.val
      x.val = y.val
      y.val = temp

    swap(x, y)
