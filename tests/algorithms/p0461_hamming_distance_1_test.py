import unittest
from leetcode.algorithms.p0461_hamming_distance_1 import Solution


class TestHammingDistance(unittest.TestCase):
    def test_hamming_distance(self):
        solution = Solution()

        self.assertEqual(2, solution.hammingDistance(1, 4))
        self.assertEqual(2, solution.hammingDistance(4, 1))
