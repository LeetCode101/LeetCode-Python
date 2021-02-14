import unittest
from leetcode.algorithms.p0445_add_two_numbers_ii_3 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        solution = Solution()
        a = ListNode(7)
        b = ListNode(2)
        c = ListNode(4)
        d = ListNode(3)
        a.next = b
        b.next = c
        c.next = d

        e = ListNode(5)
        f = ListNode(6)
        g = ListNode(4)
        e.next = f
        f.next = g

        self.assertListEqual(
            [7, 8, 0, 7],
            convert_linked_list_to_list(solution.addTwoNumbers(a, e)))
        self.assertListEqual(
            [1, 0],
            convert_linked_list_to_list(
                solution.addTwoNumbers(ListNode(5), ListNode(5))))
