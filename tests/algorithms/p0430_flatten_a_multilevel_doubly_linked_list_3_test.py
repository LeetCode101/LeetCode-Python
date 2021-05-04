import unittest
from leetcode.algorithms.p0430_flatten_a_multilevel_doubly_linked_list_3 \
    import Solution, Node
from tests.algorithms.list_helper import convert_linked_list_to_list


class TestFlattenAMultilevelDoublyLinkedList(unittest.TestCase):
    def test_flatten_a_multilevel_doubly_linked_list(self):
        solution = Solution()
        n1 = Node(1, None, None, None)
        n2 = Node(2, None, None, None)
        n3 = Node(3, None, None, None)
        n4 = Node(4, None, None, None)
        n5 = Node(5, None, None, None)
        n6 = Node(6, None, None, None)
        n7 = Node(7, None, None, None)
        n8 = Node(8, None, None, None)
        n9 = Node(9, None, None, None)
        n10 = Node(10, None, None, None)
        n11 = Node(11, None, None, None)
        n12 = Node(12, None, None, None)
        n1.next = n2
        n2.prev = n1
        n2.next = n3
        n3.prev = n2
        n3.next = n4
        n4.prev = n3
        n4.next = n5
        n5.prev = n4
        n5.next = n6
        n6.prev = n5
        n3.child = n7
        n7.next = n8
        n8.prev = n7
        n8.next = n9
        n9.prev = n8
        n9.next = n10
        n10.prev = n9
        n8.child = n11
        n11.next = n12
        n12.prev = n11

        self.assertListEqual([], convert_linked_list_to_list(
            solution.flatten(None)))
        self.assertListEqual([1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6],
                             convert_linked_list_to_list(solution.flatten(n1)))
