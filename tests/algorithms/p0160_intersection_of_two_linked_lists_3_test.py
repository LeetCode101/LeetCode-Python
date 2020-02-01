import unittest
from leetcode.algorithms.p0160_intersection_of_two_linked_lists_3 \
    import Solution, ListNode


class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def test_intersection_of_two_linked_lists(self):
        solution = Solution()
        a1 = ListNode(4)
        a2 = ListNode(1)
        a1.next = a2
        b1 = ListNode(5)
        b2 = ListNode(0)
        b3 = ListNode(1)
        b1.next = b2
        b2.next = b3
        c1 = ListNode(8)
        c2 = ListNode(4)
        c3 = ListNode(5)
        c1.next = c2
        c2.next = c3
        b3.next = c1
        a2.next = c1

        self.assertIsNone(solution.getIntersectionNode(a1, None))
        self.assertEqual(8, solution.getIntersectionNode(a1, b1).val)
