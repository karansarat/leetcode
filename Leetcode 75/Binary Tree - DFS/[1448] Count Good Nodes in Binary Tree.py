# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxVal):
            if not node:
                return 0
            
            good = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)            
            return good + dfs(node.left, maxVal) + dfs(node.right, maxVal)
        
        return dfs(root, root.val)