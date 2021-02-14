import unittest
from leetcode.algorithms.p0023_merge_k_sorted_lists_1 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestMergeKSortedLists(unittest.TestCase):
    def test_merge_k_sorted_lists(self):
        solution = Solution()
        a = ListNode(-1)
        b = ListNode(5)
        c = ListNode(11)
        a.next = b
        b.next = c

        d = ListNode(6)
        e = ListNode(10)
        d.next = e

        self.assertListEqual(
            [-1, 5, 6, 10, 11],
            convert_linked_list_to_list(
                solution.mergeKLists([None, a, None, d])))
        self.assertIsNone(solution.mergeKLists([]))
