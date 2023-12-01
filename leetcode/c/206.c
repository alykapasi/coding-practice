// Leetcode 206 - Reverse Linked List
// Dec. 1, 2023

#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* temp = NULL;
    struct ListNode* curr = head;
    struct ListNode* node = NULL;

    while (curr != NULL) {
        node = curr->next;
        curr->next = temp;
        temp = curr;
        curr = node;
    }

    return temp;
}