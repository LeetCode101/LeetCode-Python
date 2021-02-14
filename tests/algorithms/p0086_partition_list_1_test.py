import unittest
from leetcode.algorithms.p0086_partition_list_1 \
    import Solution, ListNode
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestPartitionList(unittest.TestCase):
    def test_partition_list(self):
        solution = Solution()
        a = ListNode(1)
        b = ListNode(4)
        c = ListNode(3)
        d = ListNode(2)
        e = ListNode(5)
        f = ListNode(2)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertListEqual(
            [1, 2, 2, 4, 3, 5],
            convert_linked_list_to_list(solution.partition(a, 3)))
