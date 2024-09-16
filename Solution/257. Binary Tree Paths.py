# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        out_str = ""
        all_out_str = []
        def dfs(out_str, all_out_str, root):
            if not root:
                return

            out_str += str(root.val)

            if not root.left and not root.right:
                all_out_str.append(out_str)
                return

            out_str += "->"
            dfs(out_str, all_out_str, root.left)
            dfs(out_str, all_out_str, root.right)
        dfs(out_str, all_out_str, root)

        return all_out_str


