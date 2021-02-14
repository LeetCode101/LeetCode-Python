import unittest
from leetcode.algorithms.p0025_reverse_nodes_in_k_group \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestReverseNodesInKGroup(unittest.TestCase):
    def test_reverse_nodes_in_k_group(self):
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
            [2, 1, 4, 3, 5],
            convert_linked_list_to_list(solution.reverseKGroup(a, 2)))
