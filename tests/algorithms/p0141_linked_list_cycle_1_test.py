import unittest
from leetcode.algorithms.p0141_linked_list_cycle_1 \
    import Solution, ListNode


class TestLinkedListCycle(unittest.TestCase):
    def test_linked_list_cycle(self):
        solution = Solution()
        a = ListNode(3)
        b = ListNode(2)
        c = ListNode(0)
        d = ListNode(-4)
        c.next = d
        b.next = c
        a.next = b
        d.next = a

        self.assertTrue(solution.hasCycle(a))
        self.assertFalse(solution.hasCycle(ListNode(1)))
