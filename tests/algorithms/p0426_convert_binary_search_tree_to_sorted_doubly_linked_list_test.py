import unittest
from leetcode.algorithms\
    .p0426_convert_binary_search_tree_to_sorted_doubly_linked_list \
    import Solution, Node


class TestConvertBinarySearchTreeToSortedDoublyLinkedList(unittest.TestCase):
    def test_convert_binary_search_tree_to_sorted_doubly_linked_list(self):
        solution = Solution()
        root = Node(
            4,
            Node(2, Node(1), Node(3)),
            Node(5)
        )

        self.assertEqual(2, solution.treeToDoublyList(root).right.val)
