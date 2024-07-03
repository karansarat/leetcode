# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = [root] if root else []
        while stack:
            newStack = []
            result.append(stack[-1].val)
            for n in stack:
                if n.left: newStack.append(n.left)
                if n.right: newStack.append(n.right)
            stack = newStack
        return result
