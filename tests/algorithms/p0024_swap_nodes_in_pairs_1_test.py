import unittest
from leetcode.algorithms.p0024_swap_nodes_in_pairs_1 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestSwapNodesInPairs(unittest.TestCase):
    def test_swap_nodes_in_pairs(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        a.next = b
        b.next = c
        c.next = d

        self.assertListEqual(
            [2, 1, 4, 3], convert_linked_list_to_list(solution.swapPairs(a)))
