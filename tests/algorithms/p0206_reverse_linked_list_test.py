import unittest
from leetcode.algorithms.p0206_reverse_linked_list_1 \
    import Solution as Solution1, ListNode as ListNode1
from leetcode.algorithms.p0206_reverse_linked_list_2 \
    import Solution as Solution2, ListNode as ListNode2


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list1(self):
        solution = Solution1()
        a = ListNode1(1)
        b = ListNode1(2)
        c = ListNode1(3)
        d = ListNode1(4)
        e = ListNode1(5)
        d.next = e
        c.next = d
        b.next = c
        a.next = b

        self.assertListEqual(
            [5, 4, 3, 2, 1],
            self.convert_linked_list_to_list(solution.reverseList(a)))

    def test_reverse_linked_list2(self):
        solution = Solution2()
        a = ListNode2(1)
        b = ListNode2(2)
        c = ListNode2(3)
        d = ListNode2(4)
        e = ListNode2(5)
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
