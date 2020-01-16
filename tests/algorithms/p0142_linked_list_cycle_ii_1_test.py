import unittest
from leetcode.algorithms.p0142_linked_list_cycle_ii_1 \
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
        d.next = b

        self.assertEqual(b, solution.detectCycle(a))
