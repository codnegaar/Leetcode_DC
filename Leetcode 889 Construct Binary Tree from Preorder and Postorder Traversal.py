'''
Leetcode 889 Construct Binary Tree from Preorder and Postorder Traversal
 
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and
postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
If there exist multiple answers, you can return any of them. 

Example 1:
        Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
        Output: [1,2,3,4,5,6,7]

Example 2:
        Input: preorder = [1], postorder = [1]
        Output: [1]
 

Constraints:
        1 <= preorder.length <= 30
        1 <= preorder[i] <= preorder.length
        All the values of preorder are unique.
        postorder.length == preorder.length
        1 <= postorder[i] <= postorder.length
        All the values of postorder are unique.
        It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            hold =  pre[1]
            for i in range(len(post)):
                if post[i] == hold:
                    break
            count = i + 1
            root.left = helper(pre[1:count + 1], post[:count])
            root.right = helper(pre[count + 1:], post[count:len(post) - 1])
            return root
        
        return helper(preorder, postorder)


# solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            hold =  pre[1]
            for i in range(len(post)):
                if post[i] == hold:
                    break
            count = i + 1
            root.left = helper(pre[1:count + 1], post[:count])
            root.right = helper(pre[count + 1:], post[count:len(post) - 1])
            return root
        
        return helper(preorder, postorder)

