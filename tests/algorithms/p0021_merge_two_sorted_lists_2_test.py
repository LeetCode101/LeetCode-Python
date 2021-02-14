import unittest
from leetcode.algorithms.p0021_merge_two_sorted_lists_2 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(4)
        a.next = b
        b.next = c

        d = ListNode(1)
        e = ListNode(3)
        f = ListNode(4)
        d.next = e
        e.next = f

        self.assertListEqual(
            [1, 1, 2, 3, 4, 4],
            convert_linked_list_to_list(solution.mergeTwoLists(a, d)))

        a = ListNode(2)
        b = ListNode(3)
        a.next = b

        self.assertListEqual(
            [1, 2, 3],
            convert_linked_list_to_list(
                solution.mergeTwoLists(a, ListNode(1))))
