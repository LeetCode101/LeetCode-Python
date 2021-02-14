import unittest
from leetcode.algorithms.p0138_copy_list_with_random_pointer \
    import Solution, Node
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestCopyListWithRandomPointer(unittest.TestCase):
    def test_copy_list_with_random_pointer(self):
        solution = Solution()
        a = Node(7)
        b = Node(13)
        c = Node(11)
        d = Node(10)
        e = Node(1)
        a.next = b
        a.random = e
        b.next = c
        b.random = a
        c.next = d
        c.random = e
        d.next = e
        e.random = a

        self.assertListEqual(
            [7, 13, 11, 10, 1],
            convert_linked_list_to_list(solution.copyRandomList(a)))
