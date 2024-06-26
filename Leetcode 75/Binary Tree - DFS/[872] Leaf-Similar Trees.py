# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []
        def recursive(root, leaf):
            if not root.left and not root.right:
                leaf.append(root.val)
            if root.left:
                recursive(root.left, leaf)
            if root.right:
                recursive(root.right, leaf)

        recursive(root1, leaf1)
        recursive(root2, leaf2)

        return leaf1 == leaf2