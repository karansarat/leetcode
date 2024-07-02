# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None

        prev = head
        mid = head.next
        midIndex = 1
        ptr = head.next
        n = 2
        while ptr:
            currMid = n / 2
            while currMid > midIndex:
                mid = mid.next
                prev = prev.next
                midIndex += 1
            n += 1
            ptr = ptr.next
        prev.next = mid.next
        return head