import unittest
from leetcode.algorithms.p0061_rotate_list_2 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestRotateList(unittest.TestCase):
    def test_rotate_list(self):
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
            [4, 5, 1, 2, 3],
            convert_linked_list_to_list(solution.rotateRight(a, 2)))
        self.assertListEqual(
            [1],
            convert_linked_list_to_list(solution.rotateRight(ListNode(1), 0)))
        self.assertIsNone(solution.rotateRight(None, 1))
