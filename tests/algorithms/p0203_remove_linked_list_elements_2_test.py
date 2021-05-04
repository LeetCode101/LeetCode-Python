import unittest
from leetcode.algorithms.p0203_remove_linked_list_elements_2 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class RemoveLinkedListElements(unittest.TestCase):
    def test_remove_linked_list_elements(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(6)
        d = ListNode(3)
        e = ListNode(4)
        f = ListNode(5)
        g = ListNode(6)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g

        self.assertListEqual(
            [1, 2, 3, 4, 5],
            convert_linked_list_to_list(solution.removeElements(a, 6)))
