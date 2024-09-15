# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    # Stack方法
    def maxDepth_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:  # 如果樹是空的，深度為0
            return 0

        stack = [(root, 1)]  # 堆疊保存 (節點, 深度) 元組
        max_depth = 0

        while stack:
            node, depth = stack.pop()  # 取出當前節點和深度

            if node:
                max_depth = max(max_depth, depth)  # 更新最大深度
                # 注意：先將右子節點壓入堆疊，再壓入左子節點
                # 這樣左子節點會先被處理，符合 DFS 的特性
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))

        return max_depth

    # 遞迴方法
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:  # 如果樹是空的，深度為0
            return 0

        # 遞迴計算左子樹和右子樹的最大深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 返回較大的深度並加上當前節點的深度（1）
        return max(left_depth, right_depth) + 1