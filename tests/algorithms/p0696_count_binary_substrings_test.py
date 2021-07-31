import unittest
from leetcode.algorithms.p0696_count_binary_substrings import Solution


class TestCountBinarySubstrings(unittest.TestCase):
    def test_count_binary_substrings(self):
        solution = Solution()

        self.assertEqual(6, solution.countBinarySubstrings('00110011'))
