import unittest
from leetcode.algorithms.p0237_delete_node_in_a_linked_list \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class DeleteNodeInALinkedList(unittest.TestCase):
    def test_delete_node_in_a_linked_list(self):
        solution = Solution()
        a = ListNode(4)
        b = ListNode(5)
        c = ListNode(2)
        d = ListNode(9)
        a.next = b
        b.next = c
        c.next = d

        solution.deleteNode(b)

        self.assertListEqual(
            [2, 9], convert_linked_list_to_list(b))
