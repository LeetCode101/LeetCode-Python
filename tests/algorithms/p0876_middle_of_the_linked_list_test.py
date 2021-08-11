import unittest
from leetcode.algorithms.p0876_middle_of_the_linked_list \
    import Solution, ListNode


class TestMiddleOfTheLinkedList(unittest.TestCase):
    def test_middle_of_the_linked_list(self):
        solution = Solution()
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(
            4, ListNode(5, ListNode(6))))))

        self.assertIsNone(solution.middleNode(None))
        self.assertEqual(4, solution.middleNode(head).val)
