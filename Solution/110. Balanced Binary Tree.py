# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node: TreeNode) -> int:
            if node is None:
                return 0  # 空節點的高度為 0

            # 計算左子樹的高度
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # 左子樹不平衡，提前結束

            # 計算右子樹的高度
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # 右子樹不平衡，提前結束

            # 如果左右子樹的高度差超過 1，返回 -1 表示不平衡
            if abs(left_height - right_height) > 1:
                return -1

            # 否則返回當前節點的高度
            return max(left_height, right_height) + 1

        # 使用 check_height 函數檢查整棵樹是否平衡
        return check_height(root) != -1





