// Leetcode Problem 141 - Linked List Cycle
// Dec. 1, 2023

#include <cstddef>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        ListNode *fast = head, *slow = head;

        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;

            if (slow == fast) return true;
        }
        return false;
    }
};