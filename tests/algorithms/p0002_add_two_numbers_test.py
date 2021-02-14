import unittest
from leetcode.algorithms.p0002_add_two_numbers \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        solution = Solution()
        a = ListNode(2)
        b = ListNode(4)
        c = ListNode(3)
        a.next = b
        b.next = c

        d = ListNode(5)
        e = ListNode(6)
        f = ListNode(4)
        d.next = e
        e.next = f

        self.assertListEqual(
            [7, 0, 8],
            convert_linked_list_to_list(solution.addTwoNumbers(a, d)))
        self.assertListEqual(
            [0, 1],
            convert_linked_list_to_list(
                solution.addTwoNumbers(ListNode(5), ListNode(5))))
