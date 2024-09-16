from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #bfs
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])  # 使用雙端隊列進行層序遍歷

        while queue:
            level_length = len(queue)

            # 遍歷當前層的所有節點
            for i in range(level_length):
                node = queue.popleft()
                # 如果是該層的最後一個節點，將它加入結果
                if i == level_length - 1:
                    result.append(node.val)

                # 將左右子節點加入隊列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
    #dfs
    def rightSideView_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def dfs(node, level):
            if not node:
                return

            # 如果當前層級還沒有加入到結果中，則加入該層第一個訪問到的節點
            if level == len(result):
                result.append(node.val)

            # 先遞迴右子樹，確保右邊的節點優先加入結果
            dfs(node.right, level + 1)
            # 然後遞迴左子樹
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result