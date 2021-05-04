import unittest
from leetcode.algorithms.p0708_insert_into_a_sorted_circular_linked_list \
    import Solution, Node
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
        e = Node(1)
        f = Node(3)
        g = Node(5)
        e.next = f
        f.next = g
        g.next = e
        h = Node(3)
        i = Node(4)
        j = Node(1)
        h.next = i
        i.next = j
        j.next = h

        self.assertListEqual([1], convert_circular_linked_list_to_list(
            solution.insert(None, 1)))
        self.assertListEqual([1, 0], convert_circular_linked_list_to_list(
            solution.insert(d, 0)))
        self.assertListEqual(
            [3, 4, 1, 2],
            convert_circular_linked_list_to_list(solution.insert(a, 2)))
        self.assertListEqual(
            [1, 2, 3, 5],
            convert_circular_linked_list_to_list(solution.insert(e, 2)))
        self.assertListEqual(
            [3, 4, 0, 1],
            convert_circular_linked_list_to_list(solution.insert(h, 0)))
