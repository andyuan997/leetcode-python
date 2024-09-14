# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    #遞迴
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 如果兩個節點都是 None，表示這兩個子樹相同
        if not p and not q:
            return True
        # 如果只有一個節點為 None，表示這兩個子樹不同
        if not p or not q:
            return False
        # 如果節點的值不同，表示這兩個子樹不同
        if p.val != q.val:
            return False
        # 遞迴檢查左子樹和右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
