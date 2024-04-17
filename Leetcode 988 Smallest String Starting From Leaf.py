'''
Leetcode 988 Smallest String Starting From Leaf

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:
        Input: root = [0,1,2,3,4,3,4]
        Output: "dba"

Example 2:
        Input: root = [25,1,3,1,3,0,2]
        Output: "adz"

Example 3:
        Input: root = [2,2,1,null,1,0,null,0]
        Output: "abc"
 
Constraints:
        The number of nodes in the tree is in the range [1, 8500].
        0 <= Node.val <= 25

'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], path: list, smallest: list) -> None:
            if node is None:
                return

            # Convert current node's value to corresponding character and add to path
            path.append(chr(node.val + ord('a')))
            
            # Check if the current node is a leaf node
            if node.left is None and node.right is None:
                # Form the string from leaf to root by reversing the path
                current_string = ''.join(reversed(path))
                # Update the smallest string found if the current one is smaller
                if current_string < smallest[0]:
                    smallest[0] = current_string
            
            # Continue DFS on child nodes
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            
            # Backtrack by removing the last character added to path
            path.pop()

        # Use a high initial value for smallest to ensure any valid path will be smaller
        smallest = ['{' * 26]  # '{' is the character right after 'z' in ASCII

        # Start DFS from root
        dfs(root, [], smallest)

        return smallest[0]

# Example of using this class would be needed here if required.
