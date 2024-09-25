# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # 遞迴解法
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

            # 交換左右子樹
        root.left, root.right = root.right, root.left

        # 遞迴對左右子樹進行翻轉
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    # Queue
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()

            # 交換左右子樹
            current.left, current.right = current.right, current.left

            # 將左右子樹節點加入隊列中
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root
