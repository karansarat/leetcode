# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0: return head
        if not head: return head 
        listLen = 1
        ptr = head
        while ptr.next:
            listLen += 1
            ptr = ptr.next
        k = k % listLen
        ptr.next = head
        node = head
        for i in range(listLen - k - 1):
            node =  node.next
        ans = node.next
        node.next = None

        return ans
