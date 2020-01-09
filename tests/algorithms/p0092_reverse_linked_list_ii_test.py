import unittest
from leetcode.algorithms.p0092_reverse_linked_list_ii \
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
            [1, 4, 3, 2, 5],
            self.convert_linked_list_to_list(solution.reverseBetween(a, 2, 4)))

        a1 = ListNode(3)
        b1 = ListNode(5)
        a1.next = b1

        self.assertListEqual([5, 3],
                             self.convert_linked_list_to_list(
                                 solution.reverseBetween(a1, 1, 2)))

    def convert_linked_list_to_list(self, head):
        list, current = [], head

        while current is not None:
            list.append(current.val)

            current = current.next

        return list
