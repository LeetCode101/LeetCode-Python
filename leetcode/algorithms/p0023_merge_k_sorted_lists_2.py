import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeWrap:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = [ListNodeWrap(node) for node in lists if node]
        heapq.heapify(queue)
        dummy = ListNode(-1)
        prev = dummy

        while queue:
            node_wrap = heapq.heappop(queue)
            prev.next = ListNode(node_wrap.node.val)
            prev = prev.next
            node = node_wrap.node.next

            if node:
                heapq.heappush(queue, ListNodeWrap(node))

        return dummy.next
