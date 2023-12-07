// Leetcode Problem 21 - Merge Two Sorted Lists
// Dec. 2, 2023


struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (!list1) return list2;
    if (!list2) return list1;

    struct ListNode* ans;
    if (list1->val < list2->val) {
        ans = list1;
        list1 = list1->next;
    } else {
        ans = list2;
        list2 = list2->next;
    }

    struct ListNode* temp = ans;

    while (list1 && list2) {
        if (list1->val < list2->val) {
            temp->next = list1;
            list1 = list1->next;
        } else {
            temp->next = list2;
            list2 = list2->next;
        }
        temp = temp->next;
    }

    temp->next = list1 ? list1 : list2;

    return ans;
}