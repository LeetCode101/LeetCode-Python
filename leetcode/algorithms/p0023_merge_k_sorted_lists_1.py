from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self._merge(lists, 0, len(lists) - 1)

    def _merge(self, lists: List[ListNode], low: int, high: int) -> ListNode:
        if low > high:
            return None

        if low == high:
            return lists[low]

        middle = (low + high) // 2
        list1, list2 = \
            self._merge(lists, low, middle), \
            self._merge(lists, middle + 1, high)

        return self._merge_two_lists(list1, list2)

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy
        current1, current2 = l1, l2

        while current1 and current2:
            new = None

            if current1.val <= current2.val:
                new, current1 = current1, current1.next
            else:
                new, current2 = current2, current2.next

            prev.next, prev = new, new

        if current1:
            prev.next = current1

        if current2:
            prev.next = current2

        return dummy.next
