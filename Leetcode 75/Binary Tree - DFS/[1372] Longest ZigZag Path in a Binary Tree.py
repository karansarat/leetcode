# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, isLeft, cnt):
            if node is None: return cnt
            if isLeft:  return max(dfs(node.right, 0, cnt + 1), dfs(node.left, 1, 0))
            return max(dfs(node.left, 1, cnt + 1), dfs(node.right, 0, 0))
        return max(dfs(root.left, 1, 0), dfs(root.right, 0, 0))
