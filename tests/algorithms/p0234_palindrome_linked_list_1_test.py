import unittest
from leetcode.algorithms.p0234_palindrome_linked_list_1 \
    import Solution, ListNode


class TestPalindromeLinkedList(unittest.TestCase):
    def test_palindrome_linked_list(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(2)
        d = ListNode(1)
        a.next = b
        b.next = c
        c.next = d

        self.assertTrue(solution.isPalindrome(a))
        self.assertFalse(solution.isPalindrome(ListNode(1, ListNode(2))))
