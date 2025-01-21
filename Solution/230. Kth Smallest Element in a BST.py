class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0

        def dfs(node):
            if not node:
                return None
            
            # 遍歷左子樹，檢查是否找到了結果
            left = dfs(node.left)
            if left is not None:
                return left
            
            # 計數器加1，表示已經遍歷了一個節點
            self.counter += 1
            
            # 當計數器等於 k 時，返回當前節點值
            if self.counter == k:
                return node.val
            
            # 遍歷右子樹，檢查是否找到了結果
            return dfs(node.right)

        # 從根節點開始進行 DFS 遍歷，並返回結果
        return dfs(root)
