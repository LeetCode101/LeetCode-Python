import unittest
from leetcode.algorithms.p1102_path_with_maximum_minimum_value_2 \
    import Solution


class TestPathWithMaximumMinimumValue(unittest.TestCase):
    def test_path_with_maximum_minimum_value(self):
        solution = Solution()

        self.assertEqual(4, solution.maximumMinimumPath(
            [[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
        self.assertEqual(2, solution.maximumMinimumPath(
            [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]))
        self.assertEqual(3, solution.maximumMinimumPath(
            [[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7],
             [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]))
