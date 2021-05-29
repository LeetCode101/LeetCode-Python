import unittest
from leetcode.algorithms.p0421_maximum_xor_of_two_numbers_in_an_array \
    import Solution


class TestMaximumXOROfTwoNumbersInAnArray(unittest.TestCase):
    def test_maximum_xor_of_two_numbers_in_an_array(self):
        solution = Solution()

        self.assertEqual(28, solution.findMaximumXOR([3, 10, 5, 25, 2, 8]))
