import unittest
from leetcode.algorithms.p1019_next_greater_node_in_linked_list_2 \
    import Solution, ListNode


class TestNextGreaterNodeInLinkedList(unittest.TestCase):
    def test_next_greater_node_in_linked_list(self):
        solution = Solution()
        head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))

        self.assertListEqual([], solution.nextLargerNodes(None))
        self.assertListEqual([7, 0, 5, 5, 0], solution.nextLargerNodes(head))
