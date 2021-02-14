import unittest
from leetcode.algorithms.p0092_reverse_linked_list_ii_2 \
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
            [1, 4, 3, 2, 5],
            convert_linked_list_to_list(solution.reverseBetween(a, 2, 4)))

        a1 = ListNode(3)
        b1 = ListNode(5)
        a1.next = b1

        self.assertListEqual([5, 3],
                             convert_linked_list_to_list(
                                 solution.reverseBetween(a1, 1, 2)))
