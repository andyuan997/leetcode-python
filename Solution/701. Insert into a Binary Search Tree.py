# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 如果樹是空的，直接回傳新節點
        if not root:
            return TreeNode(val)
        
        # 遞迴遍歷樹找到合適的位置進行插入
        if val < root.val:
            # 如果 val 小於當前節點值，往左子樹走
            root.left = self.insertIntoBST(root.left, val)
        else:
            # 如果 val 大於當前節點值，往右子樹走
            root.right = self.insertIntoBST(root.right, val)
        
        # 回傳最終的根節點
        return root
