import unittest
from leetcode.algorithms.p0708_insert_into_a_sorted_circular_linked_list \
    import Node, Solution
from tests.algorithms.list_helper import convert_circular_linked_list_to_list


class TestInsertIntoASortedCircularLinkedList(unittest.TestCase):
    def test_insert_into_a_sorted_circular_linked_list(self):
        solution = Solution()
        a = Node(3)
        b = Node(4)
        c = Node(1)
        d = Node(1)
        a.next = b
        b.next = c
        c.next = a
        d.next = d

        self.assertListEqual([1], convert_circular_linked_list_to_list(
            solution.insert(None, 1)))
        self.assertListEqual([1, 0], convert_circular_linked_list_to_list(
            solution.insert(d, 0)))
        self.assertListEqual(
            [3, 4, 1, 2],
            convert_circular_linked_list_to_list(solution.insert(a, 2)))
