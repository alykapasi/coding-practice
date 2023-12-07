## Leetcode Problem 19 - Remove Nth Node From Linked List
## Dec. 4, 2023

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        fast, slow = temp, temp

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next. fast.next
        
        slow.next = slow.next.next

        return temp.next

    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1, size = head, 0

        while temp1:
            size += 1
            temp1 = temp1.head

        if size == n:
            return head.next
        
        for i in range(size - n - 1):
            temp2 = temp2.next

        temp2.next = temp2.next.next

        return head