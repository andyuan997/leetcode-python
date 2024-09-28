# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 初始總和為0
        self.range_sum = 0

        def dfs(node):
            if not node:
                return  # 節點為空時直接返回
            # 節點值在範圍內，加入總和
            if low <= node.val <= high:
                self.range_sum += node.val
            # 節點值大於low，遞歸處理左子樹
            if node.val > low:
                dfs(node.left)
            # 節點值小於high，遞歸處理右子樹
            if node.val < high:
                dfs(node.right)

        # 呼叫深度優先搜尋函數
        dfs(root)
        return self.range_sum  
