// Leetcode 206 - Reverse Linked List
// Dec. 1, 2023

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* temp = nullptr;
        ListNode* node = nullptr;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            node = curr->next;
            curr->next = temp;
            temp = curr;
            curr = node;
        }

        return temp;
    }
};