# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rigthElements = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            rigthElements.append(node.val)

        return rigthElements