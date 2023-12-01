// Leetcode Problem 141 - Linked List Cycle
// Dec. 1, 2023

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    if (head === null) return false;
    let fast = head, slow = head;
    while (fast !== null && fast.next !== null) {
        fast = fast.next.next;
        slow = slow.next;
        if (slow === fast) return true;
    }
    return false;
};