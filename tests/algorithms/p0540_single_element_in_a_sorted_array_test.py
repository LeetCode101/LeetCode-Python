import unittest
from leetcode.algorithms.p0540_single_element_in_a_sorted_array import Solution


class TestSingleElementInASortedArray(unittest.TestCase):
    def test_single_element_in_a_sorted_array(self):
        solution = Solution()

        self.assertEqual(2, solution.singleNonDuplicate(
            [1, 1, 2, 3, 3, 4, 4, 8, 8]))
        self.assertEqual(10, solution.singleNonDuplicate(
            [3, 3, 7, 7, 10, 11, 11]))
