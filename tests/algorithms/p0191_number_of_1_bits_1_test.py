import unittest
from leetcode.algorithms.p0191_number_of_1_bits_1 import Solution


class TestNumberOf1Bits(unittest.TestCase):
    def test_number_of_1_bits(self):
        solution = Solution()

        self.assertEqual(3, solution.hammingWeight(11))
