/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int k = lists.length;
        if (k == 0) return null;
        
        return mergeKLists(lists, 0, k-1);
    }
    
    public ListNode mergeKLists(ListNode[] lists, int start, int end) {
        if (end - start == 0) return lists[start];
        if (end - start == 1) {
            return mergeLists(lists[start], lists[end]);
        }  
        
        int mid = start + ((end - start) / 2);
        ListNode listA = mergeKLists(lists, start, mid);
        ListNode listB = mergeKLists(lists, mid+1, end);
        
        return mergeLists(listA, listB);
    }

    
    
    public ListNode mergeLists(ListNode listA, ListNode listB) {
        if (listA == null) return listB;
        if (listB == null) return listA;
        
        if (listA.val < listB.val) {
            listA.next = mergeLists(listA.next, listB);
            return listA;
        } 
        else {
            listB.next = mergeLists(listA, listB.next);
            return listB;
        } 
    }
}