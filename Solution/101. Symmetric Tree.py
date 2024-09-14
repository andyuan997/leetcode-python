# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    #遞迴
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def isMirror(t1, t2):
            # 如果兩個子節點都是 None，則鏡像
            if not t1 and not t2:
                return True
            # 如果只有一個子節點為 None，則不鏡像
            if not t1 or not t2:
                return False
            # 兩個節點的值相等，並且它們的左右子樹鏡像
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        
        return isMirror(root.left, root.right)
