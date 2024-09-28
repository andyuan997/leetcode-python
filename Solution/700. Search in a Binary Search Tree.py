# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 基本情況：當節點為空或者找到目標值時，返回當前節點
        if root is None or root.val == val:
            return root

        # 如果目標值小於當前節點值，繼續在左子樹搜索
        if val < root.val:
            return self.searchBST(root.left, val)

        # 如果目標值大於當前節點值，繼續在右子樹搜索
        return self.searchBST(root.right, val)
