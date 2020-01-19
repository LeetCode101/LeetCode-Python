import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = [(node.val, id(node), node) for node in lists if node]
        heapq.heapify(queue)
        dummy = ListNode(-1)
        prev = dummy

        while queue:
            value, node_id, node = heapq.heappop(queue)
            prev.next = ListNode(value)
            prev = prev.next
            node = node.next

            if node:
                heapq.heappush(queue, (node.val, id(node), node))

        return dummy.next
