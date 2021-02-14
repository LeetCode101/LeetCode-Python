import unittest
from leetcode.algorithms.p0019_remove_nth_node_from_end_of_list_3 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    def test_remove_nth_node_from_end_of_list(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        e = ListNode(5)
        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertListEqual(
            [1, 2, 3, 5],
            convert_linked_list_to_list(solution.removeNthFromEnd(a, 2)))
        self.assertIsNone(solution.removeNthFromEnd(ListNode(1), 1))
