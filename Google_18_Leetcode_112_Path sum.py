'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum. A leaf is a node with no children.

'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs (node, curSum):
            if not node:
                return False
            
            curSum += node.val
            
            # if node has no child
            if not node.left and not node.right:
                return curSum == targetSum
            
            # check if the node has child
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        return dfs(root, 0)
	
