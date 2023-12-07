## Leetcode Problem 23 - Merge k Sorted Lists
## Dec. 3, 2023

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i, list_node in enumerate(lists):
            heapq.heappush(pq, (list_node.val, i, list_node))

        ans = ListNode()
        temp = ans

        while pq:
           _, i, node = heapq.heappop(pq)
           temp.next = node
           temp = temp.next
           if node.next:
               heapq.heappush(pq, (node.next.val, i, node.next))

        return ans.next 