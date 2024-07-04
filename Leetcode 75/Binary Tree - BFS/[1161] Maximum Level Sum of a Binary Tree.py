# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        levels = defaultdict(int)
        def sumVals(root, depth):
            if root:
                levels[depth] += root.val
                sumVals(root.left,  depth + 1)
                sumVals(root.right, depth + 1)
			
        sumVals(root, 1)
        return max(levels, key=levels.get)