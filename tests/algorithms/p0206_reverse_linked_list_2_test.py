import unittest
from leetcode.algorithms.p0206_reverse_linked_list_2 \
    import Solution, ListNode


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)
        e = ListNode(5)
        d.next = e
        c.next = d
        b.next = c
        a.next = b

        self.assertListEqual(
            [5, 4, 3, 2, 1],
            self.convert_linked_list_to_list(solution.reverseList(a)))

    def convert_linked_list_to_list(self, head):
        list, current = [], head

        while current is not None:
            list.append(current.val)

            current = current.next

        return list
