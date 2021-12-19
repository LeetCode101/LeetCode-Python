import unittest
from leetcode.algorithms.p0547_number_of_provinces import Solution


class TestNumberOfProvinces(unittest.TestCase):
    def test_number_of_provinces(self):
        solution = Solution()

        self.assertEqual(2, solution.findCircleNum(
            [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEqual(3, solution.findCircleNum(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
