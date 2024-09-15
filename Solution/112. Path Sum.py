class Solution(object):
    #遞迴
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False

        # 如果到達葉子節點，檢查 targetSum 是否等於該葉子節點的值
        if not root.left and not root.right:
            return targetSum == root.val

        # 減去當前節點的值，然後繼續遞迴檢查左右子樹
        remainingSum = targetSum - root.val

        leftTargetSum = self.hasPathSum(root.left, remainingSum)

        rightTargetSum = self.hasPathSum(root.right, remainingSum)

        return leftTargetSum or rightTargetSum