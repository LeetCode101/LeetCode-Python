import unittest
from leetcode.algorithms.p0108_convert_sorted_array_to_binary_search_tree \
    import Solution


class TestConvertSortedArrayToBinarySearchTree(unittest.TestCase):
    def test_convert_sorted_array_to_binary_search_tree(self):
        solution = Solution()

        self.assertEqual(0, solution.sortedArrayToBST([-10, -3, 0, 5, 9]).val)
