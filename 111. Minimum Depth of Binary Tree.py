class Solution:
    def minDepth(self, root):
        # 如果根節點是空的，返回 0
        if not root:
            return 0

        # 如果是葉子節點，返回 1
        if not root.left and not root.right:
            return 1

        # 如果左子樹或右子樹是空的，取非空的子樹的最小深度
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        # 如果左右子樹都存在，取左右子樹中較小的深度
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
