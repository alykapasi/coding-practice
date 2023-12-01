// Leetcode 206 - Reverse Linked List
// Dec. 1, 2023

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let temp = null, curr = head, node;
    while (curr) {
        node = curr.next;
        curr.next = temp;
        temp = curr;
        curr = node;
    }

    return temp;
};