'''

103 Binary Tree Zigzag Level Order Traversal
Medium
8K
209
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 

class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    ans = []
    q = collections.deque([root])
    isLeftToRight = True

    while q:
      size = len(q)
      currLevel = [0] * size
      for i in range(size):
        node = q.popleft()
        index = i if isLeftToRight else size - i - 1
        currLevel[index] = node.val
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      ans.append(currLevel)
      isLeftToRight = not isLeftToRight

    return ans
