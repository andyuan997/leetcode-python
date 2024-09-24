# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return []

        def dfs(output, node):
            if not node:
                return
            output.append(node.val)
            dfs(output, node.left)
            dfs(output, node.right)

        dfs(output, root)
        return output
