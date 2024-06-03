/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        bool sorted = false;
        ListNode* ans = new ListNode();
        ListNode* head = ans;
        while (!sorted) {
            if (list1 == NULL && list2 == NULL) {
                sorted = true;
                continue;
            }

            if (list1 == NULL || list2 == NULL) {
                while (list1 == NULL && list2 != NULL) {
                    ListNode* node = new ListNode(list2->val);
                    head->next = node;
                    head = head->next;
                    list2 = list2->next;
                }

                while (list1 != NULL && list2 == NULL) {
                    ListNode* node = new ListNode(list1->val);
                    head->next = node;
                    head = head->next;
                    list1 = list1->next;
                }
                sorted = true;
                continue;
            }

            if (list1->val < list2->val) {
                ListNode* node = new ListNode(list1->val);
                head->next = node;
                head = head->next;
                list1 = list1->next;
            } else {
                ListNode* node = new ListNode(list2->val);
                head->next = node;
                head = head->next;
                list2 = list2->next;
            }
        }
        return ans->next;
    }
};