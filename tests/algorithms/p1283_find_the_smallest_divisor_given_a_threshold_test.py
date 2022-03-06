import unittest
from leetcode.algorithms.p1283_find_the_smallest_divisor_given_a_threshold \
    import Solution


class TestFindTheSmallestDivisorGivenAThreshold(unittest.TestCase):
    def test_find_the_smallest_divisor_given_a_threshold(self):
        solution = Solution()

        self.assertEqual(5, solution.smallestDivisor([1, 2, 5, 9], 6))
        self.assertEqual(44, solution.smallestDivisor([44, 22, 33, 11, 1], 5))
