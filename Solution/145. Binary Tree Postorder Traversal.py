# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if not root:
            return []

        def dfs(output, node):
            if not node:
                return
            dfs(output, node.left)
            dfs(output, node.right)
            output.append(node.val)

        dfs(output, root)
        return output
