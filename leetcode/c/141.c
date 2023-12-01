// Leetcode Problem 141 - Linked List Cycle
// Dec. 1, 2023

#include <stdbool.h>
#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    if (head == NULL) return false;
    struct ListNode *fast = head, *slow = head;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast) return true;
    }
    return false;
}