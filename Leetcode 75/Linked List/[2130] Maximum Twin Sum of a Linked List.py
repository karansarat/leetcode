# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast, slow, stack, twinSum = head, head, [], 0
        
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow)
            slow = slow.next
        
        while slow:
            twinSum = max(twinSum, stack.pop().val + slow.val)
            slow = slow.next
        
        return twinSum
            