import unittest
from leetcode.algorithms.p0206_reverse_linked_list_1 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
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
            [5, 4, 3, 2, 1],
            convert_linked_list_to_list(solution.reverseList(a)))
