## Leetcode 206 - Reverse Linked List
## Dec. 1, 2023

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        curr = head
        while curr:
            node = curr.next
            curr.next = temp
            temp = curr
            curr = node
        return temp