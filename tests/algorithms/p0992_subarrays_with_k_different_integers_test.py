import unittest
from leetcode.algorithms.p0992_subarrays_with_k_different_integers \
    import Solution


class TestSubarraysWithKDifferentIntegers(unittest.TestCase):
    def test_subarrays_with_k_different_integers(self):
        solution = Solution()

        self.assertEqual(3, solution.subarraysWithKDistinct(
            [1, 2, 1, 3, 4], 3))
