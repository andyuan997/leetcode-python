# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

class Solution:
    def isValidBST_X(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node.left and node.val <= node.left.val:
                return False
            if node.right and node.val >= node.right.val:
                return False
            dfs(node.right)

        return dfs(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            # 如果當前節點值不在合法範圍內，返回 False
            if node.val <= lower or node.val >= upper:
                return False

            # 遞迴檢查左子樹，左子樹的所有節點值必須小於當前節點值
            # 遞迴檢查右子樹，右子樹的所有節點值必須大於當前節點值
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root)


